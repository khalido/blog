---
title: "Setup Linux"
description: "setup notes for debian/ubuntu"
date: 2018-09-20
tags:
- linux
---

# Linux setup

# Evnironment

todo

# Apps 


## vs code


```bash
curl -L https://go.microsoft.com/fwlink/?LinkID=760868 > vscode.deb
sudo apt install ./vscode.deb
```

Useful plugins:

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## markdown app

 Currently I'm using [Caret](http://thomaswilburn.net/caret/) - a chromeos text editor app which runs lightening fast.

vs code can handle markdown nicely, but it be slow. I prefer [Typora.io](https://typora.io/) or [Caret.io](http://caret.io/) for markdown and vs code is for coding. BUT all these apps are based on electron.

Install Caret by downloading the [latest beta release .deb](https://github.com/careteditor/releases-beta/releases) and:

`sudo apt install ./caret-beta.deb`

Install Typora - haven't tested this out, especially adding repo. Apparently you have to `sudo apt install software-properties-common` first before adding a repo.


```bash
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io/linux ./'
sudo apt update

# install typora
sudo apt install typora
```

## install anaconda for a better python

See 

## nodejs

Step 1: install [nvm](https://github.com/nvm-sh/nvm#install--update-script), a script to install nodejs

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash`

step 2: install nodejs itself by:

`nvm install node`


## make the terminal nicer to use

this is really important, cause if the terminal doesn't look like something out of a movie, are you really doing something?

I'm using [Tilix](https://gnunn1.github.io/tilix-web/), install by

`sudo apt -t stretch-backports install tilix`


### multiplex all the things

If using Tilix, no need to do this, but for the native terminal, install tmux:

`sudo apt -t stretch-backports install tmux`

the only thing I really do with tmux is to split the terminal horizontally, then splitting one horizontal terminal vertically, for a total of three windows. Now there is a lot more about sessions and whats not, but the bare basics are:

start tmux by typing `tmux`, then press `ctrl+b` to enter command mode. `"` splits the window horizontally and `%` splits it vertically. To move around, press `ctrl-b arrow-key`

For more customizatoin, make a `.tmux.conf` in the home directory and add:

```bash
# Enable mouse mode (tmux 2.1 and above)
set -g mouse on
```

### jazz up the shell

Consider [oh-my-bash](https://github.com/ohmybash/oh-my-bash) or [bash-it](https://github.com/ohmybash/oh-my-bash) for hacker level coding.

also install [powerline-fonts](https://github.com/powerline/fonts) and select a powerline font for the terminal.

`sudo apt -t stretch-backports install fonts-powerline`

Useful shell tools:

[tldr](https://tldr.sh) shows a short and useful help page for commands, e.g type `tldr curl` to get a synopsis of how to use curl.

- Preferred install: `npm install -g tldr`
- If node not installed: `pip install tldr`

[bat](https://github.com/sharkdp/bat) a replacement for cat, displays files with syntax highlighting in the terminal. Install by downloading the .deb and `sudo apt install ./bat_file.deb`.


## Download all my git repos

This command will grab json output of the first (or last?) 200 repos in my github and git clone them all one by one into the directory this command was run.

```bash
curl -s https://api.github.com/users/khalido/repos?per_page=200 | grep \"clone_url\" | awk '{print $2}' | sed -e 's/"//g' -e 's/,//g' | xargs -n1 git clone
```