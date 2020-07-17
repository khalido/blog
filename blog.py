"""Converts markdown files and jupyter notebooks in a directory to html files

This file:
- gets config values from config.ini file
- reads all markdown files in a folder, parses front matter, saves info in a Posts dataclass
- returns a  sorted dict of Posts and a dict of tags: post_slugs 


"""

# libs built into python
import os
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
import pandas as pd  # no real need to use this so rethink later
from mako.template import Template
from mako.lookup import TemplateLookup

# from tqdm.auto import tqdm
from datetime import datetime
import markdown
import nbconvert


@dataclass
class Post:
    """class to store each individual posts data"""

    title: str
    slug: str
    link: str
    path: Path
    tags: List[str]
    markdown: str
    html: str
    date: datetime
    lastmod: datetime
    toc: Optional[str]
    showtoc: bool = False
    draft: bool = False


# read config file
config = ConfigParser()
config.read("config.ini")

# read in all the config stuff actually used from the config file
# path to where all the files are stored
path_md = Path(config["blog"]["posts"])

# this folder contains all the html/css/images to be published
path_publish = Path(config["blog"]["publish"])

# baseurl = config["blog"]["baseurl"]

# configure python markdown parser
# make enters into line breaks by adding "nl2br"
extensions = ["extra", "toc", "codehilite"]  # , "smarty"

# https://help.farbox.com/pygments.html - consider monokai default themes
# noclasses: True puts all the styling in the html itself. False adds css styles
extension_configs = {
    "codehilite": {"noclasses": True, "linenums": False, "pygments_style": "monokai"},
}

md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)

# setup Mako templates
lookup = TemplateLookup(directories=["templates"])


def get_posts(debug=False):
    """reads from disk and returns a dataframe of all posts"""

    # lists of md files and notebooks to convert
    md_paths = [f for f in path_md.rglob("*.md")]
    # notebook_paths = [f for f in path.rglob("*.ipynb")]

    # decide whether to use dataframe or a dict to hold all the posts
    posts = []  # list holding all the posts
    postsdict = {}  # dict to hold all posts, using slug as the key
    tagsdict = defaultdict(set)  # holds set of all posts for every tag

    for p in md_paths:

        all_txt = p.read_text()

        # extract front matter b/w "---" lines
        n = all_txt[3:].find("---") + 3
        fm = yaml.load(all_txt[:n], Loader=yaml.FullLoader)  # front matter dict
        txt = all_txt[n + 3 :].strip()  # text excluding front matter
        if debug:
            print(fm)

        # using slug as the url and unique id for each post
        # so consider some logic to make sure slugs aren't repeated
        if fm.get("slug"):
            slug = fm["slug"]
        else:
            slug = p.name.split(".")[0]

        # add created date
        if "date" in fm:
            dt = fm["date"]
        else:
            dt = datetime.fromtimestamp(p.stat().st_ctime).date()  # file createtime

        # add last modified data
        if "lastmod" in fm:
            lastmod = fm["lastmod"]
        else:
            lastmod = datetime.fromtimestamp(p.stat().st_mtime).date()

        if "draft" in fm:
            draft = fm["draft"]
        else:
            draft = False

        # tags
        if "tags" in fm:
            tags = fm["tags"]
            for tag in tags:
                tagsdict[tag].add(slug)
        else:
            tags = ["untagged"]
            tagsdict["untagged"].add(slug)

        html = md.convert(txt)

        toc = False  # default to not showing toc
        if "toc" in fm:
            if fm["toc"] is True:
                toc = md.toc

        link = f"{tags[0]}/{slug}.html"

        pp = Post(
            title=fm["title"],
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

        # data.append(post)
        posts.append(pp)

    posts.sort(key=lambda x: x.date, reverse=True)

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
    and writes to disk"""

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

    print(f"\nWriting post page for {len(posts)} posts.")

    for post in posts:
        html = template.render(post=post).strip()

        # publish each post inside its first tag folder
        if post.tags:
            path = path_publish / post.tags[0]
        else:
            path = path_publish

        make_folder(path)  # make folder in case

        path = path / f"{post.slug}.html"

        path.write_text(html)
        print(f"wrote {post.slug} to {path}")


def write_index_page(posts, tmpl: str = "index.html", foldername=None):
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

    html = template.render(posts=posts, postsjson=postsjson).strip()

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
    write_index_page(posts=posts, foldername="")
    write_tags(posts=posts, tags=tags)
    write_posts(posts=posts)


if __name__ == "__main__":
    posts, postsdict, tags = get_posts()
    write_all(posts, tags)
