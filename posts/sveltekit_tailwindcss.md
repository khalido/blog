---
title: "Sveltekit with Tailwindcss"
description: "building an interactive website"
date: 2021-07-29
tags:
- web
---

# Sveltekit with TailwindCSS

I wanted to setup a simple interactive website, and [react](https://reactjs.org/) is so 2019 and verbose, so I [looked around](https://news.ycombinator.com/item?id=26693959) and svelte looked awesome, especially the [tutorial](https://svelte.dev/tutorial/basics) which is a work of art.

[Svelte](https://svelte.dev/) is a JS framework which puts html, css and javascript inside a .svelte file. It aims to stick mostly to basic html/css/js, so is easier to use than the more complicated frameworks like react which essentially are their own language. A good [intro video](https://youtu.be/qSfdtmcZ4d0).

Each .svelte file can be thought of as a component, and you use them like lego to build an app. Svelte files can contain javascript, html and css like so:

```html
// javascript goes here
<script>
  let name = "KO";
  let img = "testpic.gif"
</script>

// content goes here, curly brackets are javascript
<h1>Hello {name.toUpperCase()}!</h1>
<img src={img} alt="alt text">

// css goes here, scoped only to this file
<style>
  h1 {color: purple}
</style>
```

While it’s possible to build an entire app inside a single .svelte file, we’re better off with making multiple components each doing one thing and import them as needed.

First, make a basic component containing just a para, and save it as `nested.svelte`.

```html
<p>This is another paragraph.</p>
```
Then another svelte file can import and use it:

```html
<script>
  import Nested from './nested.svelte';
</script>

<p>This is a paragraph.</p>

// runs whatever is inside the nested.svelte file
<Nested/> 
```

Note: svelte uses capitalcase for component names to not confuse them with html tags.

and thats the basics of svelte! Its actually pretty straightforward.

## Sveltekit

[Sveltekit](https://kit.svelte.dev/) is a framework for svelte which transforms svelte files into a static or interactive web app.

### Pages (or routes)

Svelte kit looks at the folder `src/routes` and turns every svelte file into a page.  The entry point of the app is of course `src/routes/index.svelte`.

So, `src/routes/about.svelte` becomes the `/about` page, or alternatively, if the about page contains other files and stuff, we can put all in a sub directory: `src/routes/about/index.svelte`.

### Layouts

i.e shared components, like a header visible on each page. This file applies to ever page: `src/routes/__layout.svelte`. Layouts can be nested, so subfolders can contain a `__layout.svelte` file which only applies to the pages in that subfolder.

Put `__layout.reset.svelte` in any subfolder where you don’t want the pages to inherit layouts.

### sveltekit targets

Sveltekit sites can run on node server, or be pre-rendered to to run on any web server as static web pages. The following two adapters seem production ready:

- [adaptor-static](https://github.com/sveltejs/kit/tree/master/packages/adapter-static) - static site, suitable for github pages or anywhere really
- [adapter-vercel](https://github.com/sveltejs/kit/tree/master/packages/adapter-vercel) - dynamic server rendering

These two are listed as experimental, so ignoring for now:

- [adapter-netlify](https://github.com/sveltejs/kit/tree/master/packages/adapter-netlify) - dynamic server renering
- [adapter-cloudflare-workers](https://github.com/sveltejs/kit/tree/master/packages/adapter-cloudflare-workers) - suitable for sites needing dynamic server rendering

## Tailwindcss

Css is so complex that using it directly is akin to programming in C. So there are a ton of css frameworks which do the heavy lifting. But all of them require separating the content (html) from design (css), and going back and forth can be a pain.

Tailwind provides a ton of helper styles to use directly inside html. This makes it easier to just modify things  directly all in one file. This made sense to me with svelte as that puts content, code and style all in the one svelte file  anyways.

### icons, styled with css, oh my!

[tailwind has made svg icons](https://heroicons.com) which can be styled with css directly.

```
<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
</svg>
```

## Setting up all the things

This is the complex part. So I’m laying it out here step by step for my future self.

1. install node using brew (mac) or [nvm](https://github.com/nvm-sh/nvm) (cross platform, probably better) or [fnm](https://github.com/Schniz/fnm).
2. install VS code and these extensions:
    1. [svelte vs code](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode)
    2. [tailwindcss](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss) 

Note: tailwindcss wasn't auto-completing so I had to update this vscode setting:

```json
"editor.quickSuggestions": {
  "strings": true
}
```

### Install svelte and tailwind

```bash
npm init svelte@next myapp
cd myappp
npx svelte-add tailwindcss --jit
npm install
```

This will have installed and configured sveltekit and tailwindcss. To run:

```bash
npm run dev -- --open
```

Optionally, add the [tailwind typography plugin](https://github.com/tailwindlabs/tailwindcss-typography): `npm install @tailwindcss/typography` and update the plugins section in `tailwind.config.js` to include this:

```
plugins: [
		require('@tailwindcss/typography'),
	],
```

Now adding the prose class to any html will style it nicely, though ideally you still need a `div` class around everything to set margins for the page.

```html
<article class="prose lg:prose-xl">
    <h1>some heading</h1>
    <p>some text.... </p>
</article>
```

A good starting container - the outside div colours everything, and the inside pads and centers.

```html
<div class="bg-yellow-100"> 
<div
	class="px-4 py-10 max-w-3xl mx-auto sm:px-6 sm:py-12 lg:max-w-4xl lg:py-16 lg:px-8 xl:max-w-6xl bg-gray-50"
>
    <!-- content goes here -->
</div></div>
```

I've put up all this in a github repo: __TODO__


## To look  at later

- https://storybook.js.org/blog/storybook-for-svelte/
