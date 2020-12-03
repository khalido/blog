Herin lies a mixed up blog, notes, reviews, recepies, whatever else I might want to possible refer back to in the future.

Posts use yaml, each post should have something like this at the top:

```
---
title: "how the blog was built"
date: 2020-07-14
tags:
- python
toc: true
---
```

The title becomes the h1 heading for the post.

Mardown files are processed from the `posts` directory, and jupyter notebooks from the `notebooks` directory. This makes it easy to treat them differently. 

### todo

- [ ] convert notebooks to markdown manually, since those are only updated infrequently. Should save a lot of time in the github build action.