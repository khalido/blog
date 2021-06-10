---
title: "deeplearning.ai: Structuring Machine Learning Projects"
date: 2018-01-01
description: notes for part 3 of the deeplearning.ai course
image: /images/deeplearningai-3-of-5-cert.png
tags:
- courses
---

# deeplearning.ai: Structuring Machine Learning Projects

This course covers how to think about and improve machine learning systems.

> You will learn how to build a successful machine learning project. If you aspire to be a technical leader in AI, and know how to set direction for your team's work, this course will show you how.


**Course Resources**

- [Course home](https://www.coursera.org/learn/machine-learning-projects/home/welcome)
- [Discussion forum](https://www.coursera.org/learn/machine-learning-projects/discussions)

- [Week 1: ML Strategy](#week-1-ml-strategy)
    - [Orthogonalization](#orthogonalization)
    - [Setting up your goal](#setting-up-your-goal)
        - [Single number evaluation metric](#single-number-evaluation-metric)
        - [Satisficing and Optimizing metric](#satisficing-and-optimizing-metric)
        - [Train/dev/test distributions](#traindevtest-distributions)
        - [Size of the dev and test sets](#size-of-the-dev-and-test-sets)
        - [When to change dev/test sets and metrics](#when-to-change-devtest-sets-and-metrics)
    - [Comparing to human-level performance](#comparing-to-human-level-performance)
        - [Why human-level performance?](#why-human-level-performance)
        - [Avoidable bias](#avoidable-bias)
        - [Understanding human-level performance](#understanding-human-level-performance)
        - [Surpassing human-level performance](#surpassing-human-level-performance)
        - [Improving your model performance](#improving-your-model-performance)
    - [Andrej Karpathy interview](#andrej-karpathy-interview)
- [Week 2: More ML Strategy](#week-2-more-ml-strategy)
    - [Error Analysis](#error-analysis)
        - [Carrying out error analysis](#carrying-out-error-analysis)
        - [Cleaning up incorrectly labeled data](#cleaning-up-incorrectly-labeled-data)
        - [Build your first system quickly, then iterate](#build-your-first-system-quickly-then-iterate)
    - [Mismatched training and dev/test data](#mismatched-training-and-devtest-data)
        - [Training and testing on different distributions](#training-and-testing-on-different-distributions)
        - [Bias and Variance with mismatched data distributions](#bias-and-variance-with-mismatched-data-distributions)
        - [Addressing data mismatch](#addressing-data-mismatch)
    - [Learning from multiple tasks](#learning-from-multiple-tasks)
        - [Transfer learning](#transfer-learning)
        - [Multi-task learning](#multi-task-learning)
    - [End-to-end deep learning](#end-to-end-deep-learning)
        - [What is end-to-end deep learning](#what-is-end-to-end-deep-learning)
        - [Whether to use end-to-end deep learning](#whether-to-use-end-to-end-deep-learning)
    - [Ruslan Salakhutdinov interview](#ruslan-salakhutdinov-interview)

## Week 1: ML Strategy

There are lots of ways to improve a deep learning system, so its important to sse quick and effective ways to figure out the most promising things to try and and improve.

### Orthogonalization

- old school tv's had a number of knobs to tune the picture - all the settings made it very hard to get the picture perfect
- cars have orthogonal controls - a steering and speed which effect two different things making it easier to control. If we have controls which effect the steering and speed at the same time it would make it much harder to get the speed and steering angle we wanted.
- we have a chain of assumptions in ML: fit training set on cost func, fit dev set, fit test set, then perform well in the real world and we want to have different set of knobs to tune each part.
- ideally we have a number of controls which do one task well without effecting other things too much. 
- of course, some controls apply across many layers and are still useful, like early stopping

### Setting up your goal

#### Single number evaluation metric

- set up a single real number to evaluate performance before starting out on a project
- a well defined dev set and a single metric speeds up the iterative process of developing a good model
- looking at a simple cat classifier:

| Classifier | Precision | Recall |
| ---------- | --------- | ------ |
| A          | 95%       | 90%    |
| B          | 98%       | 85%    |

- **Precision**: of the examples our classifier says are cats, what percentage is actually right
- **Recall**:  what % of actual cats are correctly classified
- The problem with using precision and recall is it can make it hard to figure out which classifier is better
- [F1 Score](https://www.wikiwand.com/en/F1_score) is the harmonic average of precision and recall using $F1 = 2 / ((1/P) + (1/R))$ or $2 * (precision * recall) / (precision + recall)$
    - F1 score is usefeul as it balances precision and recall, rather than just taking the simple average, which would favour outliers
- to summarize, have a single number metric (this could be an average of several metrics) and a good dev set

#### Satisficing and Optimizing metric

- its not easy to setup a single number - we might narrow things down to a single number, accuracy, but also want to evaluate running time
- solve this by picking one metric to optimize, and satisfy the other metric by picking a threshold, like all running times below 1000ms are good enough.
    - for voice recognition, like on Amazon Alexa, we have metrics for how long humans are ok to wait, so we can just use that number as a threshold
- so, we have a make metric to optimize, and any number of other metrics which we satisfy with thresholds. 
 
 #### Train/dev/test distributions

 - dev (cross validation set) and test (the final holdout data) sets have to come from the same distribution.
 - for example, if we have data from different regions, don't say us/uk/europe is the dev set and asia is the test set - regions will have differences.
 - an ML team wasted time optimizing loan approvals on medium income zip codes, but was testing on low income zip codes.
 - choose a dev and test set to reflect data you expect to get in the future and consider important to do well on.

#### Size of the dev and test sets

- old rule of thumb for train/dev/test: 60/20/20 - worked for smaller data.
- but now we have much larger data sets, so for 1M data set, 1% or 10K might be enough for a test set.
- deep learning is data hungry so we want to feed it as much data as possible for training
- the test set helps us evaluate the overall system, so it has to be big enough to give us high confidence.
    - this will vary depending on the data set.
    - sometimes we might not need a test set at all.

#### When to change dev/test sets and metrics

- say we've built two cat classifiers, A has 3% error, B has 5% error.
- A is better, but lets through porn images. B stops all the porn images, so even though it has higher error, B is better algorithm.
- so we want to change our metrics here, say adding a weight to penalize porn images
- think of machine learning as having two separate steps:
    - 1. figure out the metric
    - 2. worry about how to actually do well on the metric
- other things happen, like our image classifier performs well on our data set, but users upload bad quality pictures which lower performance, so change metric and/or the dev set to better capture what we need our algorithm to actually do.

### Comparing to human-level performance

#### Why human-level performance?

- two main reasons we compare to human level performance:
    - ML is getting better so its become feasible to compare to human level performance in many applications.
    - the workflow of designing and building ML systems is much more efficient when comparing to what humans also do.
- for many problems, progress is rapid approaching human level performance, and slows down upon reaching it. the hope is that its reaching a theoretical limit, called the Bayes optimal error.
- **Bayes optimal error** is the best possible error
    - for tasks humans are good at, there isn't much range b/w human error and the bayes optimal error.
- when our ML algo is worse than humans, get humans to:
    - give us more data, like label images, translate text, etc.
    - manual analysis errors - why did a human get it right and algo get it wrong?
    - better analysis of bias/variance
  
#### Avoidable bias

- humans are great at image classification, so looking at two image classification algos:

|                | Bias Example | Variance Example |
| -------------- | ------------ | ---------------- |
| Humans         | 1%           | 7.5%             |
| Training error | 8%           | 8%               |
| Dev Error      | 10%          | 10%              |

- the left example illustrates bias - since humans are doing much better than the algo, we focus on improving training error.
- the right example shows that we are close to human error - so we focus on reducing the variance
- if we are doing better than Bayes error we're overfitting.
- having an estimate of the bayes optimal error helps us to focus on whether to reduce bias or variance.
    - avoidable bias: training error - human level error
    - variance: dev error - training error

#### Understanding human-level performance

- there are multiple levels of human performance - choose what matters and what we want to achieve for our system
    - do we use a typical doctors error level, an experienced doctors, or the lower error level from a team of experienced doctors.
    - surpassing an average radiologist might mean our system is good enough to deploy
- use human level error as a proxy for Bayes error. 
- An error analysis example from medical classification, where say human error ranges from 0.5-1%:

| Error       | Bias Example | Variance Example |
| ----------- | ------------ | ---------------- |
| Human/Bayes | 1%           | 1%               |
| Training    | 5%           | 1%               |
| Dev         | 6%           | 5%               |

- the left column we need to concentrate on reducing the training error - the variance, and the human error we pick doesn't matter.
- the right col we need to concentrate on the dev error - i.e the variance, and picking the lower range of human error is more important since we are close to human level performance.
- so we have a more nuanced view of error, and using bayes error instead of zero error leads to better and faster decisions on reducing bias or variance.

#### Surpassing human-level performance

- ml gets harder as we approach/surpass human level performance
- when we've surpassed human level performance, are we overfitting, or is the bayes error lower than human error.
- some applications have surpassed human level: online advertising, product recommendation, loan approval, logistics
    - all these examples are learning from structured data, not natural perception problems which humans are very good at
    - teams have access to heaps of data
- computers haven gotten to single human level at certain perception tasks, like image recognition, speech.

#### Improving your model performance

- two fundamental assumptions of supervised learning:
    - we can fit the training set pretty well, or avoid bias
    - the training set performance generalizes well to the dev/test set - achieve low variance
- to improve a deep learning supervised system
- for improving bias:
    - train bigger model
    - train longer or use better optimization algo (RMSprop, Adam, momentum, etc)
    - try other model architectures, hyperparameter search
- improve variance:
    - more data
    - regularization (L2, dropout, data augmentation)
    - NN architecture, hyperparameter search
- 

### Andrej Karpathy interview

- before NN's ml/ai was a lot of graphs, tree pruning, not very satisfying - NN's actually felt like AI vs the old school AI techniques
- before, humans wrote code to do something, with neural networks / machine learning humans write the optimization algo and specify inputs/outputs and the computers write code
- while working on cifar10, had predicted an error rate of 10%, but we're now down to 2-3%.
- built a javascript interface to show himself imagenet images and classify them
- famous for putting his deep learning stanford class online
- understand of deep learning has changed:
    - surprised by how general deep learning is - no one saw how well it would work
- amazed at how you can take pre trained networks and apply them to other tasks
- people are crushing tasks one after the other with transfer learning
- surprised that unsupervised learning hasn't worked so well
- has been thinking about the future of AI, thinks will split into two directions:
    - applied AI, where ppl train NN's to do something, generally supervised learning
    - artificial general intelligence, working on dynamic systems to do everything a human can
- thinks the approach to do one thing at a time, like with current neural nets which recoginze images, or do speech etc, won't lead to AGI, we need a single kind of NN which learns all the tasks a human can do - see [his short story on how this might look](http://karpathy.github.io/2015/11/14/ai/).
- people liked CS213N becuase it didn't abstract away things, it works through the low-level details. Implementing stuff is the best way to learn it.

## Week 2: More ML Strategy

### Error Analysis

#### Carrying out error analysis

- manually examining what your algo is doing gives insight
    - e.g looking at a 100 misclassified dev set examples, see whats the biggest type of error and work on fixing that. i.e we want to work on the errors which make up the bulk of our problem, rather than the lower percentage errors.
- error analysis helps us pick useful actions which will have meaningful improvements.
- we can evaluate multiple ideas in parallel - use a spreadsheet to help decide:

![](img/eval-multiple-ideas.png)

- so summarize errors, find categories, prioritize important ones

#### Cleaning up incorrectly labeled data

- sometimes its worthwhile to check training sets for mislabelled images
    - deep neural networks are quite robust to random errors in the training set, so few mistakes are ok
    - but systematic errors aren't ok, like labelling all white dogs as cats
- modify our error spreadsheet above to have a mis-labelled category, we should always go after the biggest cause of error first
- correcting dev/test set examples:
    - apply same process to dev/test so they continue to come from the same distribution
    - consider examining examples the algo got right as well as the ones it got wrong
    - we might decide to only correct labels in the dev/test sets and not go through the bigger training set, so dev/test data may now come from slightly different distrubutions. This is ok, long as both dev/test have the same distribution, and the train set is a slightly different distribution

#### Build your first system quickly, then iterate

- there are many ways to make a speech recognition system more robust. More generally, for any ML project there are 50 different directions to improve a ml system
- quickly set up a dev/test set and metric, build a initial system, then use Bias/Variance analysis and error analysis to prioritize next steps
- a lot of value in the initial ML system is to help us prioritize future efforts. 

### Mismatched training and dev/test data

#### Training and testing on different distributions

- deep learning needs big data, so often teams end up shoving whatever they can find into a training set, so you end up with different distributions b/w train and test/dev sets.
- e.g we can get 200k cat pictures from web pages, which are good quality and in large numbers, and 10k pictures from a mobile app which are crappy.
- so what can we do:
    - combine the datasets and randomly shuffle into a train/dev/test split (205k, 2,500, 2,500), so everything is from the same distribution
        - the problem here is that 2,381 out of 2,500 images in the dev/test set will come from the mobile app
    - make the training set use all 200k from the web plus 5K from the app, and test/dev set will be 2,500 images each from the app. This sets the target what we want it to be, even though the distributions are no different.
- a real example of a speech recognizer for directions - we are only listening for sentences like "find the nearest gas station" but we can train on all kinds of speech data, while the dev/test sets are from our specific area. If our specific application has enough data we can add some of it to the training set as well.

#### Bias and Variance with mismatched data distributions

- the way we analyze bias and variance changes when train dev/test sets are from different distributions
- so we need a training-dev set which has the same distribution as the training set, and isn't used for training. so we would have error analysis like:

 |                    | Variance Problem | data mismatch Problem |
 | ------------------ | ---------------- | --------------------- |
 | Training Error     | 1%               | 1%                    |
 | Training-dev error | 9%               | 1.5%                  |
 | Dev Error          | 10%              | 10%                   |

#### Addressing data mismatch

- carry out manual error analysis to understand difference b/w training and dev/test sets
- we might find errors like a lot of our dev/test data is nosier than training set
- so then we can collect more training data, or make it similar to dev/test data
- use artificial data synthesis to make the training data more similar to dev set:
    - combine some of the training data with something to make it similar to the test/dev distribution, like recorded background noise, or generate new examples
- be careful about simulating data from a small subset of space, like background noise which isn't representative of actual background noise 
- we can synthesize data which passes the human test but it could lead to over fitting as our synthetic data might just be making a subset of the dataset.

### Learning from multiple tasks

#### Transfer learning

- apply knowledge from one task to another
- take a image recognizer NN, delete the last layer, create a new layer with random weights and retrain the NN on the new dataset. (called fine tuning)
    - we can train only the last layer, or given enough data we can train the entire network.
    - this works as a lot of the low level layers are recognizing structures and features which transfers across to different tasks
- transfer learning makes sense when:
    - task A and B have the same input X (image, speech)
    - we have a lot of data for task A and less data for task B
    - the low level features are similar for both tasks
- obviously, having a large dataset for the actual problem is ideal, but often we end up having better/more data for a well known problem, like ImageNet for images, and a lot less for what we want to do (say radiology photos).

#### Multi-task learning

- try to have one NN learn multiple tasks - like a simple self driving car has to detect several things: stop signs, pedestrians, cars, traffic lights, etc
- so the NN predicts a output vector where each position indicates whether something is there or not. (one image has multiple labels)
- we could have a NN for each type of object, so when does multi-task learning make sense?
    - low level features are shared across each object.
    - the amount of data for each task is similar
    - can train a big enough NN to do well on all tasks (can perform better than single NNs)
- in practice, multi-task is used a lot less than transfer learning - though is used a lot in computer vision

### End-to-end deep learning

#### What is end-to-end deep learning

- there are some learning systems which need multiple stages of processing, like speech recognition and vision - engineers had spent years engineering feature pipelines
- and end to end deep learning neural network replaces all these multiple stages with a single neural network
- but sometimes you don't want to just feed raw data, like with face recognition - it works better if the image is zoomed and cropped to the face - so you have two deep learning stages:
    - figure out where is the face
    - now figure out whose face it is
- when we have heaps of data, like with translation, end to end works better 
- estimating a childs age from a hand xray: there isn't much data so multistep approach works better.

#### Whether to use end-to-end deep learning

- benefits of end-to-end deep learning:
    - lets the data speak - if we have enough data a large enough NN will figure it out
    - less hand designing of components needed
- cons
    - may need large amount of data
    - may exclude potentially useful hand designed components
- learning algos have two main sources of knowledge: the data and human knowledge
- key q: do we have enough data to learn a function of the complexity to map x to y?
- in a self driving car, we have `image/radar/lidar -> cars/pedestrians -> route -> steering` and currently some of these things are done with non deep learning approaches
- it would be great to input data and get a steering/accel output, but this isn't very promising yet for self driving cars

### Ruslan Salakhutdinov interview

- Director of AI research at Apple [twitter](https://twitter.com/rsalakhu?lang=en), [linkedin](https://www.linkedin.com/in/ruslan-salakhutdinov-53a0b610)
- see his [slides on his talk on the deep learning revolution](http://www.cs.cmu.edu/~rsalakhu/jsm2018.html)
- boltzmann machines and deep boltzmann machines are very powerful but we haven't figured out how to use them yet
- generative modelling is exciting, expects a lots of progress in the near future
- companies have lots of unlabelled data but we haven't figured out how to use it
- advice for new researchers:
    - try different and new things. with neural networks too many ppl wrote them off as non-convex problems impossible to optimize. 
    - code backprop yourself once to understand it
    - phd vsd industry: more freedom in academia for long term problems, but industry research is very exciting and well funded, impacts millions of users
- exciting areas: unsupervised learning, deep reinforcement learning, NLP

---

course [done and dusted](https://www.coursera.org/account/accomplishments/certificate/QZESAQHSKF3K):

![](img/deeplearningai-3-of-5-cert.png)