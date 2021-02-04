---
title: Windows 10
date: 2020-10-28
tags:
- windows
---

## Factory reset

Windows 10 gets slow and crufty over time. So once every few years, its good to start afresh. 

[Reset](https://support.microsoft.com/en-us/surface/restore-or-reset-surface-for-windows-10-e1fd649a-6396-a7de-2e87-7ba3b45e0fb1) by:

- `Start -> Settings -> Update & Security -> Recovery -> Reset this PC`

OR, if windows is pretty borked, restart the surface and hold the `shift` key down. This should boot into a screen with a: `Troubleshoot -> Reset this PC`.



## Setup

install [scoop](https://scoop.sh/) by running this in powershell:

```
iwr -useb get.scoop.sh | iex
scoop bucket add extras
```

- [Rufus](https://rufus.ie/) for making bootable disks. [etcher](https://www.balena.io/etcher/) is a decent alternative, but not as reliable.
