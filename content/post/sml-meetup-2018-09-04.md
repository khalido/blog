---
title: "SML 2018-09: Deep Reinforcement Learning"
date: 2018-09-04
tags:
- meetup
---

SML's [2018-09 meetup](https://www.meetup.com/Sydney-Machine-Learning/events/253797245/).

- [STEM Careers expo on Thu 6th Sep](https://www.eventbrite.com.au/e/emerge-2018-stem-careers-expo-tickets-46959173151)

the talks:

## Kosuke Fujimoto: How can we innovate our workstyle at construction sites with Image Classification?

> Kosuke, Takenaka Corporation is one of the top 5 largest construction companies in Japan. Their site supervisors perform site visits, record the progress of ongoing construction as well as assign appropriate resourcing from their workforce by writing up the report every evening. This involves taking a lot of photos and organizing them based on the construction progress.

> In this talk, I walk you through an effort by Takenaka with help from Microsoft to automatically organize photos utilizing Keras and Transfer Learning to make workstyle innovation at construction sites possible.

- [github](https://github.com/fujikosu)
- Takanaka is a huge consturction company in Japan
- so much demand that only 5.7% of employees get 2 days a week, plus working population is decreasing
  - need to make work more efficent
- lots of photo related tasks - construction management relies on photos for order, evidence & education
  - manually organised, takes lots of time
  - 100 millions photos taken yearly
- Used transfer learning with 10K photos split: train/test/valid split: 7,2,1 for a trial
- You don't need heaps of photos for transfer learning, the pretrained models have already been trained on heaps of data. 
- Keras has a [bunch of pretrained models](https://keras.io/applications/) ready to use.
- We have to run a bunch of experiments to figure out stuff. [Azure Machine Learning Services has lots of tools for experimentation](https://docs.microsoft.com/en-us/azure/machine-learning/desktop-workbench/experimentation-service-configuration).
- see https://github.com/fujikosu/aml-keras-image-recognition
- think about data augmentation - Keras's built in functions for this are great	

The company's example was really powerful - a very small amount of deep learning solved a very big problem, since transfer learning and the cloud is making vision problems much easier to deal with.

## Krit Kamtuo: Using Batch AI to train NLP based on Tensorflow and CNTK in the retail industry

> Currently, SSG.COM, the subsidiary of Shinsegae Group the largest retailer in South Korea, is developing an AI chatbot service based on deep learning. It was decided that the internet as as service-based architecture is not efficient because it requires additional resources if the operation production scale is increased.
>
> We will discuss why the AI model training layer does not have to be running at all times but the GPU-supported VM should be used continuously, to reduce costs to SSG.COM.

- @kritcs18, [github](https://github.com/taeyo)
- ssg.com is the largest retailer in South Korea, was working on a AI chatbot based on deep learning
- pretty complex and expensive architecture, wanted to migrate to the cloud (PaaS)
- shifed to a serverless model with API gateways
- [MS Azure Batch AI](https://azure.microsoft.com/en-us/services/batch-ai/) takes care of all the hardware, you focus on the work which needs to happen. Looks pretty pimp. The era of spinning up your own VM is fast ending.
  - suited for bigCo for sure, but for personal experiments there is too much configuration code (for now). 

> Batch AI is a managed service that enables data scientists and AI researchers to train AI and other machine learning models on clusters of Azure virtual machines, including VMs with GPU support. You describe the requirements of your job, where to find the inputs and store the outputs, and Batch AI handles the rest.

Interesting becuase companies are moving from running their own hardware, to hardware in the cloud, and now on to running apps themselves with the hardware spin up spin down somewhat abstracted (or in the process of getting so).


## Matt Gibson: Learning with not quite the right labels

> Having the right data is often as important as having the right model for building effective computer vision systems. Even if you have enough data, what do you do when don't have the right labels? Common problems arising in image understanding include only having partially labelled data, have the wrong type of labels and noisy labels. Broadly these problems can be addressed by an area of research called weakly supervised learning. I will give an overview of some strategies coming from weakly supervised learning to help train good predictive models in the presence of these difficulties. The tools used will include ConvNets combined with some interesting applications of familiar friends such as the EM algorithm and graph-based clustering.

- 
