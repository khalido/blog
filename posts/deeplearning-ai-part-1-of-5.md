---
title: "deeplearning.ai: Neural Networks and Deep Learning"
date: 2016-01-01
image: /images/deeplearningai-1-of-5-cert.png
tags:
- courses
---

It had been a while since I finished Udacity's Deep Learning course, so as a refresher I signed up for Andrew NG's [deeplearning.ai](https://www.deeplearning.ai/) course.

These are my notes for the first course in the series: [Neural Networks and Deep Learning](https://www.coursera.org/learn/neural-networks-deep-learning).

**Course Resources**

- [Discussion forum](https://www.coursera.org/learn/neural-networks-deep-learning/discussions)
- [YouTube playlist for Course 1](https://www.youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0)
- course reviews: [1](https://towardsdatascience.com/review-of-deeplearning-ai-courses-aed1328e4ffe)

## Week 1: Introduction

A basic NN looks at housing price prediction, can use simple regression

- there are many input variables, like size, bedrooms, zip code, etc so you end up with a more complex regression
- What Neural networks are great at, giving training data of inputs and matching outputs, is figuring out functions which predict the price for us.

Supervised learning maps `Input(x) → Output(y)`

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CFA8F1100ADFAC4AC884B6482F58197667C5D7E698F7354F2FCD70E34111B14C_1525925978278_file.png)

- Structured data essentially means when you have a defined input → output model, like with housing data, recommendation engines, etc
- Unstructured data is things like text, audio, video
- Deep learning is taking of because of:
  1.  **vast increase in data**
  2. increase in **computing power** - enabled experimentation
  3. which led to **better algorithms** for NN
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CFA8F1100ADFAC4AC884B6482F58197667C5D7E698F7354F2FCD70E34111B14C_1525926437957_file.png)


**Geoffrey Hinton Interview:**

- developed [back-propagation algorithm](http://neuralnetworksanddeeplearning.com/chap2.html) (as did others)
  - using the chain rule to get derivatives, see [wikipedia](https://www.wikiwand.com/en/Backpropagation)
- today, most excited about [Boltzmann machines](https://www.wikiwand.com/en/Boltzmann_machine)
  - neural nets which can learn internal representations
  - restricted Boltzmann machines can do efficient inference
- ’93 - variation bayes paper
- currently working on a paper on backprop and gradient
  - is backprop a really good algorithim for learning?
  - if cells can turn into eyeballs or teeth, than they can implement backprop as well. so, does the brain use it? the brain might have something close to it
- multiple time skills in DL - TK
- really believes in capsules:
  - represent multi dimensional activities by a little vector of activities - in each region of a image, (assuming there is only one of each type of feature) a bunch of neurons can represent different aspects of a feature. normally in NN u have a great big layer, this partitions the representation into capsules.
- supervised learning has worked really well, but unsupervised learning is going to be crucial in the future
- today, varitional altering code and GAN’s are huge
- advice for breaking into deep learning:
  - read the literature, but don’t read too much
  - notice something which doesn’t feel right, then figure out how to do it right
  - never stop programming
  - read enough so you start developing intuitions then trust them
  - research ideas for grad students: find a adviser whose beliefs are similar to yours
- deep learning is not quite a second industrial revolution, buts its close to it. there is a huge change from programming computers to showing them, and they figure it out
- early days of AI ppl were convinced you need symbolic representations of things and logic and that the essence of intelligence was reasoning, but that was a huge mistake
- Now, the view is that a thought is just a great big vector of neural activity. say, words go in, words go out, but whats in b/w doesn’t have to be anything like a string of words. Hinton says its silly to think thoughts have to be in some kind of language.

Hinton is fascinating and explains things really clearly.

----------

## Week 2: Basics of NN programming

First up, we do a binary classification via logistic regression, where we classify an image into `1` cat or `0` not cat. Key concepts for this:

- a derivative is just the slope of a line, and on a curve its  different at different points on the curve.
- loss function: this gives us a score for prediction vs actual (on a single sample)
- cost function: gives us the average of errors across all predictions
- gradient descent: move slowly in the direction of the correct result
- computation graph: functions or calculations can be represented as a graph of the actual calcs to be done and added together
- …
- vectorization: running code is fast, and using vectors speeds up code tremendously. Wherever possible avoid for loops.

**Pieter Abbeel Interview:**

- his [twitter](https://twitter.com/pabbeel)
- deep reinforcement learning is taking off because regular reinforcement learning needs a lot of domain expertise, while the deep learning version needs a lot less engineering
- supervised learning is about input output mapping, while deep reinforcement learning is much more about learning the incoming data - the exploration problem, then how do you credit actions which got rewards/failures?
- the big challenge is how to get systems to reason over long time horizons
- safety is a big challenge - how do you learn safety, for example in a self driving car, you need both success and failure to learn.
- make sure you can make the connection from the code/math to what change it can make
- good time to get into AI, Andrej Karpathy’s DL course, UC Berkely has a Deep Reinforcement course online.
- deep reinforcement learning is really powerful and general, the same learning can take in different inputs and learn a task, like teaching a two legged robot to move, then the same algo can take a four legged robot to move even though the inputs (sensors) and outputs (motors) are now different.
  - drl algos still start from scratch for tasks

## Week 3: Code a simple NN

- goes over the vector math to compute NN output
- activation functions take in weighted data and apply a non-linear transformation
  - sigmoid squeezes output to `0 to 1`, useful for predicting probablity, not used much anymore
  - tanh is like sigmoid but from `-1 to 1` - superior to sigmoid in almost all applications
  - relu function is very popular, anything below zero becomes zero, otherwise the value stats as it is
  - leaky relu multiplies negative numbers by a small number, like `0.01` - this helps to increase the range of the relu output
  - more, try different activation functions
- non-linear activation functions are a critical part of a NN since they create new relationships b/w data points, increasing complexity with each layer.
- linear hidden layers are more or less useless since any number of linear hidden layers can be reduced to a single linear layer
- its important to randomly initialise weights as starting with weights set to zero the hidden units will initialise the same way and thus all the hidden units are symmetric and compute the same function.
- Fix this by initialising weights and b to small random numbers like `0.01`. If weights are large, the slopes of an activation function like tanh or sigmoid are flat for large numbers, so the gradient is small and training is slow.

**Ian Goodfellow interview:**

- had been studying generative models for a long time, so GANs rose out of that. At a bar, coded it up at midnight after a party, and it worked on the first try.
- working on making GANs more reliable
- wrote the first modern textbook on deep learning, very popular
- linear algebra and probability are very important to master deep learning
- DL only really got going five years ago
- there’s an amazing amount of AI work to be done
- write good code and put it on github, solve a problem which ppl have

## Week 4: Code a deep NN

- A deep neural network is a neural network with many layers which can learn functions which shallower networks are unable to. Its hard to predict the number of layers for a given problem, so experiment.
- write down all the matrix dimensions of all the layers in your NN - this helps with debugging and understanding how data is being transformed as it passes through the NN
- why do we need deep networks?
  - different layers learn different features
  - early layers learn simpler features, the deeper layers learn more complex objects and representations
  - DNN allow more complex functions to be computed - circuit theory postulates that a small L layer deep NN can compute functions which a shallower network would require exponentially more hidden units to compute
  - deep learning makes for great PR
- gradient descent needs forward and backward functions:
  - forwards: we compute a prediction, moving through all the layers, and caching the results at each layer
  - backwards: now we compute the gradients at each layer, moving backwards
  - finally we use these gradients to tweak each layer slightly towards the right direction
- a lot of the complexity in ml comes from the data, not the code
- parameters are the weights and beta
- hyper parameters:
  - learning rate
  - # iterations
  - # hidden layers L
  - # hidden units n1, n2 ….
  - choice of activation function
  - there are lots of other hyperparameters like momentum, minibatch size, regularization, etc
- there is a lot of experimentation around parameters, try to do this empirically and build intuitions around what works for different kinds of data and NN as parameters work differently for different problems
- don’t compare DL networks to the human brain - while there are simplistic analogies b/w a single neuron and a logistic unit with sigmoid activation - but we don’t know how neurons in a human brain work or how the brain learns