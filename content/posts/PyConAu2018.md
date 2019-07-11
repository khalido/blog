---
title: "PyCon Australia 2018"
date: 2018-08-24
tags:
- python
---

My notes for the [PyConAU 2018 talks](https://2018.pycon-au.org/schedule/) I went to.

- [How Python saved a rescue dog - a foster fail story](#how-python-saved-a-rescue-dog---a-foster-fail-story)
- [Lighting Macro Photographs with CircuitPython](#lighting-macro-photographs-with-circuitpython)
- [Writing fast and efficient MicroPython](#writing-fast-and-efficient-micropython)
- [Asyncio in MicroPython](#asyncio-in-micropython)
- [Demystifying LoRaWAN with PyCom](#demystifying-lorawan-with-pycom)
- [Workplace Environment Sensing with Python](#workplace-environment-sensing-with-python)
- [Automating Your Home with Python, Raspberry Pi and Homekit](#automating-your-home-with-python-raspberry-pi-and-homekit)
- [Education Seminar Student Showcase](#education-seminar-student-showcase)
- [Keynote: Annie Parker on Techfugees](#keynote-annie-parker-on-techfugees)
- [Describing Descriptors](#describing-descriptors)
- [What is the most common street name in Australia?](#what-is-the-most-common-street-name-in-australia)
- [Why you should care about types: How Python typing helped my team scale](#why-you-should-care-about-types-how-python-typing-helped-my-team-scale)
- [Running Python web applications in Docker](#running-python-web-applications-in-docker)
- [Context Managers: You Can Write Your Own!](#context-managers-you-can-write-your-own)
- [Snakes in your Games](#snakes-in-your-games)
- [Keynote: Tom Eastman on getting better](#keynote-tom-eastman-on-getting-better)
- [Saturday Lightening talks](#saturday-lightening-talks)
- [Tracy Osborn: Clueless](#tracy-osborn-clueless)
- [Guide to your own artificial intelligence application in 3 easy steps](#guide-to-your-own-artificial-intelligence-application-in-3-easy-steps)
- [Hello to the World in 8 Web Frameworks](#hello-to-the-world-in-8-web-frameworks)
- [Functional Programming demystified](#functional-programming-demystified)
- [You Don't Need That!](#you-dont-need-that)
- [There is no "now" and sensor data's the worst](#there-is-no-%22now%22-and-sensor-datas-the-worst)
- [Watch out for Safety Bandits!](#watch-out-for-safety-bandits)
- [Sunday Lightening talks](#sunday-lightening-talks)

## How Python saved a rescue dog - a foster fail story

> This talk will tell the story of a foster fail, how Python helped to save the life of a rescue dog and how the initial medication feeder grew from a single IoT device into a full Internet of Dog (IoD) madness. I will show the design and implementation of the initial Python-based medication feeder, what we have learned from running it over the summer and how it has continued to grow into a multi IoT device, Python-powered, full dog carer solution. There will be microservice architecture drawings, Python code, and, of course, pictures of the dog! [#](https://2018.pycon-au.org/talks/45067-how-python-saved-a-rescue-dog-a-foster-fail-story/)

{{< youtube EqQj5os3Mfw >}}

- Andreas Moll - [twtr](https://twitter.com/SciAndreas) - Works at [ANSTO](https://www.ansto.gov.au/research/facilities/australian-synchrotron/overview) on scientific software in Python
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

**takeaway:** genius AND way overkill. but infrastructure is hard. consider using orchestration tools.

## Lighting Macro Photographs with CircuitPython

> LED lighting rigs are expensive. Worse, they have little to no controls aside from on/off. Most are not dimmable and changing colors requires the use of gels. In this talk I will discuss how CircuitPython was used in conjunction with LEDs and microcontrollers to make a custom LED photo lighting rig. [#](https://2018.pycon-au.org/talks/45177-lighting-macro-photographs-with-circuitpython/)

{{< youtube JAgCZ70Q3sg >}}

- Stacey Morse - [geekgirlbeta](https://twitter.com/geekgirlbeta), [web](https://geekgirlbeta.wordpress.com/) is an artist who also does macro photography, web dev in python
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

**takeaway:** building a real tangible project is fun. Curcuit Python looks super easy to use.

## Writing fast and efficient MicroPython

> MicroPython is a reimplementation of Python which is specifically designed to run on computing devices that have very few resources, such as CPU power, RAM and storage. Often when you write scripts in MicroPython you want to make the most of your available resources, and have code run as fast as possible (faster code usually saves power, which is important when running from a battery!) and there are certain ways of writing MicroPython code that are more efficient than others. In this talk I will go over the tricks and techniques for writing fast and efficient Python code in MicroPython. As part of this I will delve into some technical details of how MicroPython works, in order to better understand what it’s doing behind the scenes and how to make the most of it. I will discuss general techniques for making things run faster (some of which would be applicable to normal Python), as well as ways to completely avoid memory allocation, which is important for both efficiency and making code execution deterministic. The talk will include some hardware demos to show off the techniques, including five different ways to blink an LED fast. [#](https://2018.pycon-au.org/talks/45358-writing-fast-and-efficient-micropython/)

{{< youtube hHec4qL00x0 >}}

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

**takeaway:** micropython can be fast. don't use globals, but everyone knows that already, so instead apply some of the tricks from above, like caching methods, and for micropython don't have too many funcs.

## Asyncio in MicroPython

> Asyncio provides a way to achieve concurrency in a relatively simplistic fashion. However, first-time users still struggle with the concepts so let’s sort them out! Then we’ll see why it’s especially useful in an embedded environment.[#](https://2018.pycon-au.org/talks/45338-asyncio-in-micropython/)

{{< youtube tIgu7q38bUw >}}

- [Matt Trentini](https://twitter.com/matt_trentini) - a software engineer, has worked with lots of projects with embedded firmware with c compilers, has been looking for better alternatives
- micropython is the way forward for embedded development
- Coroutines - the ability to run things concurrently
  - use yield points to relingquish control and an event loop to scedule tasks
  - provides cooperative multitasking
  - concurrency isn't parallelism
- a lot of async funcs is similar - just needs `async def func` and `await` where are are awaiting stuff.
- `coroutines (tasks) --><-- event loop --><--- blocking operations` (network access, sleep, database queries)
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

**takeaway:** get micropython hardware and start coding. Understand async better, it seems pretty straightforward, and on slow hardware a godsend - i.e async sending logs + async doing other stuff makes for easy real time monitering even if the machine is stuck on something..


## Demystifying LoRaWAN with PyCom

> Connecting IoT devices using low power over wide area wireless (LoRaWAN) makes sense. But how LoRaWAN works, duty cycles, frequency plans, receive windows, etc. doesn’t. [#](https://2018.pycon-au.org/talks/44704-demystifying-lorawan-with-pycom/)

> This talk will demystify how LoRaWAN works using PyCom devices.

{{< youtube L-fh7PSpPMc >}}

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

**takeaway:** look at LoRo/PyCom if using wireless IOT away from wifi.

## Workplace Environment Sensing with Python

> Have you often wondered where the quietest spot in the office is right now? In this talk, we explain how we built a real-time system that does just that using CircuitPython. [#](https://2018.pycon-au.org/talks/45376-workplace-environment-sensing-with-python/)

{{< youtube u4rSKNX_spA >}}

- Aiden Ray, works at [BVN](http://www.bvn.com.au/)
- building awards are handed out before ppl use them - very little feedback from real users
- the web is totally instrumented, you know exactly whats going on
- the physical world is a lot less instrumented
- Amaon Go is sensored everywhere - this is where the world is moving, you get tons of data, can see where to improve
- Circuit Playground Express by Adafruit
- C/C++ vs Python boils down to runtime speed vs development speed
- Circuit Python is Adafruits fork of MicroPython, more beginner focused, doesn't have access to async, so you have a basic event loop
- `if sys.implementation == 'circuitpython'` to check implementation

**takeaway:** pervasive monitoring is creepy but its going to happen. Circuit Python is amazingly easy. Make something with it.

## Automating Your Home with Python, Raspberry Pi and Homekit

> Home Automation is a fun new field for the modern Pythonista. In this talk I will be walking through how a developer can leverage a python library to use the HomeKit service and automate the devices in their home. I will be covering topics like hardware selection for local and remote access, HomeKit service registration and management and potential security concerns around IoT. [#](https://2018.pycon-au.org/talks/45170-automating-your-home-with-python-raspberry-pi-and-homekit/)

{{< youtube SiLtPgeTZLA >}}

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

**takeaway:** No Apple, hence no homekit for me.

## Education Seminar Student Showcase

Friday August 24 2018, Education Track, C3.4 & C3.5, 16:00 AEST

> Eight short (10 min) talks from high school students across Australia. They’ll be talking about projects they’ve built with Python using machine learning, robotics, natural language processing, and more [#](https://2018.pycon-au.org/education-showcase)

{{< youtube QNAgPjbn0Ws >}}

**MENACE - building a learning matchbox machine in Python**

- machine learning is the use of programming to make a computer learn from data
- inspired by Matt Parker from Standup Math channel on youtube
- problems with indexing errors leading to endless loop
- wants to use pygame or kivy to make a actual game

**takeaway:** awesome.

**Optimising Memory Retention via a Machine Learning based Flashcard System built in Python**

> This project aims to leverage Python’s machine learning capabilities, combined with psychological theories of learning and forgetting, to construct predictive models of human memory in order to improve upon traditional flashcard systems.

> In this talk, I will share my experience of: (1) utilising Python’s sci-kit-learn package, alongside the Latent Skill Embedding package, to train, evaluate and visualise the performance of various models; (2) implementing the model into a web-based flashcard application built in Flask - a popular Python micro framework; and (3) testing the effectiveness of the system through a classroom experiment on 36 Japanese language students.

- http://josephtey.com/
- researched various techniques for the optimal time to review
- experimented on 40 students
- started with R, but how do u deploy with R? so moved on to Python as it can both train a model and an app to serve it with

**takeaway:** build my own flash cards to learn stuff with spaced repetition.

**Text Summariser**

> The Text Summariser is a program I built for when one is unable or unwilling to summarise information from a large block of text themselves. In my talk, I will discuss how it works, what inspired the project, and how I overcame the (many) challenges of building my program. I will also talk about computational linguistics and Natural Language Processing (NLP), two big components of how the text summariser works. After listening to this talk, you will have learnt some basic Natural Language Processing, and how you can apply it in Python Programs.

- sorts words by type - verbs, nouns, etc
- uses markov chains to summarize

**takeaway:** too much cleverness going on to summarize.

**NOR: creating generated worlds on iPad**

> NOR is a 2d puzzle exploration game for iPad that I made over the course of year 10. It features procedurally generated landscapes that collide with and can be edited by the player. The landscapes are host to procedurally generated bushes, trees and puzzles. My talk will discuss how I reached the point where I could set off on a large scale python coding project, how I built up the game and made the systems work, and how anyone can pick up an iPad and start developing.

- learned calculus for the game movements etc
- things are based on each other
- uses monte carlo to generate gaphics, of a random seed, which are dependend on the ground and level number
- used [pythonista](http://omz-software.com/pythonista/)
- uses momemtum + inertia for players movement

**takeaway:** procedural generation is awesome.

**Rule-Based Machine Translation**

> The Text Summariser is a program I built for when one is unable or unwilling to summarise information from a large block of text themselves. In my talk, I will discuss how it works, what inspired the project, and how I overcame the (many) challenges of building my program. I will also talk about computational linguistics and Natural Language Processing (NLP), two big components of how the text summariser works. After listening to this talk, you will have learnt some basic Natural Language Processing, and how you can apply it in Python Programs.

- uses machine translation to switch from english to latin
- four main ways to translate: rule based, example based, statistical, neural
- Google Translate sucks at Latin translation
- very impressive work

**takeaway:** NLP for the win.

**SVG Graph Calculator**

> The name of my project is somewhat self-explanatory, it is an SVG Graph calculator. I know right? My talk is going to be about how I decided to do this project, and my struggles and innovations in making this project happen.

- turns an equation into a SVG graph
- Why? had to draw graphs for yr9 math class. There are online tools which do this already, but decided it would be fun to do this
- thought of writing it in python turtle, but too slow
- wanted something which worked on web
- had to reverse engineer SVG file
- if looking for inspiration, just copy something

**takeaway:** good basis for building a equation solver.

**Emojifer in @ school**

> Emojifer is an implementation of a sequence model in Machine Learning. It will analyse the meaning of a sentence and give it the appropriate emoji. Emojifier plays an important role in @ school which is a cloud-based learning management system written in React with Flask served as the server. Come along to this talk, if you want to know what’s under the hood of Emojfier and how I make it happen. Additionally, I’ll talk about some of the problems I’ve encountered so far and how I overcame it. This talk will give you an idea of how to get started in Machine Learning as well as full-stack web development if you’re new to the area.

- http://emojifier.surge.sh/#/
- https://github.com/anhphamduy/emojifier_model
- uses RNN and LSTM
- keras and flask
- made his own training data
- lessons: best way to learn is to teach, jump in head first, pair program, stack overflow is awesome

**takeaway:** everyone needs a emojifier.

**PyVlov’s Dog**

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

**takeaway:** interesting project to follow. The future is training your own robot to do something.

**educational talks wrap up**

- high school students are doing amazing stuff
- learnt a lot from throwing themselves in the deep end to do a project.
- python is a fantastic learning language, don't babyfeed students, support them in the deep end

----------

Saturday talks

## Keynote: Annie Parker on Techfugees

> [Annie](https://twitter.com/annie_parker) is a co-founder of [Techfugees Australia](https://techfugees.com/chapters/australia/) - a global movement connecting the technology ecosystem together with newly arrived refugees here in Australia to help them integrate into their new communities. In this talk, Annie will be sharing her experience of how Techfugees works and some of the success stories they’ve had along the way [#](https://2018.pycon-au.org/talks/annie)

{{< youtube GlMVcZfFFGI >}}

- technology has a huge impact on changing peoples lives
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

**my takeaway:** this is awesome, go to their hackathon in Nov. Don't need ninja skills, a lot is just about knowing what is out there in the tech space which can help.

## Describing Descriptors

> Descriptors are a little known feature of Python. They provide a way for a programmer to customize the storage and retrieval of different instance variables. In this talk, you will learn about the descriptor protocol, what it can be used for, and how to implement a descriptor. [#](https://2018.pycon-au.org/talks/42582-describing-descriptors/)

{{< youtube lmcgtUw5djw >}}

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

**my takeaway:** descriptors are useful, can apply across classes, so makes for better code

## What is the most common street name in Australia?

> Finding the most common street name in Australia may sound like a simple thing to do - but it quickly devolves into a scenic tour of all the things that go wrong when doing data analytics. I’ll be giving advice on how to avoid these speed bumps along with how to work with OpenStreetMaps in Python. [#](https://2018.pycon-au.org/talks/45005-what-is-the-most-common-street-name-in-australia/)

{{< youtube eGgBU2Pl6iA >}}

- Rachel [git](https://github.com/RachelBunder), [twtr](https://twitter.com/ADuckIsMyFiend), [ln](https://www.linkedin.com/in/rachelbunder/) works at Solar Analytics
- read an article about most common street names in America, got her interested about Australian streets
- G-NAF is australian geocoded data containing every address/street
- used OSM, since it has every country, instead of G-NAF
- couldn't just export all of Australia data from OSM
- used metro extracts to download geojson, which has now gone offline
- geojson includes a geometery feature e.g roads defined as a series of points (a line!)
- used [geopandas](http://geopandas.org/) - works like pandas
- osm has all kinds of road types, so have to think about it, so what exactly is a street? She went with a street is something with a name which a car can drive on
- see her [blogpost on cleaning OSM data](https://rachelbunder.github.io/Cleaning-OSM/)
- she got victoria rd and pacific highway as most common street names in Sydney, which didn't sound right
- so drew a plot, and found out OSM saw streets as segments, so long streets appeared many times
- shapely is a package which merges line segments together, but didn't do a great job
- so she wrote her own function to knit streets together - get road segments with same name, find ones which are close together, merge
- there is a distance func to find distance b/w geometeries
- had to parse names, as street names have a name and a descriptor, like parade, street, avenue, etc. This was not easy as there are a lot of variations, too many!
- what about Little Street? is that same as Street?
- she wanted to use this for different countries, but each country has different street descriptors, so the Australia model didnt' work for other countries
- used [overpass turbo](https://overpass-turbo.eu/) api to get all of Australia's data - but was hitting api limits so had to break Au into a grid and make multiple calls
- most common street names in Australia: Park, Railway, George, Church, Victoria
- learnings:
  - start small - Sydney over Australia
  - choose something familiar
  - check your biases
  - constant vigilant - test, draw stuff (she plotted streets on a map)
  - know your problem

**my takeaway:** a suprisingly simple question can lead to a whole lot of learning. Answer a few simple q's myself using python.

## Why you should care about types: How Python typing helped my team scale

> By now you have probably all heard about Python static typing. But why should you care? Are types in Python even Pythonic? Is Python turning into Java? Type annotations are Pythonic, trust Guido’s word for it, and Python is definitely not turning into Java.

> The greatest benefit of types in large Python codebases is the fact that the input and output structures of a function are obvious from just looking at the signature. In the untyped world the definition for the class you are looking for may be N jumps away, hidden somewhere deep in the codebase, and you don’t have a direct reference to it. In the best possible case grepping for it will yield just a few results and you will be able to spot what you are looking for. In the worst case though, you will have hundreds of hits and you will have to start your application and inspect the type at runtime to figure out what is going on, which make the development cycle slow and tedious.

> Come to this talk if you want to know more about the typing system in Python, how to gradually add it to your codebase and what benefits will your team get in the long run! I will also cover some advanced tools like the runtime type collection system, MonkeyType, and the just open sourced type checker, Pyre![#](https://2018.pycon-au.org/talks/45224-why-you-should-care-about-types-how-python-typing-helped-my-team-scale/)

{{< youtube h1cD3a7ys8Q >}}

- Luka Sterbic [git](https://github.com/Sterbic) - works at Facebook
- [talk slides and code](https://github.com/Sterbic/PyCon-AU-2018)
- why should I care about typing?
  - you can call modules from far away, in a large codebase can be many imports away, so its not clear what kind of data object gets returned
  - with typed codes, its obvious what the input and output is, and in a modern IDE like PyCharm its just one click away
  - for new engineers, typed code makes it much easier to start coding as its both obvoius from the code and there is more context provided by the IDE
- Are Python types Pythonic?
  - typing in python is optional and doesn't impact runtime
  - zen of python says explicit is better, reduce ambiguity and readability counts - and type hints delivers all this
  - Guido said so
- typing 101
  - what needs to be annotated - variables going into a function
  - covers most: `from typing import List, Set, Dict, Tuple`
  - Union `from typing import Union, Optional` gives a way to return one of a list of objects like `Union[User, Page, None]` indicates any one of those three objects can be returned
    - can also use Optional to indicate return is optional
  - `from typing import Type, TypeVar`
    - `TypeVar` are placeholders
- mypy is the most commonly used type checker
- advanced topics: forward references, TYPE_CHECKING, @overload
  - Pyre is facebook's open source type checker, much faster than mypy
- typing in the real world
  - new project, just type everything from day 1, use a type checker in CI
  - exisiting projects: understand gradual typing. if a function isn't annotated, then if it calls a annotated function then all type errors are ignored. You delay triggering errors until the calling function is also type hinted.
    - type common libraries, like utils.py which is used all over the place
    - keep running the type checker
    - add type checker into CI
    - add types to new code
  - MonkeyType - created by Instagram
    - collects typing info at runtime and logs them, generates type stubs then applies them
- tips and tricks:
  - say you have a class, but you want to pass in a superclass - that will fail. use Protocol from typing_extensions
  - typeshed
  - type: ignore - silence typing error on a statement

**my takeaway:** types are pythonic, more readable, safer. use gradual typing and go all in!

## Running Python web applications in Docker

> An introduction on running Python web applications in Docker, covering how to structure your project, running the project in both development and production, testing the project, and compiling static assets for your frontend. [#](https://2018.pycon-au.org/talks/45205-running-python-web-applications-in-docker/)

{{< youtube 9L6x2j-7eVQ >}}

- Tim Heap [@tim_heap](https://twitter.com/tim_heap) [git](https://github.com/timheap)
- talk [code and slides](https://github.com/timheap/python-apps-in-docker)
- [Docker](https://www.docker.com/) is a determinisitic application image, runs in a isolated execution environment, composable containers
- how to structure your python app to make it easy to deploy in docker
  - built as normal, with some constraints
  - runs as a WSGI app, connects to a web service like apache
  - project code all in one top level module, which can have submodules
  - a seperate directory for deployment and development
  - have one config file in the main project directory with all the base settings the app needs to run, seperate ones for development
  - dev just hard code config variables, production pull in from the environment `os.environ`
- Testing
- you might want some other tasks running in a seperate container to the web server

q & a:

- why seperate config files for dev and prod?
  - cause in dev you often need some weird things which you don't need/want for production.
- how do u manage logging in an app?
  - configure it the normal way, then pipe it somewhere. its just running python so just do it in the normal way
- why we wouldn't use docker-compose in production
  - there isn't a way to gracefully bring it down and back up. In production use something like kubernetes which does all the magic
- process monitoring like supervisord
  - say u have a webapp image, a celery image, the supervisord runs those images. you would rarely run supervisord inside a docker container

**my takeaway:** Docker is convuluted. I wish the world would just rather clean up linux so we can go back to running things directly instead of having to faff around with docker containers.

## Context Managers: You Can Write Your Own!

> Did you know context managers go beyond with open('myfile.txt', 'r') as f? In fact, you can even write your own! Context managers are an amazing tool for managing resources safely. They make your code look great, and they’re now easier to write than ever thanks to contextlib! Come get contextual!  [#](https://2018.pycon-au.org/talks/45062-context-managers-you-can-write-your-own/)

{{< youtube -tpn94V9vK4 >}}

- Dan [git](https://github.com/banool) [web](https://dport.me/)
- [talk slides: dport.me/pycon.pdf](https://dport.me/pycon.pdf)
- context managers manage your context, like the famous `with file as :`
- why use them: you can't forget to close resources and they make code prettier by abstracting
- `contexlib` has all kind of goodies in it, so look it up

```python
from contextlib import suppress

def kill_process(pid):
with suppress(ProcessLookupError):
  os.kill(pid, signal.SIGKILL)
```

- write your own context managers - see slide deck for examples
- its just a class with a dunder enter and a dunder exit method
- decorator is just a func which takes a func and returns a new func
  - `@decorator` on top of a func is just syntactic sugar for `decorator(func)`
- generators return one value at a time until they have nothing else to return
  - they maintain state until exhausted
- `from contextlib import contextmanager` decorator builds the enter and exit methods for you - the enter method is everything before yield, the the exit method is evreything after yield
- scope - variables defined inside context managers still exist after its closed
- context managers can deal with exceptions, can use suppress

**my takeaway:** use more decorators and context managers

## Snakes in your Games

> When thinking about where to start with python and games, the first thing that might come to mind is pygame. However, python has been used in many well known commercial games titles and can be used in many different ways throughout the game development process. This talk will examine a range of game titles, genres and platforms, from AAA to Indie, to show how python is being used in each; discussing the strength and weaknesses of using python, how it has been done, and how it might be in the future.

{{< youtube WbnZqeLL1a8 >}}

- [@ducky_tape](https://twitter.com/ducky_tape)
- lots of python gaming platforms like [Ren'Py](https://www.renpy.org/), PyVida
- open source tools like Gimp have python plugins
- PyAudioGame, Audio Game Kit for Python
- 3d engines: [panda3d](https://www.panda3d.org/) - but need tools like Maya to make animations - python is very handy for scripting animations
- python is used a lot for automation inside games
- post release: for some big titles python is used to make addons

**my takeaway:** there is a lot of python out there.

## Keynote: Tom Eastman on getting better

> how we learn to get better at our craft, and also how we – all too easily – do the opposite. [#](https://2018.pycon-au.org/talks/tom)

{{< youtube 9E3qhqWFJ2c >}}

- [twtr](https://twitter.com/tveastman) [web](https://eastman.net.nz/)
- been using Python since 2002! Python was hip way back then
- joined a super smart team, felt out of place
- new knowledge deepens your understanding of what you already know
- we are poor judges of whne we're learning well or not
- real learning feels sucky, like when trying to debug broken code with multiple layers of abstraction
- effortful retreival - have to write down stuff in your own words to understand. don't absorb the words, absorb the knowledge
- using is the the only way to make it stick.
- use spaced repitition. flashcards are highly effective.
  - buid my own flashdeck
- did a contract job for which had to learn ruby in 4 days. got two big fat books on ruby, used a pomodoro app on phone, and read both books cover to cover.
  - restate things in terms you understand
  - absorbed more than had expected
  - primed by layout of boks, which makes it faster to look up bits as needed
  - learning an unfamiliar language made him a better python developer
- sticking to only one language deprives you of experience
- self sabotage - when you think you're smart, you tend to avoid things which make you look not smart. internalized that effort is whats needed when you're not talented.
- Carol Dweck's "fixed vs growth mindset" - are our abilities fixed or can we grow them?
- Growth mindset: we can improve with effort, this is the one we want
- be careful about excuses
- thinking I should have been been good at this by now is deafeatist
- you can have a fixed mindset for ages about many things
- sitting down and working on a thing is an amazingly powerful way to learn that thing
- takeaways:
  - effort of learning isn't comfy - if feeling comfortable learning its a warning sign
  - don't feel bad about being bad at something

**my takeaway:** think you can do it, and learn by doing. don't get comfy and don't feel bad about sucking at something.

## Saturday Lightening talks

{{< youtube BmWLhVMWC9I >}}

Digital Earth Australia

- archive of Australia's space/earth/ocean data
- they try and figure out how to display things to see changes over time, showed impressive animationg of pictures alongside a graph of flow changing over time
- code is all open source: [GeoscienceAustralia github](https://github.com/GeoscienceAustralia)

FuPy

- [web](fupy.github.com)
- hardware is hard, FPGA makes hardware into software, making it easier to fix bugs
- FPGA generally don't support python, but along came Migen and Misoc and LiteX which support python by putting a cpu in the FPGA
- FuPy project is to run MicroPython on FPGA

flip flop operators in Ruby

- @merxplat
- flips b/w two statements
- its from perl, which got it from sed/awk, who got it from electronics
- being removed from ruby, no one uses it
- looks pretty handy and terse to me!

python in the classroom

- math teacher who now teaches python to kids in a low income area
- coding keeps kids engaged
- they use [grok learning](https://groklearning.com/)

DRF Model Pusher

- sends realtime updates using Pusher over websockets
- django stuff

Watching water from space

- [Claire](https://twitter.com/claire_science), climate scientist at Geoscience Australia
- works with agricultural data from space
- when are farm storage dams being filled and emptied
  - dams were manually labeleed on satellite photos before
  - now algorithim to detect dams, run automatically every time there is new imagery
  - they build a flagging system to alert for drainage
- working to improve this and pass it to stake holders

Captcha Cracker

- yr 12 student
- we have so much info to learn from, but programs have very limited info
- writing a program that uses the SIFT Algorithm to get through a ReCaptcha
- [see their website](https://captchacracker.wordpress.com/)

Rocketry

- MEMS is making things a lot cheaper
- used MEMS sensors with ESP32 to make lots of telemetry modules
- of course used micropython
- look up MQTT
- the feeling of something actually happening is awesome

cyrpto money

- bitcoin uses tons of electricity
- theft
- ethereum contracts cause software
- great overview of cycrptocurrencies

Peter Lovett

- teaches Python
- python is readable, everyone loves it for that
- pep505
- python needs to grow, but we don't want to loose sight of what we have

Giving thanks

- project to fund the packages you use: [phildini/thanks](https://github.com/phildini/thanks)

---

## Tracy Osborn: Clueless

> Tracy Osborn is the author, designer, and self-publisher of three books and the solo founder of a venture-backed startup. Each of these achievements has something in common — being completely clueless about the work and problems involved in each. In this keynote, Tracy will tell stories about how she launched her projects and what she learned (after already being neck-deep.) [#](https://2018.pycon-au.org/talks/tracy)

{{< youtube fOzJ-OIZRZw >}}

- [twtr](https://twitter.com/limedaring)
- wrote easy/friendnly [hello web app books](https://twitter.com/HelloWebBooks)
- unusual background to pycon. went through high school building websites.
- quit computer science in college cause bad experience, switched to art
- ended up working as a designer and web developer - design/html/css - scared of javascript
- learnt from cs experience how difficult it is to pick up programming and how important teaching styles are
- see her djangocon 2017 keynote
- wanted to do a startup, didn't want to code but couldn't find a technical cofounder
- husband works in python, introduced her to django. learnt django and launched her first webapp in 6 weeks
- you don't have to make things perfect, or understand how they work under the hood
- lessons learned:
  - barring security issues, ugly code can be ok
  - learn by doing - picked up programming much faster by having a real project to work on
  - startups are stressful but if you like to constantly be learning and doing something different most days they are great
- she didn't like the way django was taught, which is where her book came from
- customizable tutorials, project based - she teaches how to build a web app, not how to code
- wrote book instead of tutorial cause "go big or go home". low royalites with publishers, so used kickstarter to raise 12k to self publish.
- lessons learned:
  - keep marketing in mind when building a product
  - took way longer then planned - 1yr late. build a big buffer
  - keep it simple- instead of markdown etc, used google docs - very useful for edit help, or sending drafts to ppl
  - used indesign to lay out the book - used skillshare to pick it up.
- are paperback books worth it?
- easypost - api's for shipping

**my takeaway:** pick a simple project and just do it.


## Guide to your own artificial intelligence application in 3 easy steps

> What do you think of when you hear “artificial intelligence”? Perhaps self-driving cars, autonomous robots and Siri, Alexa or Google Home? But it doesn’t have to be that complex. You can build a powerful image classification model within a topic that inspires and interests you - with 3 easy steps. [#](https://2018.pycon-au.org/talks/45386-guide-to-your-own-artificial-intelligence-application-in-3-easy-steps/)

{{< youtube ymRr0AkMb5E >}}

- Norah Klintberg Sakal [ln](https://www.linkedin.com/in/norah-klintberg-sakal-5b81322a/) - data scientist doing a masters thesis at [Chan Zuckerberg Biohub](https://www.czbiohub.org/)
- [talk github, includes code](https://github.com/norahsakal/pyconau-2018-shades)
- ususally when u think of AI or DL u think of self driving cars, Alexa, cancer diagnosis
- but we can apply things to day to day problems
- Idea - Data - Training
- wanted to look at makeup tutorials, too many on the internet, so how do you know which one of the 30M videos is relevant ($400B industry)
- **Idea:** use deep learning to answer this
- **Data:** looked at videos, eye shapes jumped out - there are 4 distinct shapes
  - created dataset by looking at celeb images and cropping out eye shapes - 200 training, 100 validation
- **Train:** used transfer learning - pretrained weights from Imagenet (architecture VGG16)
  - there are a lot of models to choose from, used VGG-16 since its fairly simple to understand and easy to play around with
  - locked all the conv layers since they already knew how to understand images
  - using keras to grab VGG16 minus the top layer
  - got 93% accuracy
- **App:** Flask to take photo and predict image
- an important part of learning is to make something end to end. take a simple problem and make a app for it

**takeaway:** this was suprisingly easy for something which sounds so complex. build my own mini app using keras and flask

## Hello to the World in 8 Web Frameworks

> We’ll start with the current crop of microframeworks, showing how to achieve the same task in each, before progressing to “Batteries included” and then the more specialised async frameworks. For developers who perhaps have only used a single framework or even none at all, this talk gives them an opportunity to get out and explore the world (of web frameworks) and broaden their horizons, with plenty of Jules Verne inspired fun along the way. [#](https://2018.pycon-au.org/talks/45282-hello-to-the-world-in-8-web-frameworks-micro-batteries-included-async/)

{{< youtube z9Ek6fefMYk >}}

- Aaron Bassett [twtr](https://twitter.com/aaronbassett) dev advocate at Nexmo - an api company for telephony
- task: return a json string
- [Flask](http://flask.pocoo.org/) - uses functional based views (does support class views too)
- [cherrypy](https://cherrypy.org/) - uses class based views
- [falcon](https://falconframework.org/) - api first framework, designed to do json based microservices and be really fast 5x faster than flask, 10x django
- [hug](http://www.hug.rest/) - make development driven python apis as simple as possible - uses falcon under the hood, just adds a simplified interface to falcon.
- microframeworks make it very easy to do something simple, you also have the freedom to change things or bolt on whatever bits you want.
- but with great power comes great responsibility - you start with great intentions and end up building a monolithic app
- in real world situations your fantastic ORM isn't going to be usable by other ppl or well documented
- [Django](https://www.djangoproject.com) in the real world, every other project is essentially structured the same. which leads us to django, which is batteries included.
  - but its somewhat complex - basic project has a bunch of stuff, and for a basic api you end up with multiple files to deal with
  - prefers class based views, though some controversy there
- [Pyramid](https://trypyramid.com/) - start small - for basic stuff not much code, finish big - includes batteries if needed
- [Tornado](http://www.tornadoweb.org/en/stable/) - async framework, pretty small code
- [Sanic](https://sanic.readthedocs.io/en/latest/) - flask like async, but can't recommend it at the moment. prone to crashes and vulnerabilities

**my takeaway:** use any, ignore differences in syntax - whats important is documentation, bug/issue tracker activity, release management, community, and of course the scope of the project and the number of "batteries" you need. Don't end up rebuilding a bastardized undocumented django on top of a microframework, just use django if thats where you're headed.

## Functional Programming demystified

> Have you ever eavesdropped on FP developers talking about programming and wondered which planet you landed on? I attended LambdaJam 2018 and felt your pain! Let’s demystify Either, Semigroups, Monoids, Functors, Monads, Traversable, Natural transformations etc. by implementing them in Python. [#](https://2018.pycon-au.org/talks/45075-fp-demystified/)

{{< youtube p9_r36fIrqc >}}

- Eugene Van den Bulke - [twtr](https://twitter.com/3KWA)
- went to [lambdajam](https://lambdajam.yowconference.com.au/)
- [Eugenia Cheng](http://eugeniacheng.com/) - read her books
- Professor Frisby introduces functional programming in javascript - we are going to cover it in python
- Functor: something that can be mapped over.
- Currying: this makes no sense. instead of a func which takes in multiple arguments you have some weird chain of funcs which take in arguments one at a time
- Applicative functors: put a func in a box and apply to objects in other boxes
- Either Left of Right: basically a [flipfloperator](https://pypi.org/project/flipfloperator/)
- Monoid - ok now things are getting into the deep end

**my takeaway:** functional programming is interesting but deeply unpythonic. don't use unless there is a clear need to.


## You Don't Need That!

> Not every design pattern makes sense in Python. This talk builds up design patterns commonly used in enterprise languages, and shows the features in Python that make these approaches unnecessary. [#]((https://2018.pycon-au.org/talks/45184-you-dont-need-that/))

{{< youtube imW-trt0i9I >}}

- Christopher Neugebauer [twtr](https://twitter.com/chrisjrn) [web](https://chris.neugebauer.id.au/) works at AlpaSigts, Director of PSF
- Deisign Patterns let you express ideas that are hard to express... in a familiar way
  - most patterns are object oriented ones from the mid 90's, back when C and Java were the hot languages
- so how would design patterns be done pythonically?
- the simplest design pattern is a Singleton
- **Singleton:** a class that can only be constructed once
  - can use `del` to delete class definition after having called it once to make sure it never gets called again
- but why do we want a singleton? what do we want to achieve?
- back in the good old days Java needed singletons for namespaces, but python already has pretty good namespace seperation
- python can achieve this by using modules - so instead of classes we can have modules to hold data. Python makes sure you always get the same object regardless of how many times we import it.
- Modules are objects, so we don't need Singletons
- Dependency infection: provide dependecies to classes as constructor arguments (useful for unit testing)
- Mocks - pretend version of functions, most lanugages have mocking frameworks
- Unit Testing - `unittest.mock` has a patch function, so we don't need to write our own mock funcs
- Iterators - python provides `for` loops to consume iterators. But what are we trying to achieve? use `yield` to write generators for your own iterators
- perform a common operation on a collection - python does this natively with `for item in Class`
- python doesn't need Visitors becuase generators
- there are some design patterns which do make sense in python
- **Factories** - used all through the python library
- book on useful patterns in python: [python-patterns.guide](http://python-patterns.guide/)

**takeaway:** a lot of design patterns exist becuase they were needed in some language or other. (java, shudder). Use python's pythonic features, don't reach for older patterns unless its truly a good idea.

## There is no "now" and sensor data's the worst

> Audience members will be asked to go to a webpage on their phone that reads accelerometer data and transmits it to the presentation. This data will then be used to highlight the issues of collecting a processing data from distributed sensors - what happens when all the data is not received at once and not perfectly in time? what happens if there is an outage? How do you turn all this noise into something tha t can be managed? [#](https://2018.pycon-au.org/talks/45064-there-is-no-now-and-sensor-datas-the-worst/)

{{< youtube uv-KQzjA08c >}}

- Mike Leonard [twtr](https://twitter.com/mikerleonard) Reposit Power
- presentation demo fail - was hosted on kubernets cluster. Reminder that all this clustering business is hard.
- collecting IOT sensor data is hard - too small a polling interval will ddos your server, but too long means loosing out on realtime data.
- during an outage you want to keep data loss to a minimum - so log data on the device, but when they came back online you don't want to get ddos'd. so each time a device fails to transmit, it doubles the delay, also introduce some randomness so each device is sending data at different times
- realtime is tricky, scale is hard, distributed sensors are the worst
- python backend using Flask, Flask-SocketIO, React & Socket.IO + browser api
- recommends using [socket.io](https://socket.io/) over websockets - [python implementation](https://github.com/miguelgrinberg/python-socketio)

**takeaway:** think orchestration. how many devices, what when how do they log/send data and how to deal with loss/latency.

## Watch out for Safety Bandits!

> The presentation itself will go into the details of example security vulnerabilities, explain why it’s important to fix them, and show how integrating these two tools into your process will better protect you and your software. Beginners will get an appreciation for the kinds of security problems that can occur, and an introduction to continuous integration workflows. [#](https://2018.pycon-au.org/talks/43518-watch-out-for-safety-bandits/)

{{< youtube Wa2pgDihWaw >}}

- Tennessee Leeuwenburg [twtr](https://twitter.com/tleeuwenburg) Head of Secure Coding at the Australian Bureau of Meteorology.
- use python tools called [Safety](https://pyup.io/safety/) and  [Bandit](https://github.com/PyCQA/bandit)
- tools like [CVE](https://www.cvedetails.com/) track security vulnerabilities - there are heaps all the time in commonly used packages
- Safety tells you all the secure packages you are using using their [cli tool](https://pyup.io/safety/) or [hosted service](https://pyup.io/)
- some security vulnerablities are just "whoops I forgot to..."
- Bandit helps us with these problems - its a security linter which checks for common security issues in your code
  - very handy for going through code to find code smells
  - can put into code so it runs with CI and raises alerts
- the tools are noisy so you have understand what to pay attention to and what to tune out

**takeaway:** integrate Safety Bandits into CI.

## Sunday Lightening talks

{{< youtube rNkbmu4e3MA >}}

chunks() the story of a generator

- break an iterable into chunks of n - lots of implementations from stackoverflow
- `itertools.islice` slices iterators but returns an emptry iterator if gets an empty iterator
- code at [gist.github.com/timheap](https://gist.github.com/timheap/4e283fea7143e64852dcc09b14a183f7)

PyCon Anthology

- write a short story, art, poetry, pg-13, deadline Sep 1
- [submit through github](https://github.com/oboechick/pyfanfic)

Tracking trucks in Africa

- [Lori Systems](https://www.lorisystems.com/)
- tracks trucks, but how to do it best? truckers in Africa don't have reliable phones, handing out phones didn't really work
- Traccar - java based IOT gps tracking system for trucks
- Zappa is an alternative to celery

Software release reports with Python Sphinx & Jira

- Cochlear, heavily regulated, need a software release report: bugs fixed, improvements, known bugs
- used MS Word, so time to automate. Data in Jira, which has a python interface.
- python script gets info from Jira

why text encoding

- we need to encode text - so whats text encoding

phy py physics

- @cormacKikert
- A 3D physics sandbox game built using pygame
- cool demo - [code on github]9https://github.com/cormackikkert/Py-PHY)

Python Bugs

- first lightening talk

Bad code

- examples of over engineered code

Goto

- in yr10! doing a arduino assigment
- missed goto, wrote his own in python

Flip Flip Face Offerator

 - a flipfloperator faceoff

Micropython.. Jupyter.. Live

- micropython is re-inventing embedded development
- but theres no debugging in micropython
- can talk to micropython from jupyter, use interactive widgets
- look up jupyter-micropyton-remote - very impressive

Nick - core CPython dev

- talk about Peps which introduced now accepted features



