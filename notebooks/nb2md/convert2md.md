---
title: Jupyter notebooks to markdown
description: using nbdev to convert notebooks to markdown
date: 2020-11-10
toc: true
tags:
- python
---

This is very meta, but since I only update notebooks once in a while, this here notebook converts all the notebooks in the folder to markdown files and images, which are used to build the blog posts on the site.

The main reason to do this is to save time when rebuilding the blog on github pages, as installing nbdev and converting all the notebooks takes a while.

Later on could add an option to the config to either build notebooks on each build or to just read the converted markdown files.



```python
#collapse-hide
import os
from pathlib import Path
from nbdev.export2html import convert_md
import yaml

import khalido as ko # my helper utils
```

helper functions follow:


```python
#collapse-hide
path_nb: Path = Path(".") # convert notebook is in the notebooks folder
path_md = path_nb / "markdown"

def make_folder(path, debug: bool = False):
    """makes parent folders if they don't exist for a path"""

    # assume the last thing is a file if there is a dot in the name
    if "." in path.name:
        path = path.parent

    try:
        path.mkdir(parents=True, exist_ok=False)
        if debug:
            print(f"{path} folder made")
    except FileExistsError:
        if debug:
            print(f"{path} folder already exists")
        pass
```

## nbdev

NBdev comes with a number of helpful extra features, so first up using that:


```python
nb_paths = [
        f for f in path_nb.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(f)
    ]

print(f"Converting {len(nb_paths)} notebooks to markdown files.")

for i, nb_path in enumerate(nb_paths):
    print(f"{i:3}: converting {nb_path}")
    path_img = path_md / f"{nb_path.stem}_files"
    make_folder(path_img) # make _files folder inside markdown output folder
    convert_md(nb_path, dest_path=path_md, img_path=None, jekyll=True)
    # remove extra empty files folder made by nbdev
    Path(path_img.stem).rmdir()
```

    Converting 11 notebooks to markdown files.
      0: converting flood_fill.ipynb



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-7-ba477e698daf> in <module>
          9     path_img = path_md / f"{nb_path.stem}_files"
         10     make_folder(path_img) # make _files folder inside markdown output folder
    ---> 11     convert_md(nb_path, dest_path=path_md, img_path=None, jekyll=True)
         12     # remove extra empty files folder made by nbdev
         13     Path(path_img.stem).rmdir()


    ~/anaconda3/envs/blog/lib/python3.8/site-packages/nbdev/export2html.py in convert_md(fname, dest_path, img_path, jekyll)
        570     fname = Path(fname).absolute()
        571     dest_name = fname.with_suffix('.md').name
    --> 572     exp = nbdev_exporter(cls=MarkdownExporter, template_file='jekyll-md.tpl' if jekyll else 'md.tpl')
        573     export = exp.from_notebook_node(nb, resources=meta_jekyll)
        574     md = export[0]


    ~/anaconda3/envs/blog/lib/python3.8/site-packages/nbdev/export2html.py in nbdev_exporter(cls, template_file)
        486     exporter.anchor_link_text = ' '
        487     exporter.template_file = 'jekyll.tpl' if template_file is None else template_file
    --> 488     exporter.template_path.append(str(Path(__file__).parent/'templates'))
        489     return exporter
        490 


    AttributeError: 'MarkdownExporter' object has no attribute 'template_path'


So now in the markdown output folder we have a list of `.md` files, with each file having a `_files` folder containing output artifacts for that notebook.


```python
os.listdir(path_md)
```




    ['monte_carlo_pi_files',
     'monty_hall.md',
     'flood_fill_files',
     'us_elections_2020_files',
     'convert2md.md',
     'Advent-of-Code-2015_files',
     'Advent-of-Code-2015.md',
     'knn_files',
     'quicksort_files',
     'blogging_with_jupyter_notebooks.md',
     'blogging_with_jupyter_notebooks_files',
     'knn.md',
     'monte_carlo_pi.md',
     'convert2md_files',
     'flood_fill.md',
     'us_elections_2020.md',
     'quicksort.md',
     'monty_hall_files']



## nbconvert

Nbconvert is usually pre-installed with jupyter notebook, so testing that out as well:


```python
import nbformat
from nbconvert import MarkdownExporter
```


```python
nb_paths = [
        f for f in path_nb.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(f)
    ]

for nb_path in nb_paths:
    try:
        os.system(f'jupyter nbconvert --to markdown {nb_path} --output-dir markdown')
    except:
        print(f"failed to convert {nb_path}")
    
    print(f"converted {nb_path}")
    
```

    converted flood_fill.ipynb
    converted knn.ipynb
    converted blogging_with_jupyter_notebooks.ipynb
    converted Advent-of-Code-2015.ipynb
    converted monty_hall.ipynb
    converted pinboard.ipynb
    converted advent-of-code-2020.ipynb
    converted quicksort.ipynb
    converted convert2md.ipynb
    converted monte_carlo_pi.ipynb



```python
md_exporter = MarkdownExporter(config=c)
```


```python
resources["outputs"].keys()
```




    dict_keys(['output_3_0.png', 'output_7_0.png', 'output_7_1.png', 'output_7_2.png', 'output_7_3.png', 'output_7_4.png', 'output_7_5.png', 'output_7_6.png', 'output_7_7.png', 'output_7_8.png', 'output_7_9.png', 'output_7_10.png'])




```python
from IPython.display import Image
Image(data=resources['outputs']['output_3_0.png'], format='png')
```




    
![png](convert2md_files/convert2md_14_0.png)
    




```python
from traitlets.config import Config
c = Config()
#c.HTMLExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']
c.MarkdownExporter.preprocessors = ['nbconvert.preprocessors.ExtractOutputPreprocessor']

```


```python

```


```python

```
