---
title: "PyCon Australia 2018"
date: 2018-08-24
tags:
- python
---

Schedule: https://2018.pycon-au.org/schedule/

My notes for the talks I attended:

## [How Python saved a rescue dog - a foster fail story](https://2018.pycon-au.org/talks/45067-how-python-saved-a-rescue-dog-a-foster-fail-story/)

> This talk will tell the story of a foster fail, how Python helped to save the life of a rescue dog and how the initial medication feeder grew from a single IoT device into a full Internet of Dog (IoD) madness. I will show the design and implementation of the initial Python-based medication feeder, what we have learned from running it over the summer and how it has continued to grow into a multi IoT device, Python-powered, full dog carer solution. There will be microservice architecture drawings, Python code, and, of course, pictures of the dog!

- Works at [ANSTO](https://www.ansto.gov.au/research/facilities/australian-synchrotron/overview) - works on scientific software in Python
- were fostering a dog, Willow - fostering: look after for a limited time and prepare for adoption
- Willow was badly treated by previous owner and needed anti-anxiety medication every 8 hrs
- 4 weeks of meds, improved Willow a lot. But then they both went back to work, and nobody had adopted Willow. So they had two issues: monitor Willow and afternoon medication
- monitoring was easy - used a webcam. Considered off the shelf dispensers, but didn’t like
- Onion Omega2+ attached to a servo which dropped the treat+drugs on time
- First drug feeder:
  - VM in the cloud - wrote a flask webapp, backed by a [Redis](https://redis.io/) database. The webapp sent actions Feed|Home to the VM. The Onion has an endless loop which polls the VM every second asking for an action, and then does it.
  - polling is a very simple scheme,  and if anything breaks down, nothing bad happens, but there is a lag b/w button and action, as well as the dependency on the IOT and VM in cloud
  - usb audio using alsa libraries which would call the dog
- the IOT was only part of the puzzle - they had to train the dog as well. Ran this setup for a couple of months, worked suprisingly well. Sometimes failed becuase of power outages, so they added a UPS.
- Willow didn’t get adopted - so they adopted her. Now that they were going to have her, they decided to get serious about the IOT
- Split into infrastructure and service
  - Device: Raspberry Pi Zero connected to I/O, sensors, a Pi3 running gateway services, docker registery, [consul](https://www.consul.io/) server
  - Service: Web service exposing a RESTful API running on flask, service discovery using Consul, packaged in a docker container and depolyed using docker-compose
- pi zero is nice and simple, is using one per physical device/sensor
- the gateway service polls the VM for actions, then does a REST call to the relevant PiZero to do the action
- Future: websockets instead of polling, wants things event driven and real time readings for sensors. web interface with react

Q&A

- Why not docker swarm?
  - wanted to use consul

## [Lighting Macro Photographs with CircuitPython](https://2018.pycon-au.org/talks/45177-lighting-macro-photographs-with-circuitpython/)

> LED lighting rigs are expensive. Worse, they have little to no controls aside from on/off. Most are not dimmable and changing colors requires the use of gels. In this talk I will discuss how CircuitPython was used in conjunction with LEDs and microcontrollers to make a custom LED photo lighting rig.


- Stacey Morse [geekgirlbeta](https://twitter.com/geekgirlbeta), [web](https://geekgirlbeta.wordpress.com/) is an artist who also does macro photography, web dev in python
- art is awesome, but led lights are very expensive and crap. the intersection b/w art and tech: both are very process drivenl
- had a conversation with a python programmer who suggested python controlled lights could solve her lighting issues - and thus she started to learn how to program in micropython
- macro photography is very technical - there is a lot of math involved, understanding light, lens dynamics, lighting
- lights: on/off, select number of leds, control brightness, colour
- hardware: microcontroller, leds, rotary encoder, buttons, ir remote
- software: [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython) (very beginner friendly), [MicroPython](https://micropython.org/)
- went with neopixels for the lights - gives true white light as its RGBW
- used Feather M4 Express for the microcontroller
- the [code](https://github.com/geekgirlbeta/MacroLighting/blob/master/code.py) is very straightforward

Q&A:

- hot shoe
  - figures she can use the hot shoe in a camera to communicate with the light - so she can write light settings in the exif data
- what can she do with this which she can’t do with a traditional flash kit?
  - led’s blink, so u need them in blink in coordination with your camera settings. this allows her to focus on a specific part of an object. traidtional flashes are bigger, whole panels of lights

