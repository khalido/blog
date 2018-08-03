---
title: "deeplearning.ai: Improving Deep Neural Networks"
date: 2018-07-12
tags:
- python
- courses
- deep learning
---

[Improving Deep Neural Networks: Hyperparameter tuning, Regularization and Optimization](https://www.coursera.org/learn/deep-neural-network/home/welcome)

**Course Resources**

- [Discussion forum](https://www.coursera.org/learn/deep-neural-network/discussions)
- [YouTube playlist for Course 1](https://www.youtube.com/watch?v=1waHlpKiNyY&list=PLkDaE6sCZn6Hn0vK8co82zjQtt3T2Nkqc)
- course reviews: [1](https://towardsdatascience.com/review-of-deeplearning-ai-courses-aed1328e4ffe)

## Week 1: Practical aspects of Deep Learning

Train / Dev / Test sets

- training is a highly iterative process as you test ideas and parameters
- even highly skilled practicioners find it impossible to predict the best parameters for a problem, so going through
- split data into train/dev/test sets
  - training set - the actual dataset used to train the model
  - cross validation or dev set - used to evaluate the model
  - test set - only used once the model is finally trained to get a unbiased estimate of the models performance
- depending on the dataset size, use different splits, eg:
  - 100 to 1M ==> 60/20/20
  - 1M to INF ==> 98/1/1 or 99.5/0.25/0.25
- you can mismatch train/test distribution, so make sure they come from the same distribution

Bias / Variance

![](/img/bias-variance.png)

- high bias - model is under fitting, or not even fitting the training set
- high variance - model is over fitting the training and dev set
- you can have both high bias AND high variance
- balance the bias and variance, and also consider the underlying problems tractibility, as are we aiming for 99% accuracy or 70%? Compare with other models and human performance to get a sense of a baseline error

Basic recipe for machine learning

- for high bias errors: bigger NN,more layers, different model, try different activations
- high variance: more data, regularize appropirately, try a different model
- training a bigger NN almost never hurts

Regularization

![](https://upload.wikimedia.org/wikipedia/commons/b/b8/Sparsityl1.png?1531465205841)

- vectors often have many dimensions, so model sizes get BIG. regulariation helps to select features and reduce dimensions, as well as reduce overfitting
- L1 regularization (or Lasso) adds a penalty equal to the sum of absoulte coefficients
- L2 regularization (or Ridge) adds a penalty equal to the sum of squared coefficients

> L2-regularization relies on the assumption that a model with small weights is simpler than a model with large weights. Thus, by penalizing the square values of the weights in the cost function you drive all the weights to smaller values. It becomes too costly for the cost to have large weights! This leads to a smoother model in which the output changes more slowly as the input changes.

- as a rule of thumb, L2 almost always works better than L1 .

Dropout regularization

- for each iteration, use a probablity to determine whether to "drop" a neuron. So each iteration through the NN drops a different, random set of neurons.
- each layer in the NN can have a different dropout probability, the downside is that we have more hyperparameters to tweak
- in computer vision, we almost always use dropout becuase we are almost always overfitting in vision problems
- a downside of dropout is that the cost function is no longer well defined, so turn off dropout to see that the loss is dropping, which implies that our model is working, then turn on dropout for better training
- remove dropout at test time
- dropout intuitions:
  - can't rely on on any given neuron, so have to spread out weights
  - can work similar to L2 regularization
  - helps prevent overfitting

Data augmentation

- inexpensive way to get more data - e.g with images flip, distory, crop, rotate etc to get more images
- this helps as a regularization technique
-

Early stopping

- stop training the NN when the dev set and training set error start diverging - get the huperparameters from the lowest dev and training set cost.
- this prevents the NN from overfitting on the training set but stops gradient descent early
- Andrew NG generally prefers using L2 regularization instead of early stopping as that


Deep NN suffer from vanishing and exploding gradients

- this happens when gradients become very small or big
- in a deep NN if activations are linear, than the activations and derivates will increase exponentially with layers

