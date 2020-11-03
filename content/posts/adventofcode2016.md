---
title: "Advent of Code 2016"
date: 2018-07-10T01:21:48Z
tags:
- python
---

Notes for the [Advent of Code 2016](http://adventofcode.com/2016) programming challange.

> Advent of Code is a series of small programming puzzles for a variety of skill levels. They are self-contained and are just as appropriate for an expert who wants to stay sharp as they are for a beginner who is just learning to code. Each puzzle calls upon different skills and has two parts that build on a theme.

I solved each puzzle in a [jupyter notebook for each day saved in a github repo](https://github.com/khalido/adventofcode/tree/master/advent2016). The solutions are all a bit verbose as I'm trying to show all the steps taken to solve the puzzles.

## General takeaways from 2016's advent of code:

- regex's can make hard things easy at the cost of the regex itself being hard. luckily there are lots great regex sites.
- dispatch tables are great
- write little functions. Some of the problems seemed very hard, and I used the famous anti-procrastination advice of just start with the smallest thing you can do and lo and behold in the middle of writing the most basic two line function I would see how to write the next one, and the next, and soon enough the entire bigger problem was done
- little functions really help with being able to read the code and troubleshoot.
- many problems are just graphs, which can be implemented many ways, from using classes to lists to dicts. but its still all graphs.
- python has lots of great tools in libraries like `collections` which should just be in the language. why do I have to import things like `defaultdict` which it is so useful that it should be there in the first place
- implementing something myself makes it stick in my brain, vs googling a solution
- if/else in list comprehensions can be great: `"".join([c if c != False else "_" for c in password]`
- the algo matters more than the machine speed. I moved my Day 11 solution to a super beefy high memory machine to brute force the solution - but it was taking the same runtime as on a small 1gb mem shared server. The fault was with the overly slow code, not the machine speed.


## notes on each puzzle:

## Day 1: No Time for a Taxicab

path finding

I found the simple things like turning directions tougher than the bigger problem. So doing it in pieces really helped.

## Day 2: Bathroom Security

move around a numpad

This problem had a diamond shaped keypad, so one way to move around the keypad was to have the shape of the keypad and move according, but it was much easier to use a dummy character to represent the off keypad points:


```
.......
...1...
..234..
.56789.
..ABC..
...D...
.......
```

Key takeaway: use a char to demarcate edges, and try to write more general code - in this case my part 1 could only deal with a square numpad, but it was just as easy to code it up to deal with a numpad of any shape.

## Day 3: Squares With Three Sides

simple math and slicing a grid. I used numpy for the win, basically use numpy if there is anything like a grid to deal with.

This involved using numpy slicing of a grid, which is always a bit tricky:

```python
def transpose(tri):
    """generates all the column wise trianges in a list of triangles"""
    for i in range(len(t[0])):          # the columns, could just use 3 here
        for j in range(0, len(t)-2, 3): # now going down the entire length of the array
            yield t[j:j+3,i]

sum([is_tri(i) for i in transpose(t)])
```

## Day 4: Security Through Obscurity

Nothing interesting here,just following directions, a few notes:

- there are lots of little tricks in these puzzles, like sorting the same list in two different orders
- namedtuples are great, much easier to read than a list
- is there a better way to build a string? Right now I append chars to a list then join them into a string.

## Day 5: How About a Nice Game of Chess?

find a password. I used hashlib, was an interesting problem since I used [hashlib](https://docs.python.org/3/library/hashlib.html) for the first time.

I liked this bit of code:

```
password = [False for _ in range(8)]

while False in password:
  # fills in one letter of the password
```

## Day 6: Signals and Noise



Day 7 | move around a numpad | used both numpy and lists. Key takeaway: use a char to demarcate edges
Day 8 | simple math and slicing a grid | numpy for the win, basically use numpy if there is anything like a grid to deal with.
Day 9 | ? | use Counter and namedtuples
Day 10  | parsing instructions | was a challange to fully comprehend the problem, though easy to code.
Day 11 | building the right kind of graph with breadth first search | solved part 1 using a dumb BFS, but part two the search space is so big that I need to optimize. #TODO
Day 12 | parse instructions to update registers | sort of like building a vm?
Day 13 | build a map and find a path | used bfs, easy enough, but need to implement a generic path solver. its got pics too!
Day 14 | find a password | used hashlib, was an interesting problem
Day 15 | solve a system | find positions of a moving system at time t. Could have used math instead.
Day 16 | find a password | used hashlib, was an interesting problem
Day 17 | Get shortest, than longest path | looked similar to day 13, but different.

Note: link jupyter notebooks and highlight the interesting part of each days challange.
