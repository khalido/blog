the `templates` dir is the current working templates for this project. All the other folders are the templates archived at that date. 

I've kept them for prosperity in case I want for some godforsaken reason to build all the old templates of this site. 

# tailwindcss

To rebuild the tailwindcss file:

Install tailwindcss and [typography](https://github.com/tailwindlabs/tailwindcss-typography) in the templates folder:

`npm install -D tailwindcss@latest`
`npm install @tailwindcss/typography`

Check that `tailwinds.config.js` is pointing to the template html files and includes the typography plugin like so:

```js
purge: ["templates/*.html"],
plugins: [
    require('@tailwindcss/typography'),
  ],
  ```

Finally, create my custom css file based on my templates:

`npx tailwindcss -i templates/ko.css -o static/tailwind.css`

This will create a gigantic css file including all of tailwind and my custom css. This is way too big for actual usage, so once happy with how everything looks, create the final production css file:

`NODE_ENV=production npx tailwindcss -i templates/ko.css -o static/tailwind.css`

Also consider adding the flag `--minify` to further compress the production css if needed.


## template changelog:

Aug 2020: Whereupon I decided css is too hard and would just use tailwindcss instead.

June 2020: The original version where I just wanted to see how templates worked. These used a simple framework. 