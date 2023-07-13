---
date: 2023-03-02
tags:
  - python
toc: true
---

Some notes on getting data out of a Peloton Cycle.

The MVP, in a jupyter notebook:
- getting out a few different users rides
- figuring out days since last ride

The project:
- displaying them on a raspberry pi pico 2, cycling through users 
- display a emoji depending on days lapsed since last tide

Improvements:
* Crunch all rides in the last week or month and display an effort number
* a simple graph? 


There doesn't seem to be a officlal API, but there is an [unofficial API](https://app.swaggerhub.com/apis/DovOps/peloton-unofficial-api/0.3.1) and a recently updated python wrapper called [pelotoncycle](https://github.com/justmedude/pylotoncycle) which does exactly what I need: 

```python
import pylotoncycle

username = 'your username or email address'
password = 'your password'
conn = pylotoncycle.PylotonCycle(username, password)
workouts = conn.GetRecentWorkouts(5)
```


## Raspbery Pi Pico W

https://github.com/paulober/Pico-W-Go

Weather API for AU:
https://www.willyweather.com.au/api/register.html

Free API

https://pirateweather.net/ - https://pirateweather.net/apis
see it in action here:
https://merrysky.net/


## Future

A limitation of this wrapper is that it only returns the logged in users rides, I want to be able to get the recent rides of the ppl I'm following. This data is visible to me, so the API probably exposes this too. 