import os

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

print(f"Converted {len(ipynb_files)} jupter notebooks to markdown.")