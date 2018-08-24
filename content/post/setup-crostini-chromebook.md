---
title: "Setting up Linux on a Chromebook with Crostini"
date: 2018-08-24
tags:
- chromebooks
---

ChromeOS supports a built in Linux - running inside a container running insde a VM. Turn it on by going to settings and pressing the on button for Linux (beta). This gives us a bare bones Linux install running Debian Stretch. So here goes all the things I did to customize it.

Most of these tips are from the [reddit crostini wiki](https://www.reddit.com/r/Crostini/wiki/index), I've put all the ones I'm using in one page for a handy reference.

## install many softwares

Now, there are many ways to do this, but the easiest and nicest is to sudo apt all-the-things. But, this is Google, so not only do you have to do this insided a container in a virtual machine inside some some weird linux/chrome melting pot, you get old software. so first up, update the container itself:

### add backports

the default crostini container/vm whatever is running debian stretch, which is nice and stable, but has a lot of old packages in its repo. To keep things simple, just add backports. Backports is a repo which contains newer packages from debian testing and unstable.

Update `source.list` by running `sudo vim /etc/apt/sources.list` and add at the bottom:

```
# Backports repository
deb http://deb.debian.org/debian stretch-backports main contrib non-free
```

by default apt will pull packages from stretch itself, so to install something from backports:

`sudo apt -t stretch-backports install "package"`

the line `-t stretch-backports` above is telling apt to target stretch-backports,

#### updating debian to testing

**hold the upgrade to testing, turns out Google is really aiming at stretch so updating to testing breaks things like the file integration with chromeos and who knows what else.**

change `sources.list` so it reads (comment out any other lines by putting # at the start):

`deb http://deb.debian.org/debian stretch testing contrib non-free`

Update the information from the new repos and then upgrade: `sudo apt update && sudo apt upgrade`

### install anaconda

Only do this if you already know why you are doing this, else you don't need to.

go to the [Anaconda linux download page](https://www.anaconda.com/download/#linux) and copy the url, then download it:

`curl -O https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh` # (update url)

Install by `bash Anaconda3-5.2.0-Linux-x86_64.sh` # change filename to whatever the downloaded file name is.

Now I use anaconda to run jupyter, so to make that run properly, generate a default config file:

`jupyter notebook --generate-config`

and at the top add:

```
c.NotebookApp.allow_origin = '*' # allow all origins
c.NotebookApp.ip = '*' # listen on all IPs
```

now running `jupyter lab` starts the jupyter server in the current directory and opens up a tab in chromeos.

todo: try out [nteract](https://nteract.io/) - a react based desktop front end for jupyter.

### vs code

edit all the things by [installing vs code](https://www.reddit.com/r/Crostini/wiki/howto/install-vscode):

```
curl -L https://go.microsoft.com/fwlink/?LinkID=760868 > vscode.deb
sudo apt install ./vscode.deb
```

### edit markdown

vs code can handle markdown nicely, but I found it a bit slow after adding markdown plugins. Caret is nicer for markdown, vs code is better for coding:

[caret](http://caret.io/) is my fav markdown editor. install it by downloading the [latest beta release .deb](https://github.com/careteditor/releases-beta/releases) and:

`sudo apt install ./caret-beta.deb`

## make the terminal nicer to use

this is really important, cause if the terminal doesn't look like something out of a movie, are you really terminalining?

### fix window shortcuts

First up, the terminal gobbles up some of my fav chromeos shortcuts, namely:

- Maximize `Alt + =`
- Minimize `Alt + -`
- Dock window left/right `Alt + [`, `Alt + ]`
- Close window `Ctrl+Shift+W` - this is actually `Ctrl-W` normally, but terminal might need that hence shift.

fix this by pressing `ctrl-shift-p` inside terminal, then scroll down to keyboard preferences and enter

```
{
  "Alt-187": "PASS",
  "Alt-189": "PASS",
  "Alt-219": "PASS",
  "Alt-221": "PASS",
  "Ctrl-Shift-W": "PASS"
}
```

### multiplex all the things

install tmux, the internets fav terminal multiplexer:

`sudo apt -t stretch-backports install tmux`

the only thing I really do with tmux is to split the terminal horizontally, then splitting one horizontal terminal vertically, for a total of three windows. Now there is a lot more about sessions and whats not, but the bare basics are:

start tmux by typing `tmux`, then press `ctrl+b` to enter command mode. `"` splits the window horizontally and `%` splits it vertically. To move around, press `ctrl-b arrow-key`


For more customizatoin, make a `tmux.conf` in the home directory and add:

```
# Enable mouse mode (tmux 2.1 and above)
set -g mouse on

# split panes using | and -
bind | split-window -h
bind - split-window -v
unbind '"'
unbind %
```

### jazz up the shell

rumour has it that crostini can have a heart attack if you change the shell, so stick with bash. Consider [oh-my-bash](https://github.com/ohmybash/oh-my-bash) or [bash-it](https://github.com/ohmybash/oh-my-bash) for hacker level coding