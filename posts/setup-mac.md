---
title: "MacOS"
description: "setup notes for osx"
date: 2020-01-20
tags:
- mac
---

## Install the latest macOS

If starting with a old mac, I recommend doing a factory reset and installing the latest macos.

Power on the mac and keep holding down `Option/Alt + Command + R` until a spinning globe appears. This boots you into recovery mode and offers to reinstall the latest version of OSX, which for me is [Big Sur](https://www.apple.com/au/macos/big-sur/).

I had to format the disk before installing as the installer wasn't recognizing it. The eraser defaulted to the old MAC disk format, change that to `AFPS` with scheme `GUID Partition Map`. 

Also see:

- [Apple reset page](https://support.apple.com/en-au/HT204904) and [recovery page](https://support.apple.com/en-au/HT201314).


## Interface tweaks


### manual tweaks

- autohide the dock: Its just a waste of space. No one should be looking or clicking on the dock anyways.
- Don't press, tap! System Preferences > Trackpad > Tap to click
- [three finger drag](https://support.apple.com/en-za/HT204609) is awesome. 
Accessibility -> Mouse & Trackpad -> Options -> Enable dragging (choose 3 finger drag) 

### Finder

New finder window open in home dir.


## App setup

#### homebrew aka easy install apps

[homebrew](https://brew.sh/) installs all the packages.

Install it by pasting this in a terminal: 

- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` downloads and installs xcode cli tools and brew.

Most cli tools are installed by: `brew install wget` and gui apps by: ` brew cask install firefox`.

Other useful commands:

- `brew update` updates brew itself and all the packages it can install
- `brew upgrade` upgrades all packages installed by homebrew


## essential apps

- [Rectangle](https://github.com/rxhanson/Rectangle) window manager, cause life is too short to use a mouse to resize windows.
- [Karabiner Elements](https://karabiner-elements.pqrs.org/) to modify keyboard shortcuts, in particular make the capslock key into a super key which can launch alred.
- [Alfred](https://www.alfredapp.com/) is a super duper launcher for macos. I remap capslock to launching it. Even though spotlight is getting better, alfred is faster and more configurable.
- [Visual Studio code](https://code.visualstudio.com/) is my cross-platform editor of choice. its awesome.
- [slack]() gotta talk to all the work colleages
- [spotify](https://www.spotify.com) gotten listen to music
- [zoom](https://zoom.us/) - video chat service of choice in 2021, even for companies paying tons of money to other companies for video calls!  

This installs them all in one fell swoop.

```
brew install --cask \
    rectangle \
    karabiner-elements \
    alfred \
    google-chrome \
    visual-studio-code \
    slack \
    spotify \
    zoomus
```



## Dev setup

Big sur has python installed, but I prefer [Anaconda](https://khalido.org/python/anaconda.html).

```bash
git config --global user.name "khalido"
git config --global user.email "myname@gmail.com"
#git config --global color.ui auto
```

### terminal setup

[ohmyzsh](https://github.com/ohmyzsh/ohmyzsh): jazz up the shell.

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

This zapped the conda settings for me, so fix those by:

```bash
source /Users/ko/anaconda3//bin/activate
conda init zsh 
```

### cli apps

- [neofetch](https://github.com/dylanaraps/neofetch) displays nifty info about your system in the terminal. Don't install this using brew as that installs way too much stuff.
- [bat](https://github.com/sharkdp/bat) - heaps better cat replacemet.

```
brew install \
    neofetch \
    bat
```

# links

- [setup mac for dev](https://github.com/nicolashery/mac-dev-setup)
- [another setup](https://mac.iamdeveloper.com/posts/my-mac-setup-2m05/)