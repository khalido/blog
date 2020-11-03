---
title: "how the blog was built"
date: 2020-09-14
tags:
- python
toc: true
---

Hereby I talk through writing my own blog engine. There are many excellent ones out there, but to customize any of them takes so much understanding of how they work, the template and theme engines they use, that its easier to just use them exactly as is with an existing theme. I wanted my own custom static blog, and a reason to do some python coding, so here goes yet another python blogging script.

This post documents the process of building this blog. The main goal is to put markdown and jupyter notebooks in a folder, and build a static site which gets autoupdated on [github pages](https://pages.github.com/) or [netlify]https://www.netlify.com/). Just like [hugo](https://gohugo.io/), [jekyll](https://jekyllrb.com/), [gatsby](https://www.gatsbyjs.org/) and so many others!

## the basic blog

Its straightforward to read a set of markdown posts and convert to python. I am using python to read the posts with [python-markdown](https://python-markdown.github.io/) to parse them into html, complete with inline syntax highlighting.

Key tools used:

- **write:** markdown docs using any editor and jupyter notebooks having yaml front matter
- **make the blog:** 
  - [nbconvert] to parse jupyter to markdown [python markdown] to parse markdown to html
  - python to read all the markdown files using [python markdown](https://python-markdown.github.io/) and [yaml](https://pyyaml.org/wiki/PyYAMLDocumentation) make html pages for index, tags and posts using [mako](https://www.makotemplates.org/) for python friendly templates
- **search:** [fusejs](https://fusejs.io/) to make a in browser search engine
- every time a post is added or updated, the whole site needs to be rebuilt and redeployed. 
  - **build site:** every time I commit to my blog repo, a github action is triggered which rebuilds the sites and saves the output to a `_site` folder.
  - **hosting:** the site is hosted on the gh-pages of my blog repository, which github pages auto republishes on every time. I am using a [github action](https://github.com/peaceiris/actions-gh-pages) to deploy output files from the `_site` folder to gh-pages on every commit to the main branch.

### parsing markdown

Python markdown 

- https://python-markdown.github.io/extensions/
- https://facelessuser.github.io/pymdown-extensions/



Start a server

```bash
python -m http.server
```



### code highlight

python markdown has pygments built in, which has a bunch of styles. To generate the css:

```bash
pygmentize -S default -f html -a .codehilite > codestyles.css
```

The 



### html

- [what to put in the head of a html page](https://github.com/joshbuchea/HEAD)
- https://htmldom.dev/

### css

Frameworks I looked at:

- [https://tachyons.io/](https://tachyons.io/) 
- [https://tailwindcss.com/](https://tailwindcss.com/)
- [Pure.css](https://purecss.io/)
- [water.css](https://github.com/kognise/water.css)
- [milligram](https://milligram.io/)
- [newcss](https://newcss.net/)
- [lit](https://ajusa.github.io/lit/docs/lit.html)
- [concrete.css](https://concrete.style/) - very minimal
- https://csslayout.io/ - examples of using css directly

### Search

Search. I want search. 

Considered at

- [fusejs](https://fusejs.io/) - [blog post implementing this in hugo](https://gist.github.com/cmod/5410eae147e4318164258742dd053993#staticjsfastsearchjs)
- [minisearch](https://lucaong.github.io/minisearch/)
- consider lunr as well as [lunr.py](https://github.com/yeraydiazdiaz/lunr.py) to pre generate the index.

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