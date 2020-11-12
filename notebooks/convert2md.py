"""
python script to convert jupyter notebooks to markdown files using ndbev
"""

import os
from pathlib import Path
from nbdev.export2html import convert_md

path_nb: Path = Path(".")  # convert notebook is in the notebooks folder
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


nb_paths = [f for f in path_nb.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(f)]

print(f"Converting {len(nb_paths)} notebooks to markdown files.")

for nb_path in nb_paths:
    print(f"converting {nb_path}")
    path_img = path_md / f"{nb_path.stem}_files"
    make_folder(path_img)  # make _files folder inside markdown output folder
    convert_md(nb_path, dest_path=path_md, img_path=None, jekyll=True)
    # remove extra empty files folder made by nbdev
    Path(path_img.stem).rmdir()

