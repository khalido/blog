---
date: 2021-01-02
tags:
  - python
toc: true
---

# Using Anaconda

Testing heading parsing here.

## Install Anaconda

There seems to be two main ways to handle python packaging, pip with pipenv and conda. I've gone with conda, though it turns out I often have to use pip inside conda. Anyways, [there is a cheatsheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf), but here's all I use:

- download and install [anaconda from here](https://www.anaconda.com/download).
- restart terminal and check anaconda is in the path by `ECHO $SHELL`

If its not in the path then:

- on mac, add `export PATH="/anaconda3/bin:$PATH"` at the top of `.zshrc` if using zsh, on bash it should have automatically added that to `.bash_profile`, add if not present.

And python + jupyter lab + a bunch of other packages should be up and running!

## Using environments

Protip: install pip inside a conda enviroment if planning to ever use pip install. Otherwise pip installs inside an environment use the main pip and that is NOT GOOD.

So here we create a new environment which will use Python 3.9x and pip.

`conda create -n py39 python=3.9 pip`

Use this environment:

`conda activate py39`

And a few basic commands:

- `conda list` - shows all packages installed in the active env

Shows all conda envs:

`conda env list`

Delete an environment:

`conda env remove -n py39 --all`

### Write the packages in use to disk:

This will include both the conda and pip installed packeges in an environment, long as pip was installed inside the environment.

`conda list --explicit > py39.txt`

Now if I git clone this repo somewhere else, I can recreate the environment by:

`conda env create --file py39.txt`

## Jupyter lab

Jupyter lab is the new hotness and is ready to rock out of the box with anaconda. to make it easy to select from all the environments installed, in the main anaconda env (i.e not inside an env) run:

`conda install nb_conda`

This should ideally let the conda env with jupyter lab see all the other kernels.

Anaconda itself has an older version of jupyter lab, so lately I have take to installing it the updated version directly in a conda env:

`conda install -c conda-forge jupyterlab`
