---
title: "PyCon Australia 2019"
date: 2019-08-02
tags:
- python
---

My notes for the [PyConAU 2019 talks](https://2019.pycon-au.org) I went to. This blog is an attempt to try and capture some useful info from the talks.

Future challange: Make a jupyter notebook for each talk to implement some of the learnings or tools or thingamajig learned.


## You don't always need NumPy

> The numerical Python ecosystem and communities are mature and powerful, but sometimes we can be too quick to reach for the numerical hammer when simpler options exist. This talk will outline some areas where the numerical stack may not be the best starting point, and survey some alternatives. [#]9https://2019.pycon-au.org/talks/you-dont-always-need-numpy)

- Sam Hames, software dev at QUT’s Digital Observatory.
- the numerical python stack is very complicated, and its a differnt idiom to the other types of python
- numpy is basically arrays and vectorized expressions on these arrays - but how to translate - for example using a dict to represent a bag of words `{'the': 21, 'bag': 2}` - its clear, there is a one to one mapping b/w word and its count - but using numpy arrays breaks that, you end up with two arrays like `[21,2]` and `['the', 'bag']`
- when writing numerical python, remember that the rest of python exists
- pythons built in data structures- lists, sets, dicts and tuples exist and are very very good - you can use them in many applications instead of numpy!
  - depending on the task, sometimes you need that numpy speed for certain ops
- lists - appends are fast, you can have dicts of lists
- sets - adding, deleting and checking membership are all fast
- tuples - work very well for things like metadata description, and you can have a set of tuples (you can't have a set of lists)
- combining python data structures is easier to understand
- the stdlib has lots of things built in:
  - collections:
    - defaultdict can simplify code
    - Counter - count all the things
  - heapq
  - bisect
- Generators and streaming - you will run out of memory at some point
  - example `pandas.read_csv` is used a lot but it fits the whole file into memory - instead you can read a file line by line by using
  -
  
```python
with open('very_big_file.txt', 'r') as f:
  for line in f:
    results = (do_something(line) for line in f)
```

- maybe don't do everything in python, use a database?
  - sqlite can do a lot of stuff, example compute and store a bag of words
- there are lots of domain specific databases, both local and hosted, and they can be a great complement to a python stack
  - this way you only have to worry about a subset of the original python
- look for task specific libs

**takeaway:** document all the numerical things, and don't be afraid to mix and match. Whats the actual problem you're solving - does it matter if its taking 1ms in numpy vs 5ms in python?



## Flying by the seat of our pants - our journey of teaching python using drones

> A few years ago we found ourselves teaching students everything from Python to Arduino. It was our plan to replace all the other languages with Python as we streamlined our course. Learn why we introduced drones, what we learned not to do and what we were surprised about. [#](https://2019.pycon-au.org/talks/flying-by-the-seat-of-our-pants--our-journey-of-teaching-python-using-drones)


- Kylie Mathers - teacher at Marymount catholic school in Qld
- the school used a veritable kitchen sink of languages, wanted to switch to one language, preferrably open source, which was useful after students left school and worked with prototyping electronics (beeps and leds makes kids heads light up)
- some considerations:
  - block based programming is too..ugh
  - Apple swift and playgrounds need ipads, those are expensive and lock you in
  - they had drones, wanted to use them, and guess what, you have [libs like pyparrot](https://github.com/amymcgovern/pyparrot) to program drones in python
- drumroll.... they choose python!
- the talk covered introducing students to the big picture concept of drones, their issues and applications and things to think about
- so after ages, the students finally went hands on with python and drones
  - used psuedo code, flowcharts to explain concepts
  - then real code, including functions like `make_it_rock`, `circle` etc etc
  - seeing the drone do stuff in real life becuase of their code was very motivating
- highly visible learning is great.

**takeaway:** theres a lot to research and think about before even starting to code and fly a drone. I guess that applies to programing in general - so much problems in python are best approached after a literature research for best practices.

Highly visibile reactions are great, so try and use that with real projects as well.

## Using Dash by Plotly for Interactive Visualisation of Crime Data

> [Dash](https://plot.ly/dash/) is a great Python framework for building data visualisation websites. In this talk I discuss the framework basics, explore a sample site and describe its use for an enterprise application to graph crime statistics. I finish with clear pros and cons of the Dash framework from our perspective. [#](https://2019.pycon-au.org/talks/using-dash-by-plotly-for-interactive-visualisation-of-crime-data)

- [Leo Broska](https://www.linkedin.com/in/leobroska) [github](https://github.com/halloleo), software dev at ACIS, works with criminal data
- with any numerical data, eventually you have to put it into a graph or dashboard
- Dash is a python framework for building analytical websites, with no javascript required
- [dash example apps:](https://dash-gallery.plotly.host/Portal/)
- plotly does all the drawing and charts in dash, and react powers the interactivity layer for dash, flask actually delivers the webapp - every dash site is a flask app
  - there is not need to call the internal components of dash for simple things
- Make a simple dash app:
  - import your data, make a figure object which graphs/maps it using plotly express. use `fig.update_traces` to tweak the fig object.
  - then make a dash app, give it a layout - this defines what the app is serving, which is typically html or markdown text and the plot objects created earlier
  - now run the app!
- Note: use a server like gunicorn for production
- dash is great but some issues:
  - slow, rendering is slow, underlying javascript code very big
  - multi-page sites awkward to code

**takeaway:** Just tried out plotly on my laptop, and it is a bit slow. Use it with caution as needed. It looks great for internal dashboard where you have beefy machines and fast connections to users, for personal use to dump on the internet a dash app is a hefty thing to host.


## Building, designing, teaching and training simulation environments for Machine Learning

> Imagine you’re building a fancy robot-driven warehouse. Your pick, place, and packing robots need to get around quickly, find the right item and put it to the right place without colliding with each other, shelves, or people. But you don’t have any robots yet, and you need to start. Try simulations! [#](https://2019.pycon-au.org/talks/building-designing-teaching-and-training-simulation-environments-for-machine-learning)


- Paris Buttfield-Addison, professional game dev and ml fan
-

**takeaway:**

## Forecasting Australia's 2019 Election with PyMC3

> Can we predict the result of an Australian election before it occurs? How certain of the outcome can we be? My talk will use the 2019 Australian federal election as a case study to provide an entry-level introduction to the benefits of probabilistic forecasting and PyMC3. [#](https://2019.pycon-au.org/talks/forecasting-australias-2019-election-with-pymc3)


-
- Martin Burgess
-

## Understanding GPUs

> With torch and tensorflow we have begun to rely on GPUs to speed up computations. Deep Learning or not, GPUs can provide massive computation speed ups but it’s not a panacea as NVIDIA would have you believe. Understanding how GPUs work can tell us where we should and shouldn’t use them. [#](https://2019.pycon-au.org/talks/understanding-gpus)


- Varun Nayyar





Note: Choose b/w the following two:


## Education Seminar Student Showcase

> Eight short talks from high school students across Australia. They’ll be talking about projects they’ve built with Python using machine learning, robotics, markov models and more! [#](https://2019.pycon-au.org/education-showcase)

## Not a long time ago, in a galaxy not very far away, an astronomer and a computer scientist walk into a bar...

> Python is one of the most popular programming languages in astronomy. In this talk, I will tell a story about how Python helped me to develop a software tool for galaxy modelling, and tackle the scientific and technical challenges that arise in the Big Data era of astronomy. [#](https://2019.pycon-au.org/talks/not-a-long-time-ago-in-a-galaxy-not-very-far-away-an-astronomer-and-a-computer-scientist-walk-into-a-bar)

- Georgios Bekiaris
-

## Learn to control your brain: Brain Computer Interfacing with Python

> Neurofeedback is a brain-computer interface where a person’s own brain waves are audio/visually presented back in real-time after they’ve been recorded and filtered within a few milliseconds. We present methods to allow people to see their own brainwaves with python. [#](https://2019.pycon-au.org/talks/learn-to-control-your-brain-brain-computer-interfacing-with-python)

- Johan van der Meer, neuroscientist at the QIMR Berghofer Medical Research Institute in Australia. [github](https://github.com/jnvandermeer)
-

## Machine Learning and Cyber Security - Detecting malicious URLs in the haystack

> Today, security teams are in an increasingly one-sided battle to defend against a myriad of cyber attacks. Web-based attacks are often devastating, with conventional blacklists and reputation-based defence tactics not able to identify previously unseen malicious URLs. Is AI the solution? [#](https://2019.pycon-au.org/talks/machine-learning-and-cyber-security--detecting-malicious-urls-in-the-haystack)


## First-timers Session



## Creating Lasting Change

> The Nature of Organisations, People, and how to Change Them [#](https://2019.pycon-au.org/talks/aurynn)

- Aurynn Shaw [@aurynn](https://twitter.com/aurynn)
-

## Data scientists and Anthropologists - Unlikely BFFs?

> The growing availability of large datasets and powerful analytical tools is creating both methodological and ethical issues for data scientists in the academy and industry alike. Qualitative methods, developed in the social sciences, offer data scientists a new toolbox to apply to these challenges. [#](https://2019.pycon-au.org/talks/data-scientists-and-anthropologists--unlikely-bffs)

- Fiona Tweedie
-

## Tunnel Snakes Rule! Bringing the many worlds of Python together to monitor Melbourne's biggest infrastructure project.

> Python is being used to provide real-time environmental monitoring on the Melbourne Metro Tunnel project. Come along to see how open source Python tools from the web, IoT, cloud infrastructure and scientific domains are being used together to monitor environmental telemetry on a city-wide scale. [#](https://2019.pycon-au.org/talks/tunnel-snakes-rule-bringing-the-many-worlds-of-python-together-to-monitor-melbournes-biggest-infrastructure-project)

- Evan Brumley, senior dev at WSP Digital

## Using python-programmed microcontrollers to build comedy props

> Early-career comedians often have difficulties adding electronic props to their acts, due to the high cost of materials and fabrication skills required. This talk will recreate several props used in comedic performances, showing the code and components used. [#](https://2019.pycon-au.org/talks/using-python-programmed-microcontrollers-to-build-comedy-props)

- Anthony Joseph & Debbie Zukerman
-

## Python Applications in Infrastructure Planning and Civil Engineering

> Engineers tasked with planning new infrastructure constantly face the problem of having to look through too much information. This talk is about how we wanted to be lazy and wrote a bot to do it for us instead. [#](https://2019.pycon-au.org/talks/python-applications-in-infrastructure-planning-and-civil-engineering)

- Ben Chu, grad engr at WSP
-

## Thinking about thinking about computers

> Let’s talk about computers: I don’t know how they work, but when I’m writing code I can imagine what it will do. I can think through, at length, what will happen at each step. So what’s the deal with that? I reckon it’s time to think about thinking about computers. [#](https://2019.pycon-au.org/talks/thinking-about-thinking-about-computers)

- Ben Taylor, dev at Grok Learning

## Profiling Pathogens with (micro) Python

> We’re building professional medical diagnostics equipment with micropython. This has come with minimal challenges, many positives and a few surprises! [#](https://2019.pycon-au.org/talks/profiling-athogens-with-micro-python)

- Andrew Leech

## The Antipodes

> ?? [#](https://2019.pycon-au.org/talks/brandon)

- [@brandonrhodes](https://twitter.com/brandonrhodes)
-

## Saturday Lightning Talks


# Sunday

## The real costs of Open Source Sustainability

> What if money isn’t the only way to create sustainable free and open source software projects? What if it turns out that sustainability is actually a multi-faceted concept that can’t truly be successful if people focus on only one of its many elements? [#](https://2019.pycon-au.org/talks/vicky)

- VM Brasseu [@vmbrasseur](https://twitter.com/vmbrasseur)


## Shipping your first Python package and automating future publishing

> One of the best things about Python is the vast ecosystem of packages available on the Python Package Index. Shipping your first Python package can be intimidating. This talk aims to remove the mystery of Python packaging and enable you to share your code with the Python community. [#](https://2019.pycon-au.org/talks/shipping-your-first-python-package-and-automating-future-publishing)

- Chris Wilcox, dev at Google
-

## Insights into Social Media Data using Entropy Theory

> Entropy theory is usually thought of as something that applies to matter and energy, but it turns out that we can apply the same techniques of analysis to social media sites. Join me as we study the thermodynamic behaviour of users on Twitter, and learn how to analyse it better. [#](https://2019.pycon-au.org/talks/insights-into-social-media-data-using-entropy-theory)

- Mars Geldard
-

## It's dark and my lights aren't working (an asyncio success story)

> I have invested huge amounts of time in achieving a simple goal – making the lighting in my home “smart”. It’s not ground breaking, nor is it practical or cost effective, but it sure was educational, uses a bunch of Python, and the result makes me (and my family) happy. [#](https://2019.pycon-au.org/talks/its-dark-and-my-lights-arent-working-an-asyncio-success-story)

- Jim Mussared
-


## The universe as balls and springs: molecular dynamics in Python

> Surprisingly, we can approximate matter as a bunch of balls on springs and learn things about our bodies and the world. This talk will look at the different stages of molecular dynamics (MD) simulations and how Python is changing everything. [#](https://2019.pycon-au.org/talks/the-universe-as-balls-and-springs-molecular-dynamics-in-python)

- Lily Wang, working on PhD on molecular dynamics at ANU
-

## Instant-feedback, instant-debugging Python coding

> Building on Bret Victor’s famous ‘Inventing on Principle’ presentation, we look at writing Python where the code is instantly run and every line visualized after every single keystroke. There’s a future beyond the text-editor -> console-run loop and this is a taste of it. [#](https://2019.pycon-au.org/talks/instant-feedback-instant-debugging-python-coding)

- Robert Lechte
-


## Volumetric Performance Capture and Playback: A Workflow with Python

> Volumetric capture is a technique used to film in three dimensions for viewing in a virtual space.This talk will explore the different elements of a full volumetric capture stack, from coordinating usb cameras to playback in a 3D game engine and how python can be used to glue it all together. [#](https://2019.pycon-au.org/talks/volumetric-performance-capture-and-playback-a-workflow-with-python)

- Luke Miller
-

## Sunday Lightning Talks


## notes

- Embed youtube vidoes by `{{< youtube EqQj5os3Mfw >}}` or `{{< youtube id="w7Ft2ymGmfc" autoplay="false" >}}`