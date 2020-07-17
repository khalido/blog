---
title: "how the blog was built"
date: 2020-07-14
tags:
- python
toc: true
---

Hereby I talk through writing my own blog engine. There are many excellent ones out there, but to customize any of them takes so much understanding of how they work, the template and theme engines they use, that its easier to just use them exactly as is with an existing theme. I wanted my own custom static blog, and a reason to do some python coding, so here goes yet another python blogging script.

This post documents the process of building this blog. The main goal is to put markdown and jupyter notebooks in a folder, and build a static site which gets autoupdated on [github pages](https://pages.github.com/) or [netlify]https://www.netlify.com/). Just like [hugo](https://gohugo.io/), [jekyll](https://jekyllrb.com/), [gatsby](https://www.gatsbyjs.org/) and so many others!

## the basic blog

Listing todos...

- [ ] add emoji
- [ ] add tag pages

Its straightforward to read a set of markdown posts and convert to python. I am using python's [pathlib] library to read the posts and [python-markdown](https://python-markdown.github.io/) to parse them into html, complete with inline syntax highlighting.

### parsing markdown

Python markdown 

- https://python-markdown.github.io/extensions/
- https://facelessuser.github.io/pymdown-extensions/



Start a server

```bash
python -m http.server
```



### html

- [what to put in the head of a html page](https://github.com/joshbuchea/HEAD)
- https://htmldom.dev/

### css

Frameworks I looked at:

- [Pure.css](https://purecss.io/)
- [milligram](https://milligram.io/)
- [newcss](https://newcss.net/)
- [lit](https://ajusa.github.io/lit/docs/lit.html)
- [concrete.css](https://concrete.style/) - very minimal
- https://csslayout.io/ - examples of using css directly





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