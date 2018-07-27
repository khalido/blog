---
title: "Googles Best Practices for ML Engineering"
date: 2018-07-22
draft: true
tags:
- python
- machine learning
- deep learning
---

Notes on [Google's best practices guide for ML engineering](https://developers.google.com/machine-learning/guides/rules-of-ml/):

> This document is intended to help those with a basic knowledge of machine learning get the benefit of Google's best practices in machine learning.

## do we need ML?

### Rule 1: don't do ML unless there is enough data and ML is actually needed.

- will human hueristics do well enough?
- is there enough data?

### Rule 2: first write down what you want the ML to do and what data you might want.

- metrics
- have a way to run experiments

### Rule 3: Use ML over complex heristics.

- Once enough data and goals, move on to ML. ML models are easier to update and maintain then complex heuristics.

## ML pipelines and infrastructure

### Rule 4: Start with simple ML and concentrate on infrastructure:

- how is data getting to the model
- what does it mean to be good or bad for us
- how are results delivered to our app/server/user whatever
- use simple features and models to start off with.

### Rule 5: Test data flows and infrastructure seperately from ML

- have a way to check how data is getting to the algo
- manually check inputs
- have statistics for the inputs
- get models, see if they behave the same in testing and production
- ML algorithims can be unpredictable, so have tests for code and use a fixed model in production
- [Understand your data](http://www.unofficialgoogledatascience.com/2016/10/practical-advice-for-analysis-of-large.html)

### Rule 6: don't drop data if copying pipelines

When setting up data pipelines, be carefuly about copying existing ones - every data pipeline is serving a specifc need.

### Rule 7: use existing knowledge

Most ML is applied to problems with existing solutions. Use the older hueristics and rules and incorporate them into the ML algo by:

- preprocess using the hueristics
- create features from the heuristic - i.e if we have a function computing a score, make that score a feature
- look at the inputs of a heuristic and feed them as features into the ML
- modify the label, e.g multiply downloads by number of stars to make quality apps stand out more

See if there is a simpler way to incorporate old heuristics.

## Monitering

Alerts! Dashboards!

### Rule 8: freshness

- how frequently does the model need to be updated? monitor and alert accordingly.

### Rule 9: sanity check models before using

- make sure the model's perf is reasonable on validation data - e.g check area under [roc curve](https://www.wikiwand.com/en/Receiver_operating_characteristic).

### Rule 10: watch for silent failures

Supid things happen, like part of the incoming data is being dropped somewhere. the ML system will keep chugging along as they adjust to feature changes and will decay gradually.

- tracking statistics for data helps here, for example if a certain feature column has less populated data then before

### Rule 11: document features and assign owners

- document all the features, duh
- for larger systems, assign ownership and responsbilities

## First Objectives

### Rule 12: dont 

