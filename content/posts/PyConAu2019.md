---
title: "PyCon Australia 2019"
date: 2019-08-03
tags:
- python
---

My notes for the [PyConAU 2019 talks](https://2019.pycon-au.org) I went to. This blog is an attempt to try and capture some useful info from the talks.

Future challange: Make a jupyter notebook for each talk to implement some of the learnings or tools or thingamajig learned.

The [pyconAU19 videos](https://www.youtube.com/playlist?list=PLs4CJRBY5F1LKqauI3V4E_xflt6Gow611) are up on youtube.


## You don't always need NumPy

> The numerical Python ecosystem and communities are mature and powerful, but sometimes we can be too quick to reach for the numerical hammer when simpler options exist. This talk will outline some areas where the numerical stack may not be the best starting point, and survey some alternatives. [#](https://2019.pycon-au.org/talks/you-dont-always-need-numpy)

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


- Paris Buttfield-Addison, Phd in CS, professional game dev and ml fan
- Unity isn't open source but is free
- [Unity Machine Learning Agents Toolkit (ML-Agents)](https://github.com/Unity-Technologies/ml-agents) - use python to connect to unity for using it as a training environment
- blog post explaining the talk is up at his [website](https://hey.paris)
- unity can be programmed using blocks, its very friendly, so don't get scared

**takeaway:** Unity is easy to use, try it out with python!

## Forecasting Australia's 2019 Election with PyMC3

> Can we predict the result of an Australian election before it occurs? How certain of the outcome can we be? My talk will use the 2019 Australian federal election as a case study to provide an entry-level introduction to the benefits of probabilistic forecasting and PyMC3. [#](https://2019.pycon-au.org/talks/forecasting-australias-2019-election-with-pymc3)

- Martin Burgess, [github](https://github.com/martintburgess) [buckleysandnone](https://www.buckleysandnone.com)
- [notebook for talk, includes slides and code](https://github.com/martintburgess/buckleys-pycon2019/blob/public/notebooks/Forecasting%20Australia's%202019%20Election%20with%20PyMC3.ipynb)
- prob forecasting tries to estimate te relative prob of all possible outcomes e.g weather forecasting
- the future is uncertain, and prob forecasting gives us an estimate of how likely different outcomes are
- ppl have different starting assumptions, probabilistic forecasting defines them up front
- [PyMC3](https://docs.pymc.io)

**takeaway**: forecasts with probabilities are much more useful than just a plain number. With the last Australian elections, practically every channel had just the one number for wins - but if they had attaced a likeihood to it and shown the other likely scenarios it would have been a lot more useful.

Apply probabilistic forecasting to a future issue. Read [this book](https://nostarch.com/learnbayes) and [ThinkBayes](https://greenteapress.com/wp/think-bayes/).
 
## cuDF: RAPIDS GPU-Accelerated Dataframe Library

> RAPIDS open-source software enables end-to-end data science and analytics pipelines to run entirely on GPUs. Key to RAPIDS is cuDF, a pandas-like Python data frame library with a high-performance CUDA C++ implementation. cuDF and RAPIDS enable large speedups for end-to-end data science using GPUs. [#](https://2019.pycon-au.org/talks/cudf-rapids-gpu-accelerated-dataframe-library)

- Mark Harris, engr at [rapids](https://rapids.ai).
- moving and transforming data is slow
- data processing evolution for query, ETL and ML train steps:
  - hadoop would read and write data to disk at every step
  - apache spark kept data in memory all the time
  - traditional gpu processing would read data into gp, do something then write to cpu. a lot of gpu speed gains were lost in the read write steps
  - apache arrow provides a common in memory data format so different tools can use the same format and save the data conversion steps
  - rapids uses arrow to skip many of the data conversion steps, much faster
- rapids aims to accelerate existing python tools, like the pydata chain
- the average data scientist spends 90% of their time in ETL
- enter cdDF: rapids dataframes to save the day by drastically speeding up ETL
  - runs on libcuDF, a low level CUDA C++ lib which does all the work on the GPU
  - cuDF provides a pandas like api, creates gpu dataframes from numpy arrays, pandas dataframes or pyarrow tables
  - bridges python (a dynamic language) with C++ & Cuda (static languages)
  - gpu accelerated i/o - 10x faster than pandas
- rapids speeds up workflows on a single pc with one gpu - for bigger data it works with dask for distributed computing
- cuML algorithms are largely compatible with sklearn, just much faster
  - 1 v100 gpu is 5-100x faster than 2x20 core cpu.
  - a regular desktop gpu is plenty fast too for a normal user
- Rapids works in Google Colab, see [getting started](https://rapids.ai/start.html).

**takeaway:** should drastically speed up many of the bigger datasets I've tried in pandas, where a clean and transform pipeline would take many minutes. cuDF promises to at drastically speed up this process, making it easier to iterate faster.

So look into getting a Nvidia powered computer suitable for using with rapids, this would have drastically sped up some of my machine learning projects.

## Understanding GPUs

> With torch and tensorflow we have begun to rely on GPUs to speed up computations. Deep Learning or not, GPUs can provide massive computation speed ups but it’s not a panacea as NVIDIA would have you believe. Understanding how GPUs work can tell us where we should and shouldn’t use them. [#](https://2019.pycon-au.org/talks/understanding-gpus)


- Varun Nayyar, mathematician - [linkedin](https://www.linkedin.com/in/varun-nayyar-94222647/?originalSubdomain=au)
- what are GPU's good for? graphics can be fundamentally reduced to matrix operations, DL is just matrix multiplication with a non linearity.
- CUDA: gpu's are made up of streaming multiprocessors (SM's) each with many cuda cores, say 64-128. They run thousands of threads simultanesouly vs 10s for a cpu.
- real world cuda threads are divided into blocks of 32 threads called a warp, and threads in a warp run at the same time.
  - a rtx2080ti can run over 4K threads in one go
- GPU's are generally memory bound, not compute bound.
- Deep learning: each forward pass is just a matrix multiply, as is backprop
- Gradient Descent is a sequential algorithim - gpu compute hasn't changed how it works, just makes it faster by 20-30x on a fully connected network.
- Convolutions are compute bound on a gpu, easy to parralize
- RNN's are memory bound
- gpu's work well with GradientBoosting
- gpu's have variable perf depending on the algo, so its not straigtforward to put algorithms on the gpu. CPU and GPU implementations can differ.
- gpu sync is slow - stick with single gpu's for personal use, you need a strong engineering team for multi-gpus.
- local compute is great - pays for itself soon over paying for cloud. don't skimp - go for a rtx2080ti

**takeaways:** very impressive talk. Worth rewatching if doing something with GPU's. For my next ML project consider getting my own gpu box running linux and look at libraries like rapids.


## Not a long time ago, in a galaxy not very far away, an astronomer and a computer scientist walk into a bar...

> Python is one of the most popular programming languages in astronomy. In this talk, I will tell a story about how Python helped me to develop a software tool for galaxy modelling, and tackle the scientific and technical challenges that arise in the Big Data era of astronomy. [#](https://2019.pycon-au.org/talks/not-a-long-time-ago-in-a-galaxy-not-very-far-away-an-astronomer-and-a-computer-scientist-walk-into-a-bar)

- [Georgios Bekiaris](https://www.linkedin.com/in/bekos/), astrocoder, makes software for astronomy
- wrote gbkfit - tool for galaxy kinematic modelling
  - initially in c++, rewrote twice, finally rewrote in python
- galaxy kinematics refers to the motions of stars, clouds of gas
- doppler effect: approaching: higher freq, receding: lower freq
- kinematics combines spectroscopy with doppler effects
- see talk...
- commonly used libs: [Astropy](https://www.astropy.org), scipy and matplotlib.
- numpy code ran as fast or faster as c++ on a single cpu. [numba](https://numba.pydata.org) makes it easy to speed up python code by applying a numba decorator to a function. Also supports gpus.

**takeaway:** Astronomers are using python for everything, and python can be fast with the right tools.

## Learn to control your brain: Brain Computer Interfacing with Python

> Neurofeedback is a brain-computer interface where a person’s own brain waves are audio/visually presented back in real-time after they’ve been recorded and filtered within a few milliseconds. We present methods to allow people to see their own brainwaves with python. [#](https://2019.pycon-au.org/talks/learn-to-control-your-brain-brain-computer-interfacing-with-python)

- Johan van der Meer, neuroscientist at the QIMR Berghofer Medical Research Institute in Australia. [github](https://github.com/jnvandermeer)
- basics: grab signals from the brainusing EEG, do real time analysis, send a feedback signal
- brain has many neurons, when a neuron fires a electrical field is generated which is pretty tiny - but when many neurons fire together it makes a big field which you can measure from even outside the brain
 - signal changes with action - exampls eyes open/close.
 - eeg resolution is quite poor/limited
 - EEG signals can have rythyms, so thus you can do frequency analysis
- [mne](https://martinos.org/mne/stable/index.html) - open source python lib for neurophysical data
- for better signals - you have to measure from inside the brain - see neuralink.
- eeg is non-invasive, portable and cheap
- [labstreaminglayer](https://github.com/sccn/labstreaminglayer) is a good library to stream realtime data from a measuring device.
- so we have devices, we have libararies to connect to them and python to glue it all up.
- Decoding all this data: this is where the research is, figuring out what it means and using it do useful things, like control a wheelchair etc.
- [neurofeedback](https://www.wikiwand.com/en/Neurofeedback) learning: with some mental disorders ppl have irregular brain rythyms. Idea is that regularzing them with "training" will help improve disorders.
- Encoding: how much data can we transmit?
- [openbci](https://openbci.com) looks really cool.

**takeaway:** lots of interesting work being done. Interesting thing is that the neural data is pretty straightforward, no wonder teenagers are building brain controlled prosthetic arms these days!

Explore openbci further and hack my own neuro thingamajig.


## Machine Learning and Cyber Security - Detecting malicious URLs in the haystack

> Today, security teams are in an increasingly one-sided battle to defend against a myriad of cyber attacks. Web-based attacks are often devastating, with conventional blacklists and reputation-based defence tactics not able to identify previously unseen malicious URLs. Is AI the solution? [#](https://2019.pycon-au.org/talks/machine-learning-and-cyber-security--detecting-malicious-urls-in-the-haystack)

- design thinking: put yourself into the shoes of your user at the start of a project
  - Know your user, understand their pain points and what they do
  - Nail the problem
  - Ideas
  - Know the threat
  - python - data, engr features, model/eval
- did a lot of feature engineering on the urls, things like getting whois data, domain expiry dates, location info, etc etc.
- they used fast.ai for deep learning, sklearn for randomforests and tensorflow for word embeddings
- used F1 score to evaluate models

**takeaway:** see the presentation again... it was a good explaination of a end to end process.

## Creating Lasting Change

> The Nature of Organisations, People, and how to Change Them [#](https://2019.pycon-au.org/talks/aurynn)

- Aurynn Shaw [@aurynn](https://twitter.com/aurynn), devops at Eiora
- talk is about introducing change
- spoke about [Contempt culture](https://www.google.com.au/search?q=contempt+culture) in the tech world
  - what has pervasive hostility done in tech jobs?
- all new tech exists in a business context, and biz don't care about technologies. Devs care about tech, not businesses.
  - biz cares about outcomes - can i deploy it, can i find ppl to work on it and the other things biz needs to care about
- expressing opinions in contemptuous terms gets you sidelined and not trusted
  - you diss one tech, like another tech - makes you look biased
  - we have done this to ourselves.
- if they think its necessary and we don't or vice versa its not them at fault there is a communications gap.
- and thus we end up in a process which doesn't believe in engineers.
  - we should not be speaking only in a language of tech and treat our assumptions as better - we need to speak in the language of biz
- processes and status quos arise from past biz experiences
- the cloud is where infrastructure as code become real - 13 yrs ago. Some companies are still having conversations about entering the cloud. Cause they don't care about the tech and ease of the cloud, they care about risks and costs and regulations and so on.. the easy of spinning up services is a small thing.
 - someone needs to communicate that
- power dynamics dictate change
- listening is key to change
- new processes need to make the lives of others betters and show them how its solving problems (and in the process you get to roll out the shiny new tech you care about)
- all technology is political - tech encodes the structures of the org which made it
  - things which make no sense often are because of the initial org constraints, and thats why they don't make sense to a different org with different constraints
  - understand the political ramifications of tech
- go and talk to ppl. make conversations safe.
  - good example of Etsy
- learn to speak business. Be empathetic to the entire org.

**takeaways:** Its not just them, its us. Solve business problems and communicate how your solution helps. Don't spend too much time on _we should have done it right in the first place._ It just so happens that we adopt new tech as sometimes its better/faster/cheaper than the old.
  
## Lessons learned building Python microservices

> I will talk about challenges and wins that have come from introducing Python into a multilingual microservices kubernetes architecture with lots of legacy. [#](https://2019.pycon-au.org/talks/lessons-learned-building-python-microservices)

- Richard Jones, dev at [reecetech](http://www.reecetech.com.au), a plumbing company
-
- trys to make every service look similar, tools to enforce this
  - cookiecutter
  - tox
  - goal is full test coverage, pytest cause its best in class
  - black to format code
  - pycharm for all devs so ppl can help other ppl easily without editor shock and for ease of pair programming
  - [pactman](https://pypi.org/project/pactman/) for contract testing of services
  - django to deliver the services
- inconsistencies happen, so you have to check across teams. i.e one team switched tool cause they found it too hard, so now you have inconsistencies across projects
- resilience: microservices are prone to brief errors or tiny service interruptions. So use http retries for some errors
- moniter services using [grafana dashboards](https://grafana.com) and [kibana](https://www.elastic.co/products/kibana) for monitering and searching logs
- get it running right first, then use tools to investigate performance, like [silk](https://github.com/jazzband/django-silk) for dango
  - reducing number of sql queries was key to speed
- batch interfaces is good, like allow consumer to get 100 price requests in one go, much faster than 100 different requests
- caching really helped. `@lru_cache(maxsize=1024)` decorator built into python does the job.

**takeaway:** make things simpler by taking away choices by using automated tools. Test and monitor services.

## Tunnel Snakes Rule! Bringing the many worlds of Python together to monitor Melbourne's biggest infrastructure project.

> Python is being used to provide real-time environmental monitoring on the Melbourne Metro Tunnel project. Come along to see how open source Python tools from the web, IoT, cloud infrastructure and scientific domains are being used together to monitor environmental telemetry on a city-wide scale. [#](https://2019.pycon-au.org/talks/tunnel-snakes-rule-bringing-the-many-worlds-of-python-together-to-monitor-melbournes-biggest-infrastructure-project)

- [Evan Brumley](https://www.linkedin.com/in/evanbrumley/), engr at [WSP Digital](https://www.wspdigital.com)
- working on 7 construction sites for Melbourne Metro
- one construction site next to hospitals, lab etc which can't be disturbed - so they have a bunch of quantative requirements to meet and report on in real time.
- so, how to keep track of all the requirements?
- old school approach was to send grad engineers to site, collect readings, analyze in excel and file reports at the end of the month
- modern approach: get sensors from a Vendor with a Saas platform, give them lots of money, download csvs, analyzie in excel and file reports at the end of the month.
  - they don't respond to custom reports, don't integrate with other vendors sensors
- solution: build a new platform which could accept data from any device
- hint: try not to work with devices directly
- 150-200 sensors, some sending data at a half second freq
- validate and store telemetry
- envirnomental requirements don't map directly to sensor data, so calculations needed to transform them - which are sometimes complex, and have to performed in real time
- access to data - both internal as well as limited external access
- alerts and reporting
- they had 4 months to build this out, fully self contained team of 2-3 devs + 1PM
- [AWS Kinesis](https://aws.amazon.com/kinesis/) to store streaming data, S3 for resilient storage, then influxdb.
- api pollers packaged into docker containers and deployed via elastic beanstalk
  - used [pyftpdlib](https://github.com/giampaolo/pyftpdlib)
- web app is built on django+celery+react, powered by pandas and the scipy stack
  - pandas allows them to transform raw telemetrym live, on request - using upto 10K points in a dataframe. Pandas was a huge timesaver.

**takeaway:** dang. that is a lot of stuff.

## Using python-programmed microcontrollers to build comedy props

> Early-career comedians often have difficulties adding electronic props to their acts, due to the high cost of materials and fabrication skills required. This talk will recreate several props used in comedic performances, showing the code and components used. [#](https://2019.pycon-au.org/talks/using-python-programmed-microcontrollers-to-build-comedy-props)

- Anthony Joseph & Debbie Zukerman
- used adafruit wearable devices, [circuit playground](https://learn.adafruit.com/introducing-circuit-playground/overview), microbit, arduino
- qlab

**takeaway:** explore micropython and get a device to play with.

## Python Applications in Infrastructure Planning and Civil Engineering

> Engineers tasked with planning new infrastructure constantly face the problem of having to look through too much information. This talk is about how we wanted to be lazy and wrote a bot to do it for us instead. [#](https://2019.pycon-au.org/talks/python-applications-in-infrastructure-planning-and-civil-engineering)

- Ben Chu, grad engr at [WSP](https://www.wsp.com/en-AU), a large engnr firm
- lots of stuff involved in railway planning
- EIA used to be done by junior staff, using datasets like noise receivers (hospitals etc), vegetation (what areas will the train cross)
  - these add up quickly to a lot of stuff
- so instead they are using jupyter notebook
  - shapefiles store shapes like the railway line and vegetation and noise senstitive areas
  - run in [Papermill](https://github.com/nteract/papermill which outputs html, csv and shapefiles
- need to check DA's along the railway line which might impact on the line - there can be many thousands.
  - used to be done manually, paid $70 per DA, slow, costly and infrequent updates
  - they need to know as soon as the DA comes in as it could pose a high risk to the railway design
- DABot automates this - it merges geocoded national address file and lot shape datasets, filters for lots on the buffer alighnment, which gives a list of addressses which they can use to search for DA's matching those addresses.
  - majority of council websites are the same, so same scraper works on most of them
  - NLP pipeline to clean text, then they form a document term matrix, used 200 most imp features
  - ML: went with XGBoost, got 85% Accuracy with a 95% recall
    - maximized recall as they didn't want to miss high risk DA's
- DABot allowed for frequent updates, saved time/money
- Future: lots of improvements to do, from using word embeddings, deep learning,
  - PostGIS database
  - fully automated pipeline so they can send out automated weekly reports

**takeaway:** Impressive how a very simple NLP pipeline and application of XGBoost gave them such good usable results. They didn't even use word embeddings! There is a lesson in this. Build simple, improve later.

## Fantastic Blocks And Where To Hide Them

> Ruby has blocks. JavaScript has blocks. Swift has blocks. Python doesn’t have blocks.In this talk, we’ll look at why Python doesn’t have blocks, and recent programming techniques that have developed in languages that do have blocks. Then we’ll look at what we – or Python – can do about it! [#](https://2019.pycon-au.org/talks/fantastic-blocks-and-where-to-hide-them)

- Christopher Neugebauer, [@chrisjrn](https://twitter.com/chrisjrn), snr engr at [AlphaSights](https://www.alphasights.com) and a director of PSF
- blocks was last discussed in 2005 for Python, and is unlikely to appear
- using Kotlin at AlphaSights - Kotlin encourages passing blocks of code around
- Python isn't really for functional programming, instead they have list comprehension
- Blocks: in python you can have a func (many lines) or a lambda (one line long)
  - so you always need to define a func and pass that. In other languages you can easily pass a block of code
- Context Managers: when opening files, you had to manually close them. Easy to miss. Hence context managers.
  - the python syntax enforced correct behaviour

**takeaway:** things to thing about. Convention matters.

## Profiling Pathogens with (micro) Python

> We’re building professional medical diagnostics equipment with micropython. This has come with minimal challenges, many positives and a few surprises! [#](https://2019.pycon-au.org/talks/profiling-athogens-with-micro-python)

- Andrew Leech, [Planet Innovation](https://planetinnovation.com)
- working with [Lumos](https://lumosdiagnostics.com) to develop point of care diagnositcs tests (spinoff of PI)
- Buid a medical device:
  - hazard and risk based development: at every stage minimise risks
- Lumos Camera Reader runs micropython, connects to a phone via bluetooth
- SOuP: Software of unknown povidence
  - for medical devices, you need certified code, or blackbox it.
- use jupytermicropython kernel to run code directly on the board. Makes dev very easy.
  - use ipywidgets to do live interactions.
- use test driven development - the same unittest can run on the board, desktop and CI
- medical devices aren't that different from regular devices, they just need to blackbox all the uncertified bits.
  
**takeaway:** use the jupyter kernel for micropython for live dev on a board.

## The Antipodes

- [@brandonrhodes](https://twitter.com/brandonrhodes), [#](https://2019.pycon-au.org/talks/brandon)
-

## Saturday Lightning Talks


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
