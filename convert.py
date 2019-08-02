import os
import re
import sys
import fileinput

# path to jupyter notebooks 
path = 'content/'

# Find all jupyter notebooks in the content folder (and its subfolders)
all_ipynb_files = [os.path.join(root, name)
                   for root, dirs, files in os.walk(path)
                       for name in files
                           if name.endswith((".ipynb"))]

# Remove all notebooks from checkpoint folders
ipynb_files = [x for x in all_ipynb_files if ".ipynb_checkpoints" not in x]

# converting to markdown, one at a time
for notebook in ipynb_files:
    os.system(f'jupyter nbconvert --to markdown {notebook}')

# now to fix image links in the generated markdown files
# code mostly from https://github.com/chrisalbon/notes/blob/master/make.ipynb

def replaceAll(file,searchExp,replaceExp):
    """func to replace text in a file"""
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

# the markdown files are in the same place as the jupyter notebooks
# this ensures I don't rewrite links in my regular markdown posts
all_md_files = [f"{f[:-6]}.md" for f in ipynb_files]

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
            #print(link, new_link)

            replaceAll(file, link, new_link)


print(f"Converted {len(ipynb_files)} jupter notebooks to markdown.")