---
date: 2022-01-02
tags:
  - python
toc: true
---

There are many ways to use python, I've gone with mamba as the environment manager for now.

# Using Anaconda/Mambaforge

Instead of using the full Anaconda install, I've switched to [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge). The key differences are:

* mamaba is a faster better version of conda
* it installs a minimal install without the tons of packages present in the default anaconda install, and defaults to the `conda-forge` channel.

See the [Mamba docs](https://mamba.readthedocs.io/en/latest/index.html) for more info.

## Install Mamba

Install the latest version of mambaforge on linux/mac :

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"
bash Mambaforge-$(uname)-$(uname -m).sh
```


## Using environments

So here we create a new environment which will use Python 3.11.

`conda create -n py311 python=3.11`

This installs pip by default, which is a great as some packages I use are only available on pip. 

The basic commands:

* Activate the env: `mamba activate py311`
- Show installed packages: `mamba list`
	- search for a specific package: `mamba list | grep pandas` 
- Show all conda envs: `mamba env list`
- Remove an environment: `remove env remove -n py310 --all`

Install packages from a file:

```bash
mamba install --file requirements.txt
```

### Write the packages in use to disk:

This will include both the conda and pip installed packeges in an environment, long as pip was installed inside the environment.

`mamba list --explicit > py.txt`

Now if I git clone this repo somewhere else, I can recreate the environment by:

`mamba env create --file py.txt`

## Jupyter lab

These days I'm using the VS code jupyter notebook hotness, but just in case:

`mamba install jupyterlab`
