"""Converts markdown files and jupyter notebooks in a directory to html files

This file:
- gets config values from config.ini file
- reads all markdown files in a folder, parses front matter, saves info in a Posts dataclass
- returns a  sorted dict of Posts and a dict of tags: post_slugs 


"""

# libs built into python
import os
import shutil
import json
from pathlib import Path
from dataclasses import dataclass
from configparser import ConfigParser
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Optional

# external libs, try to minimize use
import yaml

# import nbformat

# import pandas as pd  # no real need to use this so rethink later
from mako.template import Template
from mako.lookup import TemplateLookup

# from tqdm.auto import tqdm
from datetime import datetime
import markdown
import pymdownx.emoji

# import nbconvert


@dataclass
class Post:
    """class to store each individual posts data"""

    title: str
    type: str  # type of content post, notebook, link, etc
    slug: str
    link: str  # relative link to post in form tag/slug.html
    path: Path
    tags: List[str]
    markdown: str
    html: str
    date: datetime
    lastmod: datetime
    toc: Optional[str]
    draft: bool = False


##################
# read config file
##################
config = ConfigParser()
config.read("config.ini")

# read in all the config stuff actually used from the config file
title: str = config["blog"]["title"]
header: str = config["blog"]["header"]
header_text: str = config["blog"]["header_text"]
baseurl: str = config["blog"]["baseurl"]
default_post_title: str = config["blog"]["default_post_title"]
default_post_type: str = config["blog"]["default_post_type"]

# paths to content
path_md: Path = Path(config["paths"]["posts"])  # md posts
path_nb: Path = Path(config["paths"]["notebooks"])  # jupyter notebooks
path_static: Path = Path(config["paths"]["static"])  # static files
path_publish: Path = Path(config["paths"]["publish"])  # final output folder

#############################################
# configure python markdown parser
#############################################
# make enters into line breaks by adding "nl2br", add emoji extension
extensions = ["extra", "toc", "pymdownx.emoji"]  # , "smarty", "codehilite"

# https://help.farbox.com/pygments.html - consider monokai default themes
# noclasses: True puts all the styling in the html itself. False uses css styles
extension_configs = {
    "output_format": "html5",
    "pymdownx.emoji": {"emoji_generator": pymdownx.emoji.to_alt, "alt": "html_entity"},
    "codehilite": {"noclasses": False, "linenums": False, "pygments_style": "autumn"},
}
md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

######################
# setup Mako templates
######################
lookup = TemplateLookup(directories=["templates"])


def convert_notebooks_to_md():
    # emptying tmp so don't end up with old md files here
    shutil.rmtree("tmp", ignore_errors=True)

    # am I using nbconvert here?
    # exporter = nbconvert.MarkdownExporter()
    # write_file = nbconvert.writers.FilesWriter(build_directory="tmp")

    nb_paths = [
        f for f in path_nb.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(f)
    ]

    print(f"Converting {len(nb_paths)} notebooks to markdown files.")

    for nb_path in nb_paths:
        print(f"{nb_path}")
        # os.system(f"jupyter nbconvert --to markdown {nb_path} --output-dir tmp")
        # make folder for exported files
        make_folder(Path("tmp") / f"{nb_path.stem}_files")
        os.system(f"nbdev_nb2md --dest {Path('tmp')} --jekyll=True {nb_path}")

        # with open(nb_path) as f:
        #     nb_node = nbformat.read(f, as_version=4)

        # (body, resources) = exporter.from_notebook_node(nb_node)

        # write_file.write(
        #     output=body, resources=resources, notebook_name=nb_path.name[:-6]
        # )

    print(f"--------------------------\n")


def md_to_post(p: Path, post_type=default_post_type, debug=False):
    """takes in a path to md file  and returns a Post obj
    """

    try:
        all_txt = p.read_text()
    except:
        print(f"Failed to read {p}")

    # extract front matter b/w "---" lines
    n = all_txt[3:].find("---") + 3
    fm = yaml.load(all_txt[:n], Loader=yaml.FullLoader)  # front matter dict
    txt = all_txt[n + 3 :].strip()  # text excluding front matter

    title = fm.get("title", default_post_title)
    _post_type = fm.get("type", post_type)  # defaults to post
    slug = fm.get("slug", p.name.split(".")[0])  # todo: check repeated slugs
    dt = fm.get("date", datetime.fromtimestamp(p.stat().st_ctime).date())
    if debug:
        print(type(dt), title, dt)
    lastmod = fm.get("lastmod", datetime.fromtimestamp(p.stat().st_mtime).date())
    draft = fm.get("draft", False)

    tags = fm.get("tags", ["untagged"])

    html = md.convert(txt)

    # enable toc for posts if toc: True in front matter
    if (toc := fm.get("toc", False)) :
        toc = md.toc

    link = f"{tags[0]}/{slug}.html"

    post = Post(
        title=title,
        type=_post_type,
        slug=slug,
        link=link,
        path=p,
        tags=tags,
        date=dt,
        lastmod=lastmod,
        markdown=txt,
        draft=draft,
        toc=toc,
        html=html,
    )

    return post


