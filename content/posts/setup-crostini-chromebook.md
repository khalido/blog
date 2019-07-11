---
title: "Setting up Linux on a Chromebook with Crostini"
date: 2018-08-24
tags:
- chromebooks
---

ChromeOS supports a built in Linux - running inside a container running insde a VM. Turn it on by going to settings and pressing the on button for Linux (beta). This gives us a bare bones Linux install running Debian Stretch. So here goes all the things I did to customize it.

Most of these tips are from the [reddit crostini wiki](https://www.reddit.com/r/Crostini/wiki/index), I've put all the ones I'm using in one page for a handy reference.

- [Install all the apps](#install-all-the-apps)
  - [add backports to apt install recent packages](#add-backports-to-apt-install-recent-packages)
  - [updating debian to testing](#updating-debian-to-testing)
  - [vs code](#vs-code)
  - [markdown app](#markdown-app)
- [install anaconda for a better python](#install-anaconda-for-a-better-python)
  - [jupyter lab](#jupyter-lab)
- [make the terminal nicer to use](#make-the-terminal-nicer-to-use)
  - [fix window shortcuts](#fix-window-shortcuts)
  - [multiplex all the things](#multiplex-all-the-things)
  - [jazz up the shell](#jazz-up-the-shell)
  - [setup vim proper like](#setup-vim-proper-like)
- [Download all my git repos](#download-all-my-git-repos)

## Install all the apps

### add backports to apt install recent packages

Now, there are many ways to do this, but the easiest and nicest is to sudo apt all-the-things. But, this is Google, so not only do you have to do this insided a container in a virtual machine inside some some weird linux/chrome melting pot, you get old software. so first up, update the container itself:

the default crostini container/vm whatever is running debian stretch, which is nice and stable, but has a lot of old packages in its repo. To keep things simple, just add backports. Backports is a repo which contains newer packages from debian testing and unstable.

Update `source.list` by running `sudo vim /etc/apt/sources.list` and add at the bottom:

```
# Backports repository
deb http://deb.debian.org/debian stretch-backports main contrib non-free
```

by default apt will pull packages from stretch itself, so to install something from backports:

`sudo apt -t stretch-backports install "package"`

the line `-t stretch-backports` above is telling apt to target stretch-backports,

### updating debian to testing

**hold the upgrade to testing, turns out Google is really aiming at stretch so updating to testing breaks things like the file integration with chromeos and who knows what else.**

change `sources.list` so it reads (comment out any other lines by putting # at the start):

`deb http://deb.debian.org/debian stretch testing contrib non-free`

Update the information from the new repos and then upgrade: `sudo apt update && sudo apt upgrade`

### vs code

Anaconda can automatically install VS Code, but to [install it directly](https://www.reddit.com/r/Crostini/wiki/howto/install-vscode):

```bash
curl -L https://go.microsoft.com/fwlink/?LinkID=760868 > vscode.deb
sudo apt install ./vscode.deb
```
Useful plugins:

- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### markdown app

 Currently I'm using [Caret](http://thomaswilburn.net/caret/) - a chromeos text editor app which runs lightening fast.

vs code can handle markdown nicely, but I find it too slow on Crostini. I prefer [Typora.io](https://typora.io/) or [Caret.io](http://caret.io/) for markdown and vs code is for coding. BUT all these apps are based on electron, and currently run slow on Crostini, and will continue being slow until Crostini gets GPU accleration.

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

Only do this if you already know why you are doing this, else you don't need to.

go to the [Anaconda linux download page](https://www.anaconda.com/download/#linux) and copy the url, then download it:

`curl -O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh` # (update url)

Install by `bash Anaconda3-5.2.0-Linux-x86_64.sh` # change filename to whatever the downloaded file name is.

### jupyter lab

Now I use anaconda to run jupyter, so to make that run properly, generate a default config file:

`jupyter notebook --generate-config`

and at the top add:

```
c.NotebookApp.allow_origin = '*' # allow all origins
c.NotebookApp.ip = '*' # listen on all IPs
```

now running `jupyter lab` starts the jupyter server in the current directory and opens up a tab in chromeos.

Other useful stuff for Jupyter:

To install [extensions](https://github.com/mauhai/awesome-jupyterlab), first install nodejs:

`conda install -c conda-forge nodejs`

useful jupyter extensions:

- show a [toc](https://github.com/jupyterlab/jupyterlab-toc) from markdown headings: `jupyter labextension install @jupyterlab/toc`

todo: try out [nteract](https://nteract.io/) - a react based desktop front end for jupyter.


## make the terminal nicer to use

this is really important, cause if the terminal doesn't look like something out of a movie, are you really terminalining?

### fix window shortcuts

First up, the terminal gobbles up some of my fav chromeos shortcuts, namely:

- Maximize `Alt + =`
- Minimize `Alt + -`
- Dock window left/right `Alt + [`, `Alt + ]`
- Close window `Ctrl+Shift+W` - this is actually `Ctrl-W` normally, but terminal might need that hence shift.

fix this by pressing `ctrl-shift-p` inside terminal, then scroll down to keyboard preferences and enter

```bash
{
  "Alt-187": "PASS",
  "Alt-189": "PASS",
  "Alt-219": "PASS",
  "Alt-221": "PASS",
  "Ctrl-Shift-W": "PASS"
}
```

This has to be done only once, since ChromeOS remembers the terminal settings across devices. So handy after a powerwash.

### multiplex all the things

install tmux, the internets fav terminal multiplexer:

`sudo apt -t stretch-backports install tmux`

the only thing I really do with tmux is to split the terminal horizontally, then splitting one horizontal terminal vertically, for a total of three windows. Now there is a lot more about sessions and whats not, but the bare basics are:

start tmux by typing `tmux`, then press `ctrl+b` to enter command mode. `"` splits the window horizontally and `%` splits it vertically. To move around, press `ctrl-b arrow-key`


For more customizatoin, make a `.tmux.conf` in the home directory and add:

```bash
# Enable mouse mode (tmux 2.1 and above)
set -g mouse on
```

### jazz up the shell

rumour has it that crostini can have a heart attack if you change the shell, so stick with bash. Consider [oh-my-bash](https://github.com/ohmybash/oh-my-bash) or [bash-it](https://github.com/ohmybash/oh-my-bash) for hacker level coding.

also install [powerline-fonts](https://github.com/powerline/fonts) and select a powerline font for the terminal. 

`sudo apt -t stretch-backports install fonts-powerline`

Useful shell tools: 

[tldr](https://github.com/tldr-pages/tldr-python-client) shows a short and useful help page for commands, e.g type `tldr curl` to get a synopsis of how to use curl. 
`pip install tldr` on chromeos.

[bat](https://github.com/sharkdp/bat) a replacement for cat, displays files with syntax highlighting in the terminal. Right now as rendering problems in crostini, but hopefully will improve. Install by downloading the .deb and `sudo apt install ./bat_file.deb`.


### setup vim proper like

install plugin manager for vim - I went with [vim-plug](https://github.com/junegunn/vim-plug):

edit `~/.vimrc` so it has this stuff:

```bash
" install vim-plug if not installed
if empty(glob('~/.vim/autoload/plug.vim'))
  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

" plugin directory, don't use standard Vim names like 'plugin'
call plug#begin('~/.vim/plugged')

" plugins go here
" ---------------
" highlights code problems: https://github.com/w0rp/ale
Plug 'w0rp/ale'
" adds a status bar: https://github.com/itchyny/lightline.vim
Plug 'itchyny/lightline.vim'
" distraction free writing: https://github.com/junegunn/goyo.vim
Plug 'junegunn/goyo.vim'
" for python auto completion: https://github.com/davidhalter/jedi-vim
Plug 'davidhalter/jedi-vim'

" Initialize plugin system
call plug#end()

" don't break mid word
set linebreak

```

run `:PlugInstall` in vim to install plugs (if needed).

## Download all my git repos

This command will grab json output of the first (or last) 200 repos in my github and git clone them all one by one into the directory this command was run.

```bash
curl -s https://api.github.com/users/khalido/repos?per_page=200 | grep \"clone_url\" | awk '{print $2}' | sed -e 's/"//g' -e 's/,//g' | xargs -n1 git clone
```