---
title: "MacOS"
description: "setup notes for osx"
date: 2021-07-26
tags:
- mac
---

# MacOS

If  a new mac, just copy paste the script below and go, otherwise consider a re-install if on a crusty handmedown.

## Do the setup

copy paste this line into terminal on any mac big sur or newer and it will setup and install almost all the things:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/khalido/dotfiles/master/setup_mac.sh)"
```

And thats it! After a restart it should be ready to go. The  [setup script](https://github.com/khalido/dotfiles/blob/master/setup_mac.sh) is pretty self explanatory.

The only thing I left out was python, which I'm installing through [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) if necessary.

## Install the latest macOS (if needed)

If starting with an old mac, I recommend doing a factory reset and installing the latest macOS.

Power on the mac and keep holding down `Option/Alt + Command + R` until a spinning globe appears. This boots you into recovery mode and offers to reinstall the latest version of OSX, which for me is [Big Sur](https://www.apple.com/au/macos/big-sur/), with [Monterey](https://www.macrumors.com/roundup/macos-12/) dropping in late '21.

I had to format the disk before installing as the installer wasn't recognizing it. The eraser defaulted to the old MAC disk format, change that to `AFPS` with scheme `GUID Partition Map`. 

Also see:

- [Apple reset page](https://support.apple.com/en-au/HT204904) and [recovery page](https://support.apple.com/en-au/HT201314).

## old stuff below

Older notes below, no longer needed as the setup file does all this.

### manual tweaks

- autohide the dock: Its just a waste of space. No one should be looking or clicking on the dock anyways.
- Don't press, tap! System Preferences > Trackpad > Tap to click
- [three finger drag](https://support.apple.com/en-za/HT204609) is awesome. 
Accessibility -> Mouse & Trackpad -> Options -> Enable dragging (choose 3 finger drag) 

## App setup

#### homebrew aka easy install apps

[homebrew](https://brew.sh/) installs all the packages.

Install it by pasting this in a terminal: 

- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` downloads and installs xcode cli tools and brew.

## essential apps

- [Karabiner Elements](https://karabiner-elements.pqrs.org/) to modify keyboard shortcuts, in particular make the capslock key into a super key which can launch alred.
- [Raycast](https://raycast.com/) is a super duper launcher for macos. I remapped capslock to launch it. Even though spotlight is getting better, raycast is faster and lots more configurable.
- [Visual Studio code](https://code.visualstudio.com/) is my cross-platform editor of choice. its awesome.
- [Microsoft Teams](https://www.microsoft.com/en-au/microsoft-teams/group-chat-software) gotta talk to all the work people.
- [Spotify](https://www.spotify.com) gotten listen to music
- [Zoom](https://zoom.us/) - video chat service of choice in 2021, even for companies paying tons of money to other companies for video calls!  

My script above installs them all in one go.



# links

- [setup mac for dev](https://github.com/nicolashery/mac-dev-setup)
- [another setup](https://mac.iamdeveloper.com/posts/my-mac-setup-2m05/)