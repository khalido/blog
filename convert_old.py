import os
import re
import fileinput
import sys
from glob import glob

# Create path to content
path = 'content/'

# Find all jupyter notebooks in all content folders
all_ipynb_files = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                       for name in files
                           if name.endswith((".ipynb"))]

# Remove all notebooks from checkpoint folders
ipynb_files = [ x for x in all_ipynb_files if ".ipynb_checkpoints" not in x ]

for notebook in ipynb_files:
    os.system(f'jupyter nbconvert --to markdown {notebook}')

for f in ipynb_files:
    print(f, f[:-6])
    print(f"{f[:-6]}.md")

# fix image links in generated markdown files
# code from https://github.com/chrisalbon/notes/blob/master/make.ipynb

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

# Find all markdown files in all content folders
all_md_files = [os.path.join(root, name)
               for root, dirs, files in os.walk(path)
               for name in files
               if name.endswith((".md"))]

for file in all_md_files:
    with open(file,'r') as f:
        filedata = f.read()
        # Find all markdown link syntaxes
        md_links = re.findall('!\\[[^\\]]+\\]\\([^)]+\\)', filedata)

        # For each markdown link
        for link in md_links:
            # Replace the full file path
            md_image_path = re.search(r'\((.*?)\)', link).group(1)
            md_image_filename = os.path.basename(md_image_path)
            md_image_title = re.search(r'\[(.*?)\]', link).group(1)

            new_link = "!["+md_image_title+"]("+md_image_filename+")"

            replaceAll(file, link, new_link)