def get_posts(debug=False):
    """reads from disk and returns a dataframe of all posts"""

    # convert notebooks to md and save in a tmp folder
    # convert_notebooks_to_md()

    # lists of md files and notebooks to convert
    md_paths = [f for f in path_md.rglob("*.md")]

    try:
        nb_paths = [f for f in Path("notebooks/markdown").rglob("*.md")]
    except:
        print("No md files converted from jupyter notebooks found in tmp dir")

    # decide whether to use dataframe or a dict to hold all the posts
    posts = []  # list holding all the posts
    postsdict = {}  # dict to hold all posts, using slug as the key
    tagsdict = defaultdict(set)  # holds set of all posts for every tag

    for p in md_paths:
        if debug:
            print(p)
        pp = md_to_post(p, debug=debug)
        posts.append(pp)

    for p in nb_paths:
        pp = md_to_post(p, post_type="notebook", debug=debug)
        if debug:
            print(type(pp.date), pp.title, pp.date)
        posts.append(pp)

    if debug:
        for post in posts:
            print(type(post.date), post.slug)

    posts.sort(key=lambda x: x.date, reverse=True)

    # create tagsdict
    for post in posts:
        for tag in post.tags:
            tagsdict[tag].add(post.slug)

    # create a dict of posts - to make it easier to lookup a certain post
    for post in posts:
        postsdict[post.slug] = post

    return posts, postsdict, tagsdict

    # misc stuff, fix this later

    df = pd.DataFrame(data)  # .set_index("filename")
    print(f"{len(df)} posts converted and saved in dataframe")

    # make the slug the index - hopefully they are all unique
    df = df.set_index("slug")
    # most recent at top
    df = df.sort_values(by="date", ascending=False)
    return df


def make_folder(path, debug: bool = False):
    """makes parent folders if they don't exist for a path"""

    # assume the last thing is a file if there is a dot in the name
    if "." in path.name:
        path = path.parent

    try:
        path.mkdir(parents=True, exist_ok=False)
        if debug:
            print(f"{path} folder made")
    except FileExistsError:
        if debug:
            print(f"{path} folder already exists")
        pass


def search_json(posts, path=path_publish):
    """makes a json of the posts info to search, returns json string
    and writes json file to disk"""

    search_list = [
        {"title": post.title, "tags": post.tags, "link": post.link} for post in posts
    ]

    posts_json = json.dumps(search_list)
    path = path / "posts.json"
    make_folder(path)

    path.write_text(posts_json)
    return posts_json


def write_posts(posts, tmpl: str = "post.html"):
    """makes a html page for each post using list of posts passed in
    
    Args:
        tmpl: name of templete
        posts: list of posts
    """

    template = lookup.get_template(tmpl)

    print(f"\nWriting html pages for {len(posts)} posts.")

    for post in posts:
        html = template.render(
            post=post, header=header, header_text=header_text
        ).strip()

        # publish each post inside its first tag folder
        if post.tags:
            path = path_publish / post.tags[0]
        else:
            path = path_publish

        make_folder(path)  # make folder in case

        # copy over post_files to the post folder.
        _path = path_nb / "markdown" / f"{post.slug}_files"
        if _path.is_dir():
            shutil.copytree(_path, path / f"{post.slug}_files", dirs_exist_ok=True)

        path = path / f"{post.slug}.html"

        path.write_text(html)
        print(f"wrote {post.slug} to {path}")


def write_index_page(posts, tags=None, tmpl: str = "index.html", foldername=None):
    """makes a html index page in the foldername using list of posts passed in
    
    Args:
        tmpl: name of templete
        foldername: name of folder to create
        posts: list of posts
    """

    template = lookup.get_template(tmpl)
    path = path_publish

    if foldername:
        path = path / foldername

    make_folder(path)  # make folder in case it doesn't exist

    # get json for fusejs search object
    # todo: modify js to read json from disk instead of passing obj
    postsjson = search_json(posts, path)

    html = template.render(
        posts=posts,
        tags=tags,
        title=title,
        postsjson=postsjson,
        header=header,
        header_text=header_text,
    ).strip()

    # write to disk
    path = path / tmpl
    path.write_text(html)
    print(f"wrote {tmpl} to {path}")


def write_tags(posts, tags):
    """writes an index.html file for each tag"""
    print(f"\nWriting an index page for {len(tags)} tags.")
    for tag in tags.keys():
        # filter posts
        tag_posts = [post for post in posts if tag in post.tags]
        # using the same index page for now
        write_index_page(foldername=tag, posts=tag_posts)


def write_all(posts: list, tags: dict):
    """this writes all the html pages to disk"""
    # posts, postsdict, tags = get_posts()
    write_index_page(posts=posts, tags=tags, foldername="")
    write_tags(posts=posts, tags=tags)
    write_posts(posts=posts)


def copy_static():
    """copies over the contents of the static folder to the public folder"""

    try:
        shutil.copytree(path_static, path_publish, dirs_exist_ok=True)
        print(f"copied contents of {path_static} over to {path_publish}")
    except:
        print("Failed to copy static files")

    # copy notebook files
    print(f"TODO: copied notebook files over to {path_publish}")


if __name__ == "__main__":
    # get posts
    posts, postsdict, tags = get_posts()
    # copy static files over to the publish dir
    copy_static()
    # write all the things to the publish dir
    write_all(posts, tags)

    # commit and push publish dir to gh-pages branch
    print("Website generated, now figure out how to publish it.")
