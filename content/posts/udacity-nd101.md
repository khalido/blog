---
title: "Udacity ND101: Deep Learning Nanodegree"
date: 2017-08-20T01:21:48Z
cover: /img/udacity-nd101-cert.png
tags:
- python
- courses
- AI
- deep learning
---

My notes & files for [Udacity's Deep Learning intro course](https://www.udacity.com/course/deep-learning-nanodegree-foundation--nd101).

## Before the course starts:

- Read [Machine learning is fun](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471#.t1zhql96j)
- Watch [Andrew NG: Deep Learning in Practice](https://youtu.be/LFDU2GX4AqM) (34 minutes)
- Go though [UD730 deep learning course](https://classroom.udacity.com/courses/ud730/) on Udacity
- Watch [Learn tensorflow 3 hour video](https://cloud.google.com/blog/big-data/2017/01/learn-tensorflow-and-deep-learning-without-a-phd)
- http://rodneybrooks.com/patrick-winston-explains-deep-learning/

### Python resources

The course recommneds knowing [basic python from here](https://www.udacity.com/course/programming-foundations-with-python--ud036), but I found the following two resources better:

- [A whirlwind tour of Python](https://github.com/jakevdp/WhirlwindTourOfPython)
- [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)

### Math resources

Need to know multivariable calculus & linear algebra.
 
- [Khan Academy Multivariable calculus](https://www.khanacademy.org/math/multivariable-calculus)
- [Linear algebra youtube playlist](https://www.youtube.com/playlist?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv) or over at [lemma](https://www.lem.ma/web/#/books/VBS92YDYuscc5-lK/landing)
- [Khan Academy's Linear Algebra Intro](https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/jacobian/v/jacobian-prerequisite-knowledge)

### Books to read

- [Grokking Deep Learning by Andrew Trask](https://www.manning.com/books/grokking-deep-learning). This provides a very gentle introduction to Deep Learning and covers the intuition more than the theory.
- [Neural Networks And Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen. This book is more rigorous than Grokking Deep Learning and includes a lot of fun, interactive visualizations to play with.
- [The Deep Learning Textbook](http://www.deeplearningbook.org/) from Ian Goodfellow, Yoshua Bengio, and Aaron Courville. This online book has lot of material and is the most rigorous of the three books suggested.

# Week 1

The two instructors are [Mat Leonard] & [Siraj Raval](http://www.sirajraval.com/).

Some of the stuff covered in the first week:

- [Scikit-learn](http://scikit-learn.org/) - An extremely popular Machine Learning library for python.
- [Perceptrons](https://en.wikipedia.org/wiki/Perceptron) -The simplest form of a neural network.
- [Gradient Descent](https://en.wikipedia.org/wiki/Gradient_descent) - A process by which Machine Learning algorithms learn to improve themselves based on the accuracy of their predictions. You'll learn more about this in upcoming lessons.
- [Backpropagation](http://neuralnetworksanddeeplearning.com/chap2.html) - The process by which neural networks learn how to improve individual parameters. You'll learn all about this in the upcoming lessons.
- [Numpy](http://www.numpy.org/) - An extremely popular library for scientific computing in python.
- [Tensorflow](http://tensorflow.org/) - One of the most popular python libraries for creating neural networks. It is maintained by Google.

### fast-style transfer

Looking at[an existing style transfer deep learning script](https://github.com/lengstrom/fast-style-transfer) to play around with. Hmm.. interesting to see what can be done but HOW is it done is the q?

### [Deep Traffic](http://selfdrivingcars.mit.edu/deeptrafficjs/) simulator

See the [overview](http://selfdrivingcars.mit.edu/deeptraffic/) for how to tinker with the inputs to train the simple neural network. Interesting to see how inputs drastically effect the quality of the output.

> [DeepTraffic](http://selfdrivingcars.mit.edu/deeptrafficjs/) is a gamified simulation of typical highway traffic. Your task is to build a neural agent – more specifically design and train a neural network that performs well on high traffic roads. Your neural network gets to control one of the cars (displayed in red) and has to learn how to navigate efficiently to go as fast as possible. The car already comes with a safety system, so you don’t have to worry about the basic task of driving – the net only has to tell the car if it should accelerate/slow down or change lanes, and it will do so if that is possible without crashing into other cars.

This neural net uses [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning)

### [Flappy Bird](https://github.com/yenchenlin/DeepLearningFlappyBird)

This is a deep learning agent which plays flappy bird. Not very useful at this point. Need to know to understand/use/train the flappybird playing agent!

So come back to this later.

### Siraj's intro to linear regression

he walks through linear regression, using numpy and then by building a gradient descent model.


### moving on to neural nets

- a neural network is an algorithm which identifies patterns in data
- Backpropagation trains a neural net by updating weights via gradient descent
- deep learning = many layer neural net + big data + big compute

## Backpropagation

This is the key to understanding neural nets, so it's important to understand how Backpropagation works.

- [CS231n Winter 2016 Lecture 4: Backpropagation](https://www.youtube.com/watch?v=59Hbtz7XgjM)


## Project 1: Predictin Bike Sharing demand from historical data

[Final Notebook](https://github.com/khalido/nd101-projects/blob/playing-with-numpy/dlnd-your-first-neural-network.ipynb)

# Week 2

## Model Evaluation and Validation

Generalization is better than overfitting.

R2 score
- simplest possible model is to take the avg of all values and draw a straight line, then calculate the mean square error
 - the R2 score is 1 minus the error of our regression model divided by the error of the simplest possible model
 - if we have a good model, the error will be small compared to the simple model, thus R2 will be close to 1
 - for a bad model, the ratio of errors will be closer to 1, giving a small R2 values

 from sklearn.metrics import r2_score

### Two types of error

- overfitting
- underfitting


# Week 3

## Sentiment Analysis with Andrew Trask

This was a good project - built a simple neural network to classify reviews as negative or positive.

## Intro to TFLearn

Sigmoid activation functions have a max derivate of .25, so errors shrink by 75% or more during backprogation. This means the neural network takes a long time to train. Instead of sigmoid, most DL networks use RLU - which is a supersimple function which outputs max(input, 0). For a +ve inut the output equals the input, and for a -ve input the output is 0. Relu nodes can die if there is a large graident through them, so they are best used with a small learning rate.

For a simple binary classification, the sigmoid function works, but for mulitple outputs, for example reconigizing digits, use the [softmax](https://en.wikipedia.org/wiki/Softmax_function) function. A softmax function squashes outputs to be b/w 0 and 1 and divides them such that the total sum of the output equals 1.

one hot encoding means using a simple vector, like `y=[0,0,0,0,1,0,0,0,0,0]` to represent 4.

http://tflearn.org/

## RNN

http://colah.github.io/posts/2015-08-Understanding-LSTMs/
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

## using tflearn to do sentiment Analysis


# Week 4

## Siraj's Math for Deep learning
Need to know statistics, linear algebra and calculus.
C

## Miniflow

built a simple graph based nn

an alternative to Amazon's EC2 gpu machines: [floyd](https://www.floydhub.com/)

# Week 5

## Intro to [Tensorflow](https://www.tensorflow.org/)

Deep learning is a family of techniques which adapts to all sorts of data and problems. the basic techiniques of DL apply to a bunch of diff fields. Neural Networks have been around for decades but had pretty much disappread from the CS science. They came back in a bigway in the 2010's with advances in speech reconizition, computer vision and machine translation. This was enabled by lots of data and cheap gpus.

All the hotness is in my [intro to tensorflow notebook](https://github.com/khalido/nd101/blob/master/intro_to_tensorflow.ipynb).

# Week 6

Going deeper into tensorflow!

### Preventing overfitting

**Early Termination**: stop training soon as you stop improving

**Regulariation** applies constrains - L2 regularization adds another term to the loss which penalizes large weights.

**Dropout** is an important technique - it randomly stops half the signals flowing throgh a layer, and multiplies by 2 the remaining signals. This forces the NN to make redundant representations for everything - so with only partial info it can predict the right answer.
During testing, you cancel the dropout to maximize the predictive power of the model.

**get rid of unnecessary info** For example, when reconigizing letters, the colors don't matter, so transform R,G,B values into grayscale by (R+G+B)/2.

**weight sharing** say you have two kittens in the same image. so it makes sense to train the same part of the network on each kitten. we do this be weight sharing.

**statistical invariants** things which don't change across time and space, like say the word kitten in a text, it always refers to kittens.

## Convolution Networks, or CNN

A CNN breaks up an image into many pieces and learns to first reconigzie basic shapes, lines, curves, then the more complex objects as combinations of the simpler shapes, then classifies the image by combining the complex objects together. A CNN can have many layers, with each layer capturing a different level of complexity.

Resources:

- It seems the time is now to read [this book on neural networks](http://neuralnetworksanddeeplearning.com/) and go through [cs231](http://cs231n.github.io/).
- This [article](https://hackernoon.com/learning-ai-if-you-suck-at-math-p5-deep-learning-and-convolutional-neural-nets-in-plain-english-cda79679bbe3#.yop1x41dy) is a nice simple overview of neural networks and builds a simple covnet network using keras.
- [A beginers guide to understanding n=cnovlutional networks](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)

## Siraj's Image Classification

## Project 2

Goal is to Classify images from the [CIFAR dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

A good time to watch this [video intro to Tensorflow](https://www.youtube.com/watch?v=vq2nnJ4g6N0).

My [final project notebook](https://github.com/khalido/nd101-projects/blob/master/dlnd_image_classification.ipynb).

Note: I only got 65% accuracy, but that was at 20 epochs. Running it at a hundred or so shuold bump up the accuracy over 70%, but I got tired of waiting for the model to train.

# Week 7

## Intro to Recurrent Neural Networks

http://colah.github.io/posts/2015-08-Understanding-LSTMs/

## aside

[Deep Learning chat](https://www.youtube.com/watch?v=8UQzJaa0HPU&feature=youtu.be)
https://deeplearning4j.org/word2vec

# Week 8

## Embeddings and Word2vec

[Word2Vec](https://en.wikipedia.org/wiki/Word2vec)

Notebook: https://github.com/udacity/deep-learning/tree/master/embeddings

# Week 9

## TensorBoard

This is really useful to see the initial model, and then to see what is happening while it's training.

- [tensorboard intro](https://youtu.be/eBbEDRsCmv4)
- [basic tensorboard intro](https://www.tensorflow.org/get_started/summaries_and_tensorboard)

Can also be used for [hyperparameter search](https://github.com/udacity/deep-learning/blob/master/tensorboard/Anna_KaRNNa_Hyperparameters.ipynb) by selecting diff combinations of parameters, writing them to a logstring and viewing the diff runs in tensorboard all nicely charted out.

todo: make a simple mnist NN with tensorboard summaries of different parameters. something like:

```python
for lstm_size in [128,256,512]:
    for num_layers in [1, 2]:
        for learning_rate in [0.002, 0.001]:
            log_string = 'logs/4/lr={},rl={},ru={}'.format(learning_rate, num_layers, lstm_size)
            writer = tf.summary.FileWriter(log_string)
```

# Week 10

RNN's and language generation

## how to make a text summarizer
.....

## Weight Initialization

The initial value of weights is very important to how well a NN trains. If all the weights start of the same, it makes it hard to update the weights since they end up all giving similar outputs, making it hard for the NN to learn.

Random weights work much better. Tensorflow's [tf.random_uniform()](https://www.tensorflow.org/api_docs/python/tf/random_uniform) is a good weight initilization function. Be default, tf.random.uniform picks float values uniformly spread b/w 0 and 1, which is decent, but we can do better.

Smart people have tested out different initial weights, and it seems using weights distributed around zero with a std dev around 0.1 works well, with tails cut off. Tensorflow has a built in function:

[tf.truncated_normal](https://www.tensorflow.org/api_docs/python/tf/truncated_normal) which generates a random normal distribution around zero with values > 2 std devs from the mean repicked. So making 3 weights would look someething like:

```python
weights = [
    tf.Variable(tf.truncated_normal(layer_1_weight_shape, stddev=0.1)),
    tf.Variable(tf.truncated_normal(layer_2_weight_shape, stddev=0.1)),
    tf.Variable(tf.truncated_normal(layer_3_weight_shape, stddev=0.1))
```
A normal distribution means that the weights will tend to be closer to the mean rather than uniformly distributed.

todo: run a simple network on MNIST with different weights and see in tensorboard
todo: find some approchable resources on weights

### weight initilizaiton resources

- [cs231n weight initilization](http://cs231n.github.io/neural-networks-2/#init) - supports the above method of small random weights centered on zero, but warns that smaller numbers aren't always better.


## Sentiment Prediction RNN


## Project 3 - Generate a TV Script

This was an interesting project - to generate new text after training a RNN network on a subset of Simpsons scripts, set in Moe's Cavern.

[Completed project 3 notebook](https://github.com/khalido/nd101-projects/blob/master/dlnd_tv_script_generation.ipynb)

# Week 11

## Transfer Learning

Training nerual networks can take a long time so we can take an exisiting pretrained network and use that to extract features or as the initial network to further build upon. Here, we use [VGGNet](https://arxiv.org/pdf/1409.1556.pdf).

I'm using a [pretrained VGG network from here](https://github.com/machrisaa/tensorflow-vgg).

## Language Translation

# Week 12

## Sequence to Sequence
is a kind of RNN network.

[tf.contrib.seq2seq](https://www.tensorflow.org/api_docs/python/tf/contrib/seq2seq)

Useful posts
- [Text Summarization with Amazon Reviews](https://medium.com/towards-data-science/text-summarization-with-amazon-reviews-41801c2210b)
- [Seq2Seq talk](https://www.youtube.com/watch?v=G5RY_SUJih4)
- [Stanford lectures on NLP using deep learning](https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)

## How to make a chatbot

Train a DNN to learn text and answers. Facebook has some [datasets to learn on](https://research.fb.com/downloads/babi/).

Using Keras it's relative straightforward. See [this implementation](https://github.com/fchollet/keras/blob/master/examples/babi_rnn.py).

## Reinforcement learning

Use rewards when things be done right. Here we look at Q-Learning.
Using negative rewards for bad stuff, and postiive rewards for good stuff, you train an agent to seek out the max reward path, using a q-table which stores rewards for each state and action possible from that state.

[OpenAI Gym](https://gym.openai.com) has lots of implementations.

[basic RL](https://medium.com/@tuzzer/cart-pole-balancing-with-q-learning-b54c6068d947)

## Project 4 - Translation

use a rnn to translate english to french.

Project is built on TF 1.0, so see [release notes](https://github.com/tensorflow/tensorflow/blob/master/RELEASE.md) for later versions as TF changed some RNN bits.

I had a problem with training times. Even on a GPU it took forever. This is with relatively limited data, with a decently sized data it will take a looong time!

Questions to ponder:

- should the encoding & decoding embed size be exactly the vocab size?



**Parameters which should give > 90% accuracy:**

- epochs = 3
- batch_size = 256
- rnn_size = 128
- num_layers = 2
- encoding_embedding_size = 256
- decoding_embedding_size = 256
- learning_rate = 0.005
- keep_probability = 0.9

## GANS

Gans use a differentiable function represented by a NN to transform an output from an input (generally random noise?).

A second network, called the discriminator, which is just a regular NN classifier which has been trained on real images, gives the generated image a probablity of being real or fake. The discriminator receives a mix of real images and generated images.

Over time, the generator gets good at generating images which passes the discrimator's test.

Game theory tells us that the two NN's should come to a equilibrium where neither NN can improve their situation.

We train both networks alternately - look up best practices.
 

- [GAN by Example using Keras](https://medium.com/towards-data-science/gan-by-example-using-keras-on-tensorflow-backend-1a6d515a60d0)
- [another blog post](https://medium.com/intuitionmachine/deep-adversarial-learning-is-finally-ready-and-will-radically-change-the-game-f0cfda7b91d3)
- [Original GAN paper](https://arxiv.org/pdf/1406.2661.pdf)
- [OpenAI GAN explainer](https://blog.openai.com/generative-models/)
- [Quora GANs topic](https://www.quora.com/topic/Generative-Adversarial-Networks-1)

### Batch normalization

This greatly aids deep networks to learn faster, as well so stops them flaking out and killing too many neurons.

### Face generation project

A GAN which generates mnist images and faces.
Relatively straigtforward, but adding in [batch normalization](https://github.com/udacity/deep-learning/blob/master/batch-norm/Batch_Normalization_Lesson.ipynb) involves some tensorflow kungfu. Doing this project in TF made me yearn for Keras.

Specifically, the [batch_norm layer in TF](https://www.tensorflow.org/api_docs/python/tf/layers/batch_normalization) isn't magical enough, so we have to wrap the train operations inside tf.control_dependencies block so the batch normalization layers get updated. The below is the code from [Udacty](https://github.com/udacity/deep-learning/blob/master/dcgan-svhn/DCGAN.ipynb) but since I added batch norm to both the generator and the discriminator this didn't work for me:

```python
with tf.control_dependencies(tf.get_collection(tf.GraphKeys.UPDATE_OPS)):
        d_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(d_loss, var_list=d_vars)
        g_train_opt = tf.train.AdamOptimizer(learning_rate, beta1=beta1).minimize(g_loss, var_list=g_vars)
```

After much googling and help from the forums, this worked:

```python
# need this to make batch normalization work properly during inference
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
    g_updates  = [opt for opt in update_ops if opt.name.startswith('generator')]
    
    with tf.control_dependencies(g_updates):
        d_train_opt = tf.train.AdamOptimizer(learning_rate, beta1).minimize(d_loss, var_list=d_vars)
        g_train_opt = tf.train.AdamOptimizer(learning_rate, beta1).minimize(g_loss, var_list=g_vars)
```

Putting this here becuase there must be better/simpler easier way to do batch_norm without getting into the graph bowels of tensorflow.

todo: reimplement in Keras

[Project notebok](https://github.com/khalido/nd101-projects/blob/master/dlnd_face_generation.ipynb)

## All done!

Link to the official [course certificate](https://confirm.udacity.com/FMMYQCGE).