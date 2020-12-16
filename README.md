Herin lies a mixed up blog, notes, reviews, recepies, whatever else I might want to possible refer back to in the future.

Posts use yaml, each post should have something like this at the top:

```
---
title: "how the blog was built"
date: 2020-20-14
tags:
- python
toc: true
---
```

The title becomes the h1 heading for the post, so use only h2 or `##` levels in the actual post.

to use the script:

- `python blog.py` builds site, saves html output to public dir.
- `python blog.py --serve` builds site and starts a [local server](http://localhost:8001/) at port 8001. 
- `python blog.py --cache` builds sites and uses the last notebook to markdown conversion.

If working on the scipt, use `python blog.py -c -s`, this skips reading and converting jupyter notebooks, which is very slow, both on my local machine and when running on github.

## Content

Mardown files are processed from the `posts` directory, and jupyter notebooks from the `notebooks` directory. This makes it easy to treat them differently. 

At some point I probably need a pages directory too. At which point I might as well have a contents folder with posts, notebooks, pages, etc.

## Config stuff

- `config.ini` file specifies blog title and header, and paths to content and output.
- `static` folder content is copied over to the public folder for serving, so this contains css, images etc.
- `templates` folder contains the templates, currently written in mako.

### todo

- [ ] convert notebooks to markdown manually, since those are only updated infrequently. Should save a lot of time in the github build action.
- [ ] store post images in the posts folder itself? Have a think. Whats the easiest way to insert images in a markdown post?