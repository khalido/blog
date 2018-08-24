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
