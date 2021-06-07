---
title: KNN algorithim
description: a simple knn algo implementation
date: 2018-08-10
toc: true
tags:
- algorithims
---


```python
#hide
import numpy as np
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display
```

K Nearest Neighbours is a algorithim for finding out the similarity or distance b/w two things, to find out how alike/different they are. 

Say we have a bunch of fruit, KNN will classify them into clusters by using what we know - with fruit this would be shape, size, weight, color, etc.

Anyways, lets start with the Iris dataset, which has 150 measurements of flowers:


```python
iris = sns.load_dataset("iris")
print(f"Iris dataset shape: {iris.shape}")
iris.head()
```

    Iris dataset shape: (150, 5)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



Now I'm sampling 5 random flowers from this data set so we can use our fancy new KNN algo to determine what kind of flower they are later on:


```python
test = iris.sample(n=5)
test
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>5.8</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.9</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>104</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.8</td>
      <td>2.2</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>69</th>
      <td>5.6</td>
      <td>2.5</td>
      <td>3.9</td>
      <td>1.1</td>
      <td>versicolor</td>
    </tr>
  </tbody>
</table>
</div>



And here I am deleting the sampled flowers from the iris dataset to make sure our algo hasn't seem the test flowers:


```python
iris.drop(test.index, inplace=True)
print(iris.shape)
```

    (145, 5)


Now to look at the data visually:


```python
sns.pairplot(data=iris, hue="species");
```


    
![svg](knn_files/knn_9_0.svg)
    


It's pretty clear the the species are different, though there is some overlap at the boundaries.

Looking at petal length variation across species:


```python
sns.boxplot(x="species", y="petal_length", data=iris);
```


    
![svg](knn_files/knn_11_0.svg)
    


Now to actually write the algorithim and figure out what species the flowers in the test data set belong to.

First, a helper function to calculate the distance b/w points:


```python
def distance(x, y):
    """returns distance b/w two points x and y"""
    assert len(x) == len(y)
    inner = 0
    for a, b in zip(x,y):
        inner += (a - b)**2
    return np.sqrt(inner)
    
distance((1,5),[5,5])
```




    4.0



lets look at the values of the first flower in our test data and see if we can figure out what it is by using KNN:


```python
test.iloc[0]
```




    sepal_length          5.8
    sepal_width           2.7
    petal_length          5.1
    petal_width           1.9
    species         virginica
    Name: 101, dtype: object




```python
def knn(item, data, n=3):
    """takes in an item to check and a dataset, of size 4 features each
    returns the first n closest neighbours as a tuple (loc, distance)"""
    dist = []
    for i, row in data.iterrows():
        dist.append((i, distance(row[:4], item)))
        
    nearest = sorted(dist, key=lambda x: x[1])[:n]
    species = [iris.loc[i[0]]["species"] for i in nearest]
    
    return Counter(species).most_common()[0][0]

knn(test.iloc[0][:4], iris)
```




    'virginica'




```python
knn_species = []
for i, row in test.iterrows():
    knn_species.append(knn(row[:4], iris))
knn_species
```




    ['virginica', 'setosa', 'virginica', 'virginica', 'versicolor']




```python
test["knn"] = knn_species
test
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
      <th>knn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>101</th>
      <td>5.8</td>
      <td>2.7</td>
      <td>5.1</td>
      <td>1.9</td>
      <td>virginica</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>104</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.8</td>
      <td>2.2</td>
      <td>virginica</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>147</th>
      <td>6.5</td>
      <td>3.0</td>
      <td>5.2</td>
      <td>2.0</td>
      <td>virginica</td>
      <td>virginica</td>
    </tr>
    <tr>
      <th>69</th>
      <td>5.6</td>
      <td>2.5</td>
      <td>3.9</td>
      <td>1.1</td>
      <td>versicolor</td>
      <td>versicolor</td>
    </tr>
  </tbody>
</table>
</div>



All right! our KNN algo got all the 5 test species right!

I wrote this KNN algo a bit specifically targeting the iris dataset, but it can be modified to deal with with many different data sets.

The iris dataset is very simple, but usually I would normalize the data so all the attributes get a chance to effect the rating. 
