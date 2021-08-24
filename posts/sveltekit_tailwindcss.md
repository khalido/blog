---
title: "Sveltekit with Tailwindcss"
description: "building an interactive website"
date: 2021-08-24
tags:
- web
---

# Sveltekit with TailwindCSS

I wanted to setup a simple interactive website, and [react](https://reactjs.org/) is so 2019 and verbose, so I [looked around](https://news.ycombinator.com/item?id=26693959) and svelte looked awesome, especially the [tutorial](https://svelte.dev/tutorial/basics) which is a work of art.

[Svelte](https://svelte.dev/) is a JS framework which puts html, css and javascript inside a .svelte file. It aims to stick mostly to basic html/css/js, so is easier to use than the more complicated frameworks like react which essentially are their own language. A good [intro video](https://youtu.be/qSfdtmcZ4d0).

Each .svelte file can be thought of as a component, and you use them like lego to build an app. A very basic svelte file is just js, html and css - try it out in the [svelte repl](https://svelte.dev/repl). A sample component (i.e a svelte file to be reused elsewhere) looks like:

```html
<!-- saved as nested.svelte -->
<script>
	export let a_variable = "you can pass in your own value!";
</script>

<h2>nested h2</h2>

<p>This is a 1em paragraph, orange in nature, with this passed in beauty: <strong>{a_variable}</strong>.</p>

<style>
  p {color: orange; font-size: 1em;}
	h2 {color: teal; font-size:1.5em;}
</style>
```

The main entry point would be called `App.svelte` and will have javascript, html and css like so:

```html
<!-- svelte is mostly 100% javascript -->
<script>
	import Nested from './nested.svelte';
  let name = "KO";
  let img = "https://media.giphy.com/media/xT8qBsOjMOcdeGJIU8/giphy.gif?cid=ecf05e47oh5ia150hx4lkfrlccxgcucgqpxksgkroeru7x4p&rid=giphy.gif&ct=g"
</script>

<!-- content goes here, curly brackets are javascript -->
<h1>Hello {name.toUpperCase()}!</h1>
<p>we be coding</p>

<!-- import and use a component -->
<Nested/>

<!-- we can pass in values to the component, even computed ones -->
<Nested a_variable={21*2}/> 

<img src={img} alt="alt text">

<!-- css goes here, scoped only to this file -->
<style>
  h1 {color: purple}
</style>
```

While it’s possible to build an entire app inside a single .svelte file, we’re better off with making multiple components each doing one thing and import them as needed, as in the example above.

Thats the basics of svelte! Its actually pretty straightforward. For simple apps, this is all you need, but for more complex apps you need a router, which is where sveltekit comes in.

## Sveltekit

[Sveltekit](https://kit.svelte.dev/) is a framework for svelte which transforms svelte files into a static or interactive web app.

### Pages (or routes)

Sveltekit uses a file based router, which is fancy speak for saying it looks at the folder `src/routes` and turns every svelte file into a page.  The entry point of the app is of course `src/routes/index.svelte`.

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

Css has become so complex that using it directly is akin to programming in C. So there are a ton of css frameworks which do the heavy lifting. But all of them require separating the content (html) from design (css), and going back and forth can be a pain.

Tailwind provides a ton of helper styles to use directly inside html. This makes it easier to just modify things  directly all in one file. This made sense to me with svelte as that puts content, code and style all in the one svelte file anyways.

To see more about tailwindcss, see this earlier blog post.


## Setting up all the things

This is the complex part. So I’m laying it out here step by step for my future self.

To see this in action, here's the [github repo for this starter project](https://github.com/khalido/sveltekit-starter) and the [final, super simple output site](https://sveltekit-starter-lemon.vercel.app).

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

The install script asks for options, I choose:

- Template: Skeleton project
- Use Typescript: No
- Use ESlint: No
- Add Prettier: Yes

This will have installed and configured sveltekit and tailwindcss. To run:

```bash
npm run dev -- --open
```

Optionally, add the [tailwind typography plugin](https://github.com/tailwindlabs/tailwindcss-typography): 

```bash
npm install -D @tailwindcss/typography
```

and update the plugins section in `tailwind.config.js` to include this:

```
plugins: [
		require('@tailwindcss/typography'),
	],
```

Then start the site: `npm run dev -- --open`. Presto! A svelte site powered by sveltekit and tailwindcss should be up and running.  Go to `src/routes` and open `index.html` and copy paste this below whats already there:

```html
<article class="prose px-8 py-4 bg-gray-200">
	<h1>Welcome to SvelteKit</h1>
	<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
</article>
```

If the above chunk is styled, and updates in the browser preview, then everything is setup fine and working. 

##  Deploying

Time to setup an adaptor to publish this to the web. Initially I tried [adaptor-static](https://github.com/sveltejs/kit/tree/master/packages/adapter-static) to deploy to github pages, but kept running into errors. Now the simplest thing is to build the static site locally, and use github pages to deploy the already built site, but this requires a working local dev env for any changes and thats so last year.

So I went with [the vercel adaptor](https://github.com/sveltejs/kit/tree/master/packages/adapter-vercel) - this worked pretty painlessly out of the box, since essentially there is no local build step - you just run a local dev server: `npm run dev -- --open` and push to github once done.

### Vercel 

The exciting part about [using vercel to deploy](https://vercel.com/docs/build-step#framework-preset) is how easy it is:

> Vercel detects the following frontend frameworks automatically and chooses the best default settings for you.

Install the adaptor:

```bash
npm install -D @sveltejs/adapter-vercel@next
```

Update `svelte.config.js` so it has the vercel adapter line:

```js
    kit: {
    adapter: vercel(),
    }
```

Then go to vercel, start a [new project](https://vercel.com/new) and point it to the [repo for this starter project](https://github.com/khalido/sveltekit-starter). The default settings should just work - it should build and publish the site, and auto-rebuild and publish on every git push.

The final output: [https://sveltekit-starter-lemon.vercel.app](https://sveltekit-starter-lemon.vercel.app).

## To look  at later

- [storybookjs](https://storybook.js.org/blog/storybook-for-svelte/) - create components
- [daisyui](https://daisyui.com/) - components for tailwind
- [Svelte summit 2021](https://youtu.be/fnr9XWvjJHw)
