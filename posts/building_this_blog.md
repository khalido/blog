---
title: "how the blog was built"
date: 2020-11-11
tags:
- python
toc: true
---

There are many excellent blog engines out there, but to customise any of them takes so much understanding of how they work, the template and theme engines they use, that its easier to just use them exactly as is with an existing theme. 

I wanted my own custom static blog, which played well with jupyter notebooks and markdown files, as well as a reason to do some python coding, so here goes yet another python blogging engine.

This post documents the process of building this blog. The main goal is to put markdown and jupyter notebooks in a folder, and build a static site which gets autoupdated on [github pages](https://pages.github.com/) or [netlify](https://www.netlify.com/). Just like [hugo](https://gohugo.io/), [jekyll](https://jekyllrb.com/), [gatsby](https://www.gatsbyjs.org/) and so many others!

## blog engine

Its straightforward to read a set of markdown posts and convert to python. I am using python to read the posts with [python-markdown](https://python-markdown.github.io/) to parse them into html, complete with inline syntax highlighting.

Key tools used:

* *write:** markdown docs using any editor and jupyter notebooks having yaml front matter.
	* [obsidian](https://obsidian.md/) to edit markdown
	* [vs code](https://code.visualstudio.com/docs/python/jupyter-support) for jupyter notebooks. Jupyter lab is ok in a pinch but it causes me more problems than not. My fav cloud alternative is [Deepnote](https://deepnote.com/).
- **make the blog:** 
  -  [nbconvert](https://nbconvert.readthedocs.io/en/latest/)  to parse jupyter to markdown.
    - tried [nbdev](https://github.com/fastai/nbdev) but had too many problems, though it has a lot more blog friendly features.
  - python to read all the markdown files using [python markdown](https://python-markdown.github.io/) and [yaml](https://pyyaml.org/wiki/PyYAMLDocumentation). 
  - finally, writing html pages for index, tags and posts using [mako](https://www.makotemplates.org/) for python friendly templates.
- **search:** [fusejs](https://fusejs.io/) to make a in browser search engine
- every time a post is added or updated, the whole site needs to be rebuilt and redeployed. 
  - **build site:** every time I commit to my blog repo, a github action is triggered which rebuilds the sites and saves the output to a `public` folder.
  - **hosting:** the site is hosted on the gh-pages of my blog repository, which github pages auto republishes. I am using a [github action](https://github.com/peaceiris/actions-gh-pages) to deploy output files from the `public` folder to gh-pages on every commit to the main branch.
- **local sever**: running the script with `--serve` flag starts a local python server.

Below are notes for the specifics used.

### parsing markdown

Python markdown 

- https://python-markdown.github.io/extensions/
- https://facelessuser.github.io/pymdown-extensions/

Start a server from cli:

```bash
python -m http.server
```

### notebooks to markdown

I started with nbdev to convert notebooks to markdown, but it slowed down rebuilding the blog a lot, and its pretty complex. So in the end I've stuck with nbconvert. Some useful tips:

- [specify templates](https://stackoverflow.com/questions/64127278/what-is-the-proper-way-to-specify-a-custom-template-path-for-jupyter-nbconvert-v)

I need to customize nbconvert so it implements some of the features from [fastpages](https://github.com/fastai/fastpages), namely:

* renders output differently
* collapses code cells if #hide is at the top


### code highlight

python markdown has pygments built in, which has a bunch of styles. To generate the css:

```bash
pygmentize -S default -f html -a .codehilite > codestyles.css
```

But on second thought decided to can this and go with [highlightjs](https://highlightjs.org/) for now as it speeds up builds and keeps the html clean (at the cost of loading more javascript). 

One thing to investigate is how to make the output cells of jupyter notebooks blend into the main website. This seems to require some css trickery.

### html

I'm no longer familiar with html, even though I build my first weblog on geocities way back in 1997/8. So we have now reached html5.

- [what to put in the head of a html page](https://github.com/joshbuchea/HEAD)
- https://htmldom.dev/

### css

CSS is hard. So I want a simple to use framework, ended up looking at:

- [https://tachyons.io/](https://tachyons.io/) 
- [https://tailwindcss](https://tailwindcss.com/) - at first sight it looked horrible, with style mixed in with html, but once I thought about it some more, its beautiful. Everything is there visible in the one file and I hate css files anyways. So leaning towards using this, the only downside being is that you need npm to generate the final production tailwind css file. More to follow once I actually implement it...
- [Pure.css](https://purecss.io/)
- [water.css](https://github.com/kognise/water.css)
- [milligram](https://milligram.io/)
- [newcss](https://newcss.net/) - awesome, simple, super easy to use - basically just write html and it it makes it look nice and clean. Best for simple things like this blog. Only reason to switch to a more complex css file is cause even simple posts like this need small text and slide-outs for post meta-data like tags and date info etc.
- [lit](https://ajusa.github.io/lit/docs/lit.html)
- [concrete.css](https://concrete.style/) - very minimal
- https://csslayout.io/ - examples of using css directly

todo: decide on one. 

### Search

Search. I want search.  This is pretty straightforward, we need a list of content and some javascript to do the searching.

To just search post titles is pretty easy, from direct js to algolias [autocomplete library](https://github.com/algolia/autocomplete).

Ideally I want to search across all the content is well, which takes some thinking as the output of jupyter notebooks can be huge, with all kinds of js embedded.

Some things to look at:

- [fusejs](https://fusejs.io/) - [blog post implementing this in hugo](https://gist.github.com/cmod/5410eae147e4318164258742dd053993#staticjsfastsearchjs) - used this first. It works and is pretty straightforward but has no python integration and I would like better examples as a js newbie.
- [minisearch](https://lucaong.github.io/minisearch/)
- [lunr.js](https://lunrjs.com/) as well as [lunr.py](https://github.com/yeraydiazdiaz/lunr.py) to pre generate the index.

So step one is to build a search index - which my script does as a json file containing all the post attributes I want searched.

### Github actions

Github actions add superpowers to a repo - they can be set to be triggered at a time interval or on every code push to a branch. To make a github action: Save a github approved formatted yaml file to `.github/workflows` folder and it should run on every push. For this blog my actions:

- copys the contents of the repo to the github runner
- sets up python - [python versions available on github actions](https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json)
- install dependencies as defined in requirements.txt



## Misc stuff

### emoji

Some unicode fonts have emojis built in, so ways to enable emoji is:

- use a unicode font and investigate python-markdown emoji parser to deal with them properly
- use a script to replace `:smile:` with emoji incons - nope, don't want images scattered all over the shop.

Emoji test:

- smiley face test copy pasted from some website: 😅
- smiley face written using markdown code `:smile:`​ :smile: 
  - dang, this works in the markdown editor but not in the browser

### twitter embed

This should show a twitter tweet embedded inside the page:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sunsets don&#39;t get much better than this one over <a href="https://twitter.com/GrandTetonNPS?ref_src=twsrc%5Etfw">@GrandTetonNPS</a>. <a href="https://twitter.com/hashtag/nature?src=hash&amp;ref_src=twsrc%5Etfw">#nature</a> <a href="https://twitter.com/hashtag/sunset?src=hash&amp;ref_src=twsrc%5Etfw">#sunset</a> <a href="http://t.co/YuKy2rcjyU">pic.twitter.com/YuKy2rcjyU</a></p>&mdash; US Department of the Interior (@Interior) <a href="https://twitter.com/Interior/status/463440424141459456?ref_src=twsrc%5Etfw">May 5, 2014</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

### testing syntax highlight

```python
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=["templates"])

# make the big picture templates
for tmpl in ["index.html"]:
    template = lookup.get_template(tmpl)
    html = template.render(posts=posts).strip()
    path = path_publish / tmpl
    path.write_text(html)
    print(f"wrote {tmpl} to {path}")

# write all the posts
template = lookup.get_template("post.html")
for post in posts:
    html = template.render(post=post).strip()
    path = path_publish / f"{post.slug}.html"
    path.write_text(html)
    print(f"wrote {post.slug} to {path}")
```