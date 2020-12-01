---
title: "MacOS"
description: "setup notes for osx"
date: 2020-01-20
tags:
- mac
---

# Install the latest macOS

If starting with a old mac, I recommend doing a factory reset and installing the latest macos.

Power on the mac and keep holding down `Option/Alt + Command + R` until a spinning globe appears. This boots you into recovery mode and offers to reinstall the latest version of OSX, which for me is [10.15: Catalina](https://www.apple.com/au/macos/catalina/).

I had to format the disk before installing as the installer wasn't recognizing it. The eraser defaulted to the old MAC disk format, change that to `AFPS` with scheme `GUID Partition Map`. I'm used to case insensitive systems on linux, but on MacOS some apps don't like that, so regular AFPS seems to be the best option. 

Also see:

- [Apple reset page](https://support.apple.com/en-au/HT204904) and [recovery page](https://support.apple.com/en-au/HT201314).


# Interface tweaks


## manual tweaks

- autohide the dock: Its just a waste of space. No one should be looking or clicking on the dock anyways.
- Don't press, tap! System Preferences > Trackpad > Tap to click
- [three finger drag](https://support.apple.com/en-za/HT204609) is awesome. 
Accessibility -> Mouse & Trackpad -> Options -> Enable dragging (choose 3 finger drag) 

## Finder

New finder window open in home dir.




# App setup

## homebrew aka easy install apps

[homebrew](https://brew.sh/) installs all the packages.

Install it by pasting this in a terminal: 

- `sudo xcode-select --install` - this installs the xcode cli 
- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` downloads and installs brew.

Most cli tools are installed by: `brew install wget` and gui apps by: ` brew cask install firefox`.

Other useful commands:

- `brew update` updates brew itself and all the packages it can install
- `brew upgrade` upgrades all packages installed by homebrew

## cli apps

- [neofetch]() displays nifty info about your system in the terminal. Don't install this using brew as that installs way too much stuff.

```
brew install curl 
```

## essential apps

- [Rectangle](https://github.com/rxhanson/Rectangle) window manager, cause life is too short to use a mouse to resize windows.
- [itsycal] adds a small dropdown calendar to the menubar
- [Karabiner Elements](https://karabiner-elements.pqrs.org/) to modify keyboard shortcuts, in particular make the capslock key into a super key which can launch alred.
- [Alfred]() is a super duper launcher for macos. I remap capslock to launching it. 
- [Visual Studio code]() is my cross-platform editor of choice. its awesome.
- [slack]() gotta talk to all the work colleages
- [spotify]() gotten listen to music
- [zoom](https://zoom.us/) - video chat service of choice in 2020, even for companies paying tons of money to other companies for video calls!  

This installs them all in one fell swoop.

```
brew cask install \
    rectangle \
    itsycal \
    karabiner-elements \
    alfred \
    google-chrome \
    visual-studio-code \
    slack \
    spotify \
    zoomus
```

## A better app launcher

[Alred](https://www.alfredapp.com/) replaces spotlight.


# Dev setup

Install a nicer terminal: `brew cask install iterm2` cause why not.

update git cause the macos version is old: `brew install git` and do the basic git setup:

```
git config --global user.name "khalido"
git config --global user.email "myname@gmail.com"
git config --global color.ui auto
```

Install neofetch cause its looks nice to see your system stats in a terminal: `brew install neofetch`


# links

- [setup mac for dev](https://github.com/nicolashery/mac-dev-setup)
- [another setup](https://mac.iamdeveloper.com/posts/my-mac-setup-2m05/)