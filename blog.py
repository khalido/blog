"""Converts markdown files and jupyter notebooks in a directory to html files

This file:
- gets config values from config.ini file
- reads all markdown files in a folder, parses front matter, saves info in a Posts dataclass
- returns a  sorted dict of Posts and a dict of tags: post_slugs 


"""

# libs built into python
import os
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

# from tqdm.auto import tqdm
from datetime import datetime
import markdown
import nbconvert


@dataclass
class Post:
    """class to store each individual posts data"""

    title: str
    slug: str
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
path = Path(config["blog"]["content"])

# this folder contains all the html/css/images to be published
publish = Path(config["blog"]["publish"])

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


def get_posts(debug=False):
    """reads from disk and returns a dataframe of all posts"""

    # lists of md files and notebooks to convert
    md_paths = [f for f in path.rglob("*.md")]
    # notebook_paths = [f for f in path.rglob("*.ipynb")]

    # decide whether to use dataframe or a dict to hold all the posts
    posts = []  # list holding all the posts
    postsdict = {}  # dict to hold all posts, using slug as the key
    tagsdict = defaultdict(set)  # holds set of all posts for every tag

    for p in md_paths:

        all_txt = p.read_text()

        # extract front matter b/w "---" lines
        n = all_txt[3:].find("---") + 3
        fm = yaml.load(all_txt[:n])  # front matter dict
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

        pp = Post(
            title=fm["title"],
            slug=slug,
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

    df = pd.DataFrame(data)  # .set_index("filename")
    print(f"{len(df)} posts converted and saved in dataframe")

    # make the slug the index - hopefully they are all unique
    df = df.set_index("slug")
    # most recent at top
    df = df.sort_values(by="date", ascending=False)
    return df

def write():
    """this writes all the html pages to disk"""
    posts, postsdict, tags = get_posts()
    
    # write index page


    # write tag pages
    for t in tags.keys():
        for s in sorted(tags[t], key = lambda x: postsdict[x].date, reverse=True):
            print(postsdict[s].slug, postsdict[s].date)
        print("---------------")