---
title: Windows 10
date: 2020-10-28
tags:
- windows
---

# Windows 10

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

## wsl 2

Follow [the real wsl instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10), my clif notes are:

Run powershell as admin and do:

Activate wsl by `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`

Enable "virtual machine platform", something which should have already been enabled by the command above.

`Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart`

Restart the pc now and set wsl2 as the default wsl: `wsl --set-default-version 2`

Now install the latest [linux kernel update package](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi).

Now install debian from the windows store.
