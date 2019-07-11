
--- 
title: "ISLR in Python"  
date: 2019-07-05
description: "Python implementation of the code in ISLR" 
draft: false 
tags:
- python
---

These are my notes and code in python as I read through [An Introduction to Statistical Learning](http://faculty.marshall.usc.edu/gareth-james/ISL/). The book is in R, I prefer python so here goes.


```python
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
```

# 1: Introduction

## Data Sets

The books uses [a few different data sets](http://faculty.marshall.usc.edu/gareth-james/ISL/data.html) and chp 1 introduces three of them:

### Wages


```python
df = pd.read_csv("data/Wage.csv")
df["education_level"] = df["education"].apply(lambda x: int(x.split(".")[0]))
df.head(2)
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
      <th>Unnamed: 0</th>
      <th>year</th>
      <th>age</th>
      <th>sex</th>
      <th>maritl</th>
      <th>race</th>
      <th>education</th>
      <th>region</th>
      <th>jobclass</th>
      <th>health</th>
      <th>health_ins</th>
      <th>logwage</th>
      <th>wage</th>
      <th>education_level</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>231655</td>
      <td>2006</td>
      <td>18</td>
      <td>1. Male</td>
      <td>1. Never Married</td>
      <td>1. White</td>
      <td>1. &lt; HS Grad</td>
      <td>2. Middle Atlantic</td>
      <td>1. Industrial</td>
      <td>1. &lt;=Good</td>
      <td>2. No</td>
      <td>4.318063</td>
      <td>75.043154</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>86582</td>
      <td>2004</td>
      <td>24</td>
      <td>1. Male</td>
      <td>1. Never Married</td>
      <td>1. White</td>
      <td>4. College Grad</td>
      <td>2. Middle Atlantic</td>
      <td>2. Information</td>
      <td>2. &gt;=Very Good</td>
      <td>2. No</td>
      <td>4.255273</td>
      <td>70.476020</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig, axes = plt.subplots(1,3, figsize=(14,5))

# Ax1: Wage vs Age scatterplot and trend line
sns.regplot(x="age", y="wage", order=6, data=df, ax=axes[0], 
            scatter_kws={'alpha':0.15, "color": "grey"})

axes[0].set_title("Wages vs Age")

# Ax2: Wage per Year
axes[1].set_title("Wages and Years")
sns.regplot(x="year", y="wage", data=df, order=1, ax=axes[1], 
            scatter_kws={'alpha':0.15, "color": "grey"})

# Ax3: Wage per Year
axes[2].set_title("Education Level vs Wages")
sns.boxplot(x="education_level", y="wage", data=df, ax=axes[2]);
```


![png](intro_to_statistical_learning_6_0.png)


### Stock Market Data

This has the daily movements in the Standard & Poor’s 500 (S&P) stock index over a 5-year period between 2001 and 2005.


```python
df = pd.read_csv("data/Smarket.csv")
df.head(2)
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
      <th>Unnamed: 0</th>
      <th>Year</th>
      <th>Lag1</th>
      <th>Lag2</th>
      <th>Lag3</th>
      <th>Lag4</th>
      <th>Lag5</th>
      <th>Volume</th>
      <th>Today</th>
      <th>Direction</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2001</td>
      <td>0.381</td>
      <td>-0.192</td>
      <td>-2.624</td>
      <td>-1.055</td>
      <td>5.010</td>
      <td>1.1913</td>
      <td>0.959</td>
      <td>Up</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2001</td>
      <td>0.959</td>
      <td>0.381</td>
      <td>-0.192</td>
      <td>-2.624</td>
      <td>-1.055</td>
      <td>1.2965</td>
      <td>1.032</td>
      <td>Up</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig, axes = plt.subplots(1,3, figsize=(14,5))
```
