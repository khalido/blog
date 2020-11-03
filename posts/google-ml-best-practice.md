---
title: "Googles Best Practices for ML Engineering"
date: 2019-03-02
description: my read through notes on googles ml guide 
category: [machine learning]
layout: post
toc: false
---

Notes on [Google's best practices guide for ML engineering](https://developers.google.com/machine-learning/guides/rules-of-ml/):

> This document is intended to help those with a basic knowledge of machine learning get the benefit of Google's best practices in machine learning.

# do we need ML?

## Rule 1: don't do ML unless there is enough data and ML is actually needed.

- will human hueristics do well enough?
- is there enough data?

## Rule 2: first write down what you want the ML to do and what data you might want.

- design and implement metrics
- have a way to run experiments

## Rule 3: Use ML over complex heristics.

- Once enough data and goals, move on to ML. ML models are easier to update and maintain then complex heuristics.

# ML Phase 1: Pipelines and infrastructure

Focus on system infrastucture at first.

## Rule 4: Start with simple ML and concentrate on infrastructure:

- how is data getting to the model
- what does it mean to be good or bad for us
- how are results delivered to our app/server/user whatever
- use simple features and models to start off with.

## Rule 5: Test data flows and infrastructure seperately from ML

- have a way to check how data is getting to the algo
- manually check inputs
- have statistics for the inputs
- get models, see if they behave the same in testing and production
- ML algorithims can be unpredictable, so have tests for code and use a fixed model in production
- [Understand your data](http://www.unofficialgoogledatascience.com/2016/10/practical-advice-for-analysis-of-large.html)

## Rule 6: don't drop data if copying pipelines

When setting up data pipelines, be carefuly about copying existing ones - every data pipeline is serving a specifc need.

## Rule 7: use existing knowledge

Most ML is applied to problems with existing solutions. Use the older hueristics and rules and incorporate them into the ML algo by:

- preprocess using the hueristics
- create features from the heuristic - i.e if we have a function computing a score, make that score a feature
- look at the inputs of a heuristic and feed them as features into the ML
- modify the label, e.g multiply downloads by number of stars to make quality apps stand out more

See if there is a simpler way to incorporate old heuristics.

# Monitering

Alerts! Dashboards!

## Rule 8: freshness

- how frequently does the model need to be updated? monitor and alert accordingly.

## Rule 9: sanity check models before using

- make sure the model's perf is reasonable on validation data - e.g check area under [roc curve](https://www.wikiwand.com/en/Receiver_operating_characteristic).

## Rule 10: watch for silent failures

Supid things happen, like part of the incoming data is being dropped somewhere. the ML system will keep chugging along as they adjust to feature changes and will decay gradually.

- tracking statistics for data helps here, for example if a certain feature column has less populated data then before

## Rule 11: document features and assign owners

- document all the features, duh
- for larger systems, assign ownership and responsbilities

# First Objectives

## Rule 12: dont overthink which objective to optimize

Don't optimize a single metric early, initially all metrics we care about should typically be going up. Consider the overall 'health' of the ml process first.

## Rule 13: Use a simple, observable and attributtable metric as a first objective

This should be straightward and serve as a proxy for the true objective, in fact, often there is no 'true' objective. Model direct things, leave indirect things for later or to a different layer altogether.

## Rule 14: Start with an interpretable model to make debugging easier

Linear regression, logistic regression etc are straightforward to understand and debug vs the more complicated models. 

## Rule 15: Seperate spam filtering and quality ranking

Rank content seperately from how you determine what kind of content it is - for example have a different model for post quality score, and another one for categorzing spam.

i.e don't do something overly simple like assuming posts with a low score are spam.

# ML Phase II: Feature Engineering

Phase 1 should give us a simple working end to end system with unit and system tests.

In Phase 2 we pick all the low hanging fruit, like pulling in as many features are possible and combining them in intuitive ways.

## Rule 16: Launch and iterate

As you build the model, keep adding, removing and recombining features and launching new models. Don't wait to do all the features in one go, iterate.

## Rule 17: Start with directly observed and reported features as opposed to learned features

Learned features can be coming from elsewhere can have a lot of issues and should not be in the first model. These outside features come with their own objectives which could be only weakly correlated to our objective, and there is no gurantee they will lead to optimal solutions.

We can get excellent baseline performance without deep deatures.

## Rule 18: Explore with features of content that generalizes across contexts

## Rule 19: User very specific features when you can

with big data, its easier to learn millions of simple features than a few complex features. Consider making groups of features if each feature only applies to a small fraction of data, but the group coverage is > 90%.

## Rule 20: combine and modify existing features to create new features in human understandable ways

There are many ways to do this, for example turning an age feature into infant/child/teenager/adult/senior using age ranges. Don't overthink - basic quantiles gives the most impact. 

Also consider cross combining features like {male,female} with say a country feature like {US,Canada} to get a feature like (male, US). This takes a lot of data, but can be useful in some contexts, while overfitting in others.

## Rule 21: number of feature weights is roughly proportional to the amount of data

There is a lot of stats theory about the appropriate level of complexity for a model, but this rule is the most important to know. Scale the learning to the size of your data.

With small numbers of training data, you probably have to human engineer features. With larger data sets, regularization and feature selection helps to cut down features.

## Rule 22: clean up features no longer in use

drop useless features. keep infrastructure clean so that promising features can be tried fast. Add features back if necesary. 

Consider the coverage of features, like how many examples are covered? If a feature only covers 8% of the data, it might be useless, but on the other hand a feature covering only 1% data could have a 90% prediction rate.

# Human analysis of the System

important to look at existing models and think about how to improve them.

## Rule 23: you're not a typical end user

You're too close to the code and results, so its important to bring in outside users - from within the company, lay people or a crowdsourcing platform. 

Develop user experience methodologies, and create user personas and do usablity testing.

## Rule 24: measure the dela within models

measure both results b/w different models, and also results with the same model to make sure its stable.

## Rule 25: utilitarian performance trumps predictive power

the key question is what we are doing with the prediction - for example when ranking something the quality of the final ranking matters more than the quality of the prediction itself. But in a spam filter which has a cutoff on what is blocked, the precision matters more.

## Rule 26: look for patterns in the measured errors and create new features

Say for some reason the system is demoting longer posts, then a post lengh feature could be useful. Don't overthink it - add relevant features and let the model figure it out.

## Rule 27: try to quantify observed behaviour

if the model has 'bad' properties, like recommending gag apps too often, try to measure or get humans to add category labels and add as a feature.

>  If your issues are measurable, then you can start using them as features, objectives, or metrics. The general rule is "measure first, optimize second".

## Rule 28: be aware that identical short-term behaviour does not imply identical long-term behaviour

A model for say predicting apps will work great in practice but in production turn out to not recommend any new apps, since in practice there wasn't a way to learn that new apps should be shown too.

# Training-Serving Skew

this is the difference b/w performance during training and serving, typically caused by:

- difference in how data is handles in training and serving pipelines
- change in data b/w training and serving
- feedback loop b/w model and algorithim

Best solution is to explicitly monitor things so system and data changes don't introduce skew unnoticed.

## Rule 29: best way to make sure you train like you serve is to save the set of features used at serving time and pipe those features to a log to use them at training time

If not for all examples, log a fraction of the data.

## Rule 30: Importance-weight sampled data, don't arbitarily drop it

don't arbitarily decide to take the first ten results, rather weight by importance - say if we want to sample X with a 30# probablity, give it a weight of 10/3.

## Rule 31: beware if you join data from a table at training and serving time, the data in the table may change

b/w training and serving time, features in a table may be changed. Avoid this by logging features at training time.

## Rule 32: reuse code b/w training and serviing pipelines whenever possible

While how data is arriving is different, requiring different code, try to transform initial data into a human readable object which can be tested and transformed by a common method for use by the machine learning system. Try to use the same programming language for training and serving.

## Rule 33: if you make a model on data till Jan 5th, test it on data after Jan 6th

this better reflects how the model will do in production.

## Rule 34: in binary classification for filtering make small short-term sacrifices in performance for very clean data

Say our spam filter blocks 75%, and we might be tempted to learn from the 25% which gets through and the user labels spam. This introduces sampling bias, we will get cleaner data by labelling 1% of traffic as "held-out" and send all those to the users, and we can than use those labelled samples as training data.

## Rule 35: Beware of inherent skew in ranking problems

When we change a ranking algorithim so that different results show up, this effectively changes the data the algorithim is going to see in the future. Design algos around this:

- have higher regularization for features that cover more queries, over features that are only for one query. This allows the model to favour features that are specific to one or a few queries, and helps from preventing very popular results into leaking into irrelevant quries.
- only allow features to have positive weights
- don't have document only features

## Rule 36: Aviod feedback loops with positional features

## Rule 37: Measure Training/Serving skew

- difference in performance on training and holdout data - will always exist, so doesn't necessarily mean something bad.
- difference in performace on holdout data and the nextday data - large drops in perf here could indicate some features are time-sensitive and possibly degrading model perf.
- difference in performance bw nextday day and live data. differences here could indicate model error.

# ML Phase III: Slowed Growth, Optimization Refinement, and Complex Models

The second phase is ending when gains are diminishing and we have tradeoffs b/w metrics.

Since gains are harder to achieve, the machine learning has to get more sophisticated.

## Rule 38: don't waste time on new features if unaligined objectives have become the issue

as measurements plateau, teams often look at issues outside the scope of the current machine learning system. If those goals aren't covered by the exisiting ml system, change the system or the goals.

## Rule 39: launch decisions are a proxy for long-term product goals

For example, adding a feature might increase installs, but drop daily active use. Launch decisions depend on multiple factors, only some of which are optimizable by ML.

Metrics are a proxy for more longterm goals.

## Rule 40: Keep ensembles simple

each model should either be ensemble taking input of other models, or a base model taking in features, not both. Don't pile on models on top of models - this can result in bad behaviour.

Make sure that in crease in the predicted probality of a underlying classifier doesn't decrease the predicted probability of the classifier.

## Rule 41: When performance plateaus, look for qualitatively new sources of information to add rather than refining existing signals.

add more relevant signals, build out infrastructure for radically different features, use more deep learning, weigh benefits of new features against increased complexity.

## Rule 42: Don’t expect diversity, personalization, or relevance to be as correlated with popularity as you think they are.

popularity is easy to measure, diversity, personalization and relavance is harder - adding features for these can turn out to not work very well, i.e they get less weight in the model.

Postprocessing can help, or directly modifing the objective to increase diversity or relevance.

## Rule 43: Your friends tend to be the same across different products. Your interests tend not to be.

While one thing might be close to another, doesn't mean it applies across products. 

