---
title: "Apache Spark"
description: started some notes on Spark, but didn't get very far...
category: [data science]
date: 2016-01-01
toc: false
---

# Apache Spark

Way back in the good old days Google came up with mapreduce to store and crunch data scattered on disks across multiple machines. The world looked at mapreduce and thought it good, and made an open source implementation called Hadoop.

Ppl wanted more, and faster, and luckily memory prices went down. And thus Apache Spark was born at UC Berkely. Spark stores data across a bunch of machines in memory. This makes it easy and fast to data scientist all the data.

## RDD

The key buzzword here is RDD which stands for resilient distributed data set. Spark has a `SparkContext` object which manages the connection to clusters and how processes are run on those clusters. So we call it using code like `data = sc.textFile(``'``name_of_text_file.txt``'``)`. With text data, this just becomes a list of strings - one per each line in the text file which is accessed using `sc.take(num_of_lines)`.

Now, even though this looks very pythonic, don’t think of spark data objects which look like lists as lists. Python lists are meant to be run on a single machine, so they can be sliced and diced. Spark data is designed to be used across machines, so slices don’t make sense in that context.

RDD's are immutable - so to modify data stored inside it, we get back a new RDD. Python has both mutable objects - like lists and dictionaries - and immutable ones like tuples, so this isn't anything different from mainstream python.

## map all the things to something else

`map(func)` applies the function `func` to all the things in the RDD and returns a new RDD. so something like `data.map(lambda line: line.split('\t'))` applies the func passed into map to each object stored in the RDD and returns back a new RDD.

`map` is often accompanies by [reduceByKey](https://spark.apache.org/docs/latest/rdd-programming-guide.html#ReduceByLink) e.g to count stuff:

```python
lines = sc.textFile("data.txt")
pairs = lines.map(lambda s: (s, 1))
counts = pairs.reduceByKey(lambda a, b: a + b)
```

Now, spark deals with transformations only when it has to - so it builds up a pipelines of tasks and runs them when the output of those tasks is called.

## install spark on your local machine

Use Spark on a local machine is useful for learning purposes - for actual production use I would use [Amazon EMR](https://aws.amazon.com/emr/) or [Google Cloud Dataproc](https://cloud.google.com/dataproc/).

Spark needs Java, so to install it properly it needs a lot of installation. So to avoid all that I'm using a [docker](https://docs.docker.com/get-started/) image with spark preinstalled: [jupyter/pyspark-notebook](http://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-pyspark-notebook)

`docker run -d -P --name notebook jupyter/pyspark-notebook`

Note: use `-v` to mount the current directory in the docker container.