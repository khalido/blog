---
title: "PyCon Australia 2018"
date: 2018-08-24
tags:
- python
---

Schedule: https://2018.pycon-au.org/schedule/

My notes for the talks I attended:

- [How Python saved a rescue dog - a foster fail story](#how-python-saved-a-rescue-dog---a-foster-fail-story)
- [Lighting Macro Photographs with CircuitPython](#lighting-macro-photographs-with-circuitpython)
- [Writing fast and efficient MicroPython](#writing-fast-and-efficient-micropython)
- [Asyncio in (Micro)Python](#asyncio-in-micropython)
- [Embedded applications using Python and Debian](#embedded-applications-using-python-and-debian)
- [Workplace Environment Sensing with Python](#workplace-environment-sensing-with-python)
- [Workplace Environment Sensing with Python](#workplace-environment-sensing-with-python)
- [Automating Your Home with Python, Raspberry Pi and Homekit](#automating-your-home-with-python-raspberry-pi-and-homekit)
- [Education Seminar Student Showcase](#education-seminar-student-showcase)
  - [MENACE - building a learning matchbox machine in Python](#menace---building-a-learning-matchbox-machine-in-python)
  - [Optimising Memory Retention via a Machine Learning based Flashcard System built in Python](#optimising-memory-retention-via-a-machine-learning-based-flashcard-system-built-in-python)
  - [Text Summariser](#text-summariser)
  - [NOR: creating generated worlds on iPad](#nor-creating-generated-worlds-on-ipad)
  - [Rule-Based Machine Translation](#rule-based-machine-translation)
  - [SVG Graph Calculator](#svg-graph-calculator)
  - [Emojifer in @ school](#emojifer-in--school)
  - [PyVlov’s Dog](#pyvlovs-dog)
  - [wrap up](#wrap-up)
- [Annie Parker](#annie-parker)
- [Describing Descriptors](#describing-descriptors)
- [What is the most common street name in Australia?](#what-is-the-most-common-street-name-in-australia)
- [End-to-end Energy Monitoring in Python](#end-to-end-energy-monitoring-in-python)
- [Python & Spreadsheets: Earth Dog Edition](#python--spreadsheets-earth-dog-edition)
- [Context Managers: You Can Write Your Own!](#context-managers-you-can-write-your-own)
- [Resurrecting the dead with deep learning](#resurrecting-the-dead-with-deep-learning)
- [Tom Eastman](#tom-eastman)
- [Tracy Osborn](#tracy-osborn)
- [Guide to your own artificial intelligence application in 3 easy steps](#guide-to-your-own-artificial-intelligence-application-in-3-easy-steps)
- [Hello to the World in 8 Web Frameworks (Micro, Batteries Included & Async)](#hello-to-the-world-in-8-web-frameworks-micro-batteries-included--async)
- [You Don't Need That!](#you-dont-need-that)
- [How To Publish A Package On PyPI](#how-to-publish-a-package-on-pypi)

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
  - led’s blink, so u need them in blink in coordination with your camera settings. this allows her to focus on a specific part of an object. traditional flashes are bigger, whole panels of lights


## [Writing fast and efficient MicroPython](https://2018.pycon-au.org/talks/45358-writing-fast-and-efficient-micropython/)

> MicroPython is a reimplementation of Python which is specifically designed to run on computing devices that have very few resources, such as CPU power, RAM and storage. Often when you write scripts in MicroPython you want to make the most of your available resources, and have code run as fast as possible (faster code usually saves power, which is important when running from a battery!) and there are certain ways of writing MicroPython code that are more efficient than others. In this talk I will go over the tricks and techniques for writing fast and efficient Python code in MicroPython. As part of this I will delve into some technical details of how MicroPython works, in order to better understand what it’s doing behind the scenes and how to make the most of it. I will discuss general techniques for making things run faster (some of which would be applicable to normal Python), as well as ways to completely avoid memory allocation, which is important for both efficiency and making code execution deterministic. The talk will include some hardware demos to show off the techniques, including five different ways to blink an LED fast.

- [Damien George](http://dpgeorge.net/) - creator of [MicroPython](https://twitter.com/micropython)
- loading local variables is fast, global variables is slow. So try to use local variables.
- its slow to call functions from within a function
- some things allocate memory on the heap, others don't - try not to allocate memory.
- don't allocate memory: All the basic statements like if/else, local variables, int arthimetic, some builtin funcs like any, len, etc
- does allocate memory: importing, defining functions and classes, global variables, data structures
- tips to reduce cpu time:
  - use funcs - for example put a loop within a func and call the func
  - don't use global, try to use local variables as much as possible
  - cache funcs
  - cache variables as local
  - prefer longer expressions, not split up ones
  - use consts `from micropython import const`
- tips to reduce ram usage:
  - don't use heap when possible
  - use short variable names
  - temp buffers
  - use XXX_into methods
  - don't use 8 or ** args
  - use const, minify scripts
  - use mpy-cross to produce .mpy - this saves a lof ot time in compiling the script on the device
  - ultimate solution is to freeze scripts into the firmware (bytecode gets stored into flash storage, advanced)
- within a func, preload methods `on = led.on` and then use `on()`. So when calling a method multiple times this is much faster.
- for small loops, unroll the loop
- viper mode - undocumented, being written, writes registers directly to say turn on/off leds
- can also write inline assembler in python syntax
- pre allocate a buffer and write to it

## [Asyncio in (Micro)Python](https://2018.pycon-au.org/talks/45338-asyncio-in-micropython/)

> Asyncio provides a way to achieve concurrency in a relatively simplistic fashion. However, first-time users still struggle with the concepts so let’s sort them out! Then we’ll see why it’s especially useful in an embedded environment.

- [Matt Trentini](https://twitter.com/matt_trentini) - a software engineer, has worked with lots of projects with embedded firmware with c compilers, has been looking for better alternatives
- micropython is the way forward for embedded development
- Coroutines - the ability to run things concurrently
  - use yield points to relingquish control and an event loop to scedule tasks
  - provides cooperative multitasking
  - concurrency isn't parallelism
- a lot of async funcs is similar - just needs `async def func` and `await` where are are awaiting stuff.
- coroutines (tasks) --><-- event loop --><--- blocking operatoins (network access, sleep, database queries)
- what about threads? wasn't this a solved problem? threads provid pre-emptive multi-tasking, but they get complex, are heavy (each thread needs its own stack) and hesienbergs
- Coroutines are better cause:
  - minimal overhead, high performance
  - locking is less problematic
  - more closely reemble synchrous code
- Coroutines in python are biult on generators and use `async/await` keywords
- [PEP 492](https://www.python.org/dev/peps/pep-0492/) in Python 3.5 brought async
- Python needed async to stay relevant and competitive with other async languages
- async needs all the funcs to support async code, so hard to use with older synchronus code
- async is in active development
- coroutines in micropython is a subset but for practical use the same
- async in embedded devices is exciting as threading support is limited and many embedded operations are cncurrent by nature
- classic problem in embedded space: Debouce
  - need to wait for a button to stop bouncing - since they're typically not digital
  - async lets us write a loop which pools the button, and when a button is pressed, it can await the sleep so the controller can do other things instead of just waiting on the button
- there is micropython-async - look up tutorial from Peter Hinch
- uPTV - counts down minutes to next train
  - NTP - time support `import ntptime`
  - HTTP request - uses a requests library - python has aiohttp, micropython has a very crude version
  - LED control
  - asyncio to create loop and run it forver - sync time, poll for train, update LED
- LED strip controller
  - rotary encoder to set brightness and push on/off
  - uses a async fade routine to smoothly fade to brightness
  - async means can change the brightness while still fading, so no waiting

Q&A

- ppl using coroutines for real time?
  - in experimental stage - if u request 5ms sleep, it can be less or more depending on what the other coroutines are doing
- how is it implemented?
  - in micropython uses queues implemnted in C
- timing and checking length of executable paths
  - up to you to define - for example a fade routine might have a 5ms delay b/w levels so `await sleep(5ms)`
- how do you deal with a blocking library?
  - put timeouts on things - call a func, if it takes too long to run, interrupt it, or use threads - async can push things into threads
- with asyncio, do you apprach problems differently from threads?
  - async feels more natural - you can state what you want to do. With threading you have to think a lot about synchronization and how long things will take.


## [Embedded applications using Python and Debian](https://2018.pycon-au.org/talks/41830-embedded-applications-using-python-and-debian/)

> Embedded boards such as Raspberry Pi and BeagleBone are programmed using Python and run on Linux Debian platform. Raspian is one of the widely used Linux platform on Raspberry Pi.The talk would be about the support provided by Python and Debian for embedded application.

- [Jaminy Prabaharan](https://www.linkedin.com/in/jaminy-prabaharan/) worked as an embedded engineer, was part of Google's Summer of Code
- 95% of code for embedded systems is writter in C/C++
- python vs c - python is very easy to use, but is slow - C runs fast but is slow to write/debug.
- some devices can run Cpython, like RPi running Raspbian


## [Workplace Environment Sensing with Python](https://2018.pycon-au.org/talks/45376-workplace-environment-sensing-with-python/)

> Connecting IoT devices using low power over wide area wireless (LoRaWAN) makes sense. But how LoRaWAN works, duty cycles, frequency plans, receive windows, etc. doesn’t.

> This talk will demystify how LoRaWAN works using PyCom devices.

- talk by Brian Danilko of [Likeable Software](http://www.likeablesoftware.com/)
- LoPy
- [Pycom](https://pycom.io/) has lots of examples for LoRa and LoRaWAN
- LoRa is the transport layer - patented, developed by Cycleo, Semtech owns it
  - uses a Chirp Spread Spectrum (CSS) to transmit info reliably using low power
  - uses different power levels, frequencies, bandwidths, spread factors to optimize power use vs time on air vs distance
- LoRoWAN adds the wide area network on top of LoRa
  - connects end nodes to the internet through gateways
  - encrypts for secure transmission, controls what devices can join the network, confirms and retries (but this doubles power and clogs airways so don't use if not needed)
- you have multiple end nodes talking to one gateway, which connects to the internet via a wired link (can be wireless too)
- can have multiple gateways for backup - so nodes can connect to multiple gateways
- join a LoRaWAN network by OTAA (over the air, same keys embedded in all devices) or ABP (unique keys)
- frequencies for gateways and nodes have to be the same - something to be aware of when setting up devices

## [Workplace Environment Sensing with Python](https://2018.pycon-au.org/talks/45376-workplace-environment-sensing-with-python/)

> Have you often wondered where the quietest spot in the office is right now? In this talk, we explain how we built a real-time system that does just that using CircuitPython.

- Aiden Ray, works at [BVN](http://www.bvn.com.au/)
- building awards are handed out before ppl use them - very little feedback from real users
- the web is totally instrumented, you know exactly whats going on
- the physical world is a lot less instrumented
- Amaon Go is sensored everywhere - this is where the world is moving, you get tons of data, can see where to improve
- Circuit Playground Express by Adafruit
- C/C++ vs Python boils down to runtime speed vs development speed
- Circuit Python is Adafruits fork of MicroPython, more beginner focused, doesn't have access to async, so you have a basic event loop
- `if sys.implementation == 'circuitpython'` to check implementation


## [Automating Your Home with Python, Raspberry Pi and Homekit](https://2018.pycon-au.org/talks/45170-automating-your-home-with-python-raspberry-pi-and-homekit/)

> Home Automation is a fun new field for the modern Pythonista. In this talk I will be walking through how a developer can leverage a python library to use the HomeKit service and automate the devices in their home. I will be covering topics like hardware selection for local and remote access, HomeKit service registration and management and potential security concerns around IoT.

- Sean Johnson [twtr](https://twitter.com/seansonbronson) [ln](https://www.linkedin.com/in/sean-johnson-50030280/)
- homekit is a software framework for controlling smart hardware, built on Apples HomeKit Accessory Protocol
- there are a few opensource implementations in node and python
- apple predefines hardware configurations, you can't define your own
- Home App allows manual and automated control of devices
- there are many existing hardware, from ikea to phillips
- Raspberry Pi - supports python
- uses [HAP-Python](https://github.com/ikalchev/HAP-python), demo of a controlling an aircon via infrared
- pretty straightforward, except tied to Apple and Siri

q & a

- IR is unidirectional so what happens if u miss a packet?
  - every packet is single state, so contains all the info in one go. So if a packet fails, the next one doesn't rely on it. Also, leep transmitter close to the receiver so the signal is clear.


## [Education Seminar Student Showcase](https://2018.pycon-au.org/education-showcase)

Friday August 24 2018, Education Track, C3.4 & C3.5, 16:00 AEST

> Eight short (10 min) talks from high school students across Australia. They’ll be talking about projects they’ve built with Python using machine learning, robotics, natural language processing, and more

### MENACE - building a learning matchbox machine in Python

- machine learning is the use of programming to make a computer learn from data
- inspired by Matt Parker from Standup Math channel on youtube
- problems with indexing errors leading to endless loop
- wants to use pygame or kivy to make a actual game

### Optimising Memory Retention via a Machine Learning based Flashcard System built in Python

> This project aims to leverage Python’s machine learning capabilities, combined with psychological theories of learning and forgetting, to construct predictive models of human memory in order to improve upon traditional flashcard systems.

> In this talk, I will share my experience of: (1) utilising Python’s sci-kit-learn package, alongside the Latent Skill Embedding package, to train, evaluate and visualise the performance of various models; (2) implementing the model into a web-based flashcard application built in Flask - a popular Python micro framework; and (3) testing the effectiveness of the system through a classroom experiment on 36 Japanese language students.

- http://josephtey.com/
- researched various techniques for the optimal time to review
- experimented on 40 students
- started with R, but how do u deploy with R? so moved on to Python as it can both train a model and an app to serve it with

### Text Summariser

> The Text Summariser is a program I built for when one is unable or unwilling to summarise information from a large block of text themselves. In my talk, I will discuss how it works, what inspired the project, and how I overcame the (many) challenges of building my program. I will also talk about computational linguistics and Natural Language Processing (NLP), two big components of how the text summariser works. After listening to this talk, you will have learnt some basic Natural Language Processing, and how you can apply it in Python Programs.

- sorts words by type - verbs, nouns, etc
- uses markov chains to summarize

### NOR: creating generated worlds on iPad

> NOR is a 2d puzzle exploration game for iPad that I made over the course of year 10. It features procedurally generated landscapes that collide with and can be edited by the player. The landscapes are host to procedurally generated bushes, trees and puzzles. My talk will discuss how I reached the point where I could set off on a large scale python coding project, how I built up the game and made the systems work, and how anyone can pick up an iPad and start developing.

- learned calculus for the game movements etc
- things are based on each other
- uses monte carlo to generate gaphics, of a random seed, which are dependend on the ground and level number
- used [pythonista](http://omz-software.com/pythonista/)
- uses momemtum + inertia for players movement

### Rule-Based Machine Translation

> The Text Summariser is a program I built for when one is unable or unwilling to summarise information from a large block of text themselves. In my talk, I will discuss how it works, what inspired the project, and how I overcame the (many) challenges of building my program. I will also talk about computational linguistics and Natural Language Processing (NLP), two big components of how the text summariser works. After listening to this talk, you will have learnt some basic Natural Language Processing, and how you can apply it in Python Programs.

- uses machine translation to switch from english to latin
- four main ways to translate: rule based, example based, statistical, neural
- Google Translate sucks at Latin translation
- very impressive work

### SVG Graph Calculator

> The name of my project is somewhat self-explanatory, it is an SVG Graph calculator. I know right? My talk is going to be about how I decided to do this project, and my struggles and innovations in making this project happen.

- turns an equation into a SVG graph
- Why? had to draw graphs for yr9 math class. There are online tools which do this already, but decided it would be fun to do this
- thought of writing it in python turtle, but too slow
- wanted something which worked on web
- had to reverse engineer SVG file
- if looking for inspiration, just copy something

### Emojifer in @ school

> Emojifer is an implementation of a sequence model in Machine Learning. It will analyse the meaning of a sentence and give it the appropriate emoji. Emojifier plays an important role in @ school which is a cloud-based learning management system written in React with Flask served as the server. Come along to this talk, if you want to know what’s under the hood of Emojfier and how I make it happen. Additionally, I’ll talk about some of the problems I’ve encountered so far and how I overcame it. This talk will give you an idea of how to get started in Machine Learning as well as full-stack web development if you’re new to the area.

- http://emojifier.surge.sh/#/
- https://github.com/anhphamduy/emojifier_model
- uses RNN and LSTM
- keras and flask
- made his own training data
- lessons: best way to learn is to teach, jump in head first, pair program, stack overflow is awesome

### PyVlov’s Dog

> PyVlov’s Dog is a simulation software created to dynamically train neural networks for the control of basic robots. When we started this project we had a limited understanding of neural networks, so we simplified the problem by visualising it as training a dog.

> We developed this project as a way to streamline the concept of neural networks through this metaphor of training a dog, so as to facilitate its use as an education tool. In this talk we will talk about how we made the software, the difficulties we faced in creating it and the way in which it works. We will also discuss the development of the robot’s hardware and the way in which it is represented within the simulation. Finally, we will cover the way in which we developed the principles of ease of use, and visual clarity within the program, to allow for use by people of all skill sets.

- purpose of project was to understand neural networks, and did this through training a dog to do what its told to do (by creating a set of rules)
- sensors are the input to a NN, which gives a output to a motor
- made a simulation to train the NN - user defines a dog and an environment, once happy with the NN, throw it into the actual robot
- uses arduino to control motors, raspberry pi to run NN
- hardware is hard!
- used pymunk to handle the physics of the sim, but is only 2d, so they had to work around that
- needed to use tkinter with pygame
- https://pyvlov.wordpress.com/

### wrap up

- learnt a lot from throwing themselves in the deep end to do a project.
- python is a fantastic learning language, don't babyfeed students, support them in the deep end

----------

Saturday talks

## [Annie Parker](https://2018.pycon-au.org/talks/annie)

> [Annie](https://twitter.com/annie_parker) is a co-founder of [Techfugees Australia](https://techfugees.com/chapters/australia/) - a global movement connecting the technology ecosystem together with newly arrived refugees here in Australia to help them integrate into their new communities. In this talk, Annie will be sharing her experience of how Techfugees works and some of the success stories they’ve had along the way

- 68.5M displaced ppl around the world, with 25M refugees
- the tech community can help, done 5 hackathons so far
- 6th hackathon 24/25th Nov in Blacktown - signup
  - looking for ppl who can put togther really early stage stuff and know whats out there to use
  - don't need to be deeply skilled
- they've made significant changes  - new companies, connected investors to customers, jobs, community impact, media stories, inspiration
- case studies:
  - refugeetalent created at first hackathon in 2015, placed 150 ppl into jobs
  - onestep founded at second hackathon, connects refugees
  - muralisto - makes community art
- Shaqaeq Rezai [ln](https://www.linkedin.com/in/shaqaeq-rezai/), [twtr](https://twitter.com/r_Shaqaeq) - 18yr hazara Afghan refugee, moved to Australia from Iran where she faced a lot of discrimination - attended a hackathon, built an AI to track moods, got scholarship, started [Directa Australia](https://www.linkedin.com/company/directa-australia/). Met the CEO of the Iconic through the startup scene, who is also Aghan.
  - wants to help ppl through tech
- most refugees have good knowledge of tech, smart phones
- 50% of business in Australia have been started by a refugee or a migrant

## [Describing Descriptors](https://2018.pycon-au.org/talks/42582-describing-descriptors/)

> Descriptors are a little known feature of Python. They provide a way for a programmer to customize the storage and retrieval of different instance variables. In this talk, you will learn about the descriptor protocol, what it can be used for, and how to implement a descriptor.

- Matthew Egan [web](https://mattjegan.com/) [twtr](https://twitter.com/NullMatthew)
- why descriptors? often overlooked, used primarily by library developers
- so we have a basic class, Person, which stores info like name, etc
- our dream Person class makes sure names are capitilized properly
- `__setattr__(self, attr, value)` is called inside a class when an attribute is being set, so if Person.name is assigned, it runs through the setattr method which can can modify the variable from `name` to `Name`
- can use setter methods like `@name.setter` inside the class, but this only applies to the specific class
- the descriptor protocl allows a more general solution, has four attributes: get, set, deelte, set_name
  - `__get__(self, instance, owner)`
  - `__set__(self, instance, value)`
  - `__delete__(self, ??)`
  - `__set_name__(self, owner, name)` - doesn't take instance argument as its only called on class creation
- when you access an attribute in python, it goes through a lookup process, which gets it from a dict, a data descriptor or a non_data descriptor
- non-data descrptors: staticmethod, classmethod, abc.abstractmethod
- if we have a Person class and tons of Person objects, we write just one descriptor which covers all the objects
- `from weakref import WeakKeyDictionary` - when we delete an object which is also in the dict, it automatically removes it from the dictionary
- look up some example descriptors using weakref - he gave an example of using a descriptor to make sure names are capitilized
- descriptors have use cases like: 
  - replicating customization for multiple attrs without caring about name
  - django generic foreign keys
  - custom validation e.g only non negative integers for age 
  - better error msgs - can prepend the name of attribute being set to the error msg so its more descriptive
- talk code: https://github.com/mattjegan/describing-descriptors

q & a:

- runtime perf
  - depends on impementation, external calls
- can you chain descriptors?
  - should be possible, but haven't done it. 
- how do u replace the descriptor itself?
  - delete it off the class itself
- what happens if you pickle an object with a descriptor?
  - pickle is unsecure so don't use it
- 

## [What is the most common street name in Australia?](https://2018.pycon-au.org/talks/45005-what-is-the-most-common-street-name-in-australia/)

> Finding the most common street name in Australia may sound like a simple thing to do - but it quickly devolves into a scenic tour of all the things that go wrong when doing data analytics. I’ll be giving advice on how to avoid these speed bumps along with how to work with OpenStreetMaps in Python.

## [End-to-end Energy Monitoring in Python](https://2018.pycon-au.org/talks/45073-endtoend-energy-monitoring-in-python/)

> This talk presents the development of an open-source (hardware and software) Energy Monitoring system with as much Python as possible. With the firmware written in Micropython (successfully tested on ESP8266 and ESP32 using virtually the same code), Unix port of micropython was used as the dev environment. Data collection platform using the classic Graphite Time-series database and some fun neural-network based analysis of the collected data also in Python with Keras, just to cover AI/ML buzzwords as well.

- did not attend, look up talk notes/video/github

## [Python & Spreadsheets: Earth Dog Edition](https://2018.pycon-au.org/talks/45310-python-spreadsheets-earth-dog-edition/)

Saturday August 25 2018, C3.6, 11:50 AEST

## [Context Managers: You Can Write Your Own!](https://2018.pycon-au.org/talks/45062-context-managers-you-can-write-your-own/)

Saturday August 25 2018, C3.6, 14:10 AEST

## [Resurrecting the dead with deep learning](https://2018.pycon-au.org/talks/45179-resurrecting-the-dead-with-deep-learning/)

*Saturday August 25 2018, C3.3, 14:50 AEST*



## [Tom Eastman](https://2018.pycon-au.org/talks/tom)

*Saturday August 25 2018, Cockle Bay, 16:00 AEST*


## [Tracy Osborn](https://2018.pycon-au.org/talks/tracy)

*Sunday August 26 2018, Cockle Bay, 09:10 AEST*


## [Guide to your own artificial intelligence application in 3 easy steps](https://2018.pycon-au.org/talks/45386-guide-to-your-own-artificial-intelligence-application-in-3-easy-steps/)

*Sunday August 26 2018, C3.3, 10:30 AEST*


## [Hello to the World in 8 Web Frameworks (Micro, Batteries Included & Async)](https://2018.pycon-au.org/talks/45282-hello-to-the-world-in-8-web-frameworks-micro-batteries-included-async/)

*Sunday August 26 2018, C3.4 & C3.5, 11:10 AEST*


## [You Don't Need That!](https://2018.pycon-au.org/talks/45184-you-dont-need-that/)

*Sunday August 26 2018, C3.4 & C3.5, 13:30 AEST*

## [How To Publish A Package On PyPI](https://2018.pycon-au.org/talks/44349-how-to-publish-a-package-on-pypi/)

*Sunday August 26 2018, C3.3, 14:10 AEST*

