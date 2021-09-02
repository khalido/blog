![Blog built and deployed](https://github.com/khalido/blog/actions/workflows/build.yml/badge.svg)

Blog content + a simple python blogging engine

- the python code
    - `bloggy` python code which converts content to html
    - `templates` folder contains the templates, currently written in mako.
- the content
    - `posts` markdown posts
    - `notebooks` jupyter notebooks
    - `static` images, css, js etc used to serve the site, copied as is to the final output folder.
- output
    - `public` the final html output which gets published to github pages

Herin lies a mixed up blog, notes, reviews, recepies, whatever else I might want to possible refer back to in the future.

Posts use yaml, each post should have something like this at the top:

```
---
date: 2020-20-14
tags:
- python
---
```

to use the script:

- `python -m bloggy` builds site, saves html output to public dir.
- `python -m bloggy --serve` builds site and starts a [local server](http://localhost:8001/) at port 8000. 
- `python -m bloggy --buildnotebooks` also converts jupyter notebook to markdown, by default skips as this is a slow process with even a few notebooks. Currently I run this once in awhile, the output is saved to `notebooks/nb2md` folder and sync'd to github. I don't update notebooks often so this is good enough. 

## Content

Markdown files are processed from the `posts` directory, and jupyter notebooks from the `notebooks` directory. This makes it easy to treat them differently. 

At some point I probably need a pages directory too. At which point I might as well have a contents folder with posts, notebooks, pages, etc.

## Config stuff

- `config.ini` file specifies blog title and header, and paths to content and output.

### todo

- [ ] figure out how to use alpinejs for some interactivityu
- [ ] convert notebooks to markdown manually, since those are only updated infrequently. Should save a lot of time in the github build action.
- [ ] only convert jupyter notebooks if they have been changed since the last conversion or the output file doesn't exist.
- [ ] store post images in the posts folder itself? Have a think. Whats the easiest way to insert images in a markdown post?
- [ ] Fix the lastmod issue, since github clones over the folder the file datestamp becomes the clone time instead of the last time the file was changed. Probably just ignore this, and only do a lastmod if set in the frontmatter.
- [ ] Fix the local server so it rebuilds the blog on changes. Threading or async should do this? One thread to run the server the other to watch the posts folder. Use a delay as Vscode says files every few miliseconds.

## Shoutouts

- [fastpages](https://github.com/fastai/fastpages), in particular their [notebook template](https://github.com/fastai/fastpages/blob/master/_action_files/hide.tpl)