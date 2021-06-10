---
title: Lilygo ttgo t5 
date: 2021-01-18
toc: true
tags:
- iot
---

# Lilygo ttgo t5

## the board

TTGO T5 V2.3 Wireless WiFi Basic Wireless Module ESP-32 esp32 2.13 Inch ePaper Display Development board.

- SKU: H239, [github](https://github.com/Xinyuan-LilyGO/LilyGo-T5-ink-series)
- Model DEPG0213BN
- ESP32-D0WDQ6 (revision 1)
- WiFi, BT, Dual Core, 240MHz, Crystal is 40MHz

`esptool.py --port /dev/ttyUSB1 chip_id` tells us:

```
Chip is ESP32-D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz
```

I downloaded the latest stable generic [micropython ESP-IDF v4.x firmware](http://micropython.org/download/esp32/). Flash it by: (assuming board is on ttyUSB1)

```bash
esptool.py --chip esp32 --port /dev/ttyUSB1 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB1 --baud 460800 write_flash -z 0x1000 esp32-idf4-20200902-v1.13.bin
```

So now micropython is running on the board. 

An easier way to do the above is to use Mu, which has a flasher built it.

## Copy files

Mu-editor has a built in file manager but it wasn't working on my board, so I went with [ampy](https://github.com/scientifichackers/ampy).

Install that by: `pip install adafruit-ampy` then find the port the board is using.

On a mac this lists all the serial ports in use:
`ls -l /dev/tty.*`

On my machine I got `/dev/tty.usbserial-1420`, so ampy basics is:

- list files: `ampy --port /dev/cu.usbserial-1420 ls`
- put a file on the board: `ampy --port /dev/cu.usbserial-1420 put config.py`
- get a file: `ampy --port /dev/cu.usbserial-1420 get config.py`
- delete: `ampy --port /dev/cu.usbserial-1420 rm config.py`


## the display

This board comes with a 2.13 inch eink display.

todo: make it work!

## resources

- https://www.re-innovation.co.uk/docs/ttgo-e-paper-display/
- https://github.com/lewisxhe/TTGO-EPaper-Series
- https://github.com/peterhinch/micropython-nano-gui
- https://github.com/Xinyuan-LilyGO/LilyGo-eink-v2.3-micropython
- https://github.com/vroland/epdiy - drivers for eink screens


Micropython executes `boot.py` on startup, then runs `main.py` if found. So my code should go inside a main.py file. Mu should be able to see and write to the board, but its grayed out. 

todo: find a easy solution to write files to the board.
