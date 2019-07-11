
# Read in a file

Pandas needs data to work with, and the most common way to get it is to read it in the form of a csv file.

Pandas will attempt to deal with most common csv file stuff automatically, so you can just point it to a csv file like the example below and it should just work. Pandas automatically treats the first line as a header, which is how this file is setup.


```python
from collections import namedtuple
import numpy as np
import pandas as pd

# by default pandas treats the first line of data as the column names. use `header=None` if no names
fandango = pd.read_csv("data/fandango_score_comparison.csv") #pandas attempts to parse it best it can
fandango.head(2)
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
      <th>FILM</th>
      <th>RottenTomatoes</th>
      <th>RottenTomatoes_User</th>
      <th>Metacritic</th>
      <th>Metacritic_User</th>
      <th>IMDB</th>
      <th>Fandango_Stars</th>
      <th>Fandango_Ratingvalue</th>
      <th>RT_norm</th>
      <th>RT_user_norm</th>
      <th>...</th>
      <th>IMDB_norm</th>
      <th>RT_norm_round</th>
      <th>RT_user_norm_round</th>
      <th>Metacritic_norm_round</th>
      <th>Metacritic_user_norm_round</th>
      <th>IMDB_norm_round</th>
      <th>Metacritic_user_vote_count</th>
      <th>IMDB_user_vote_count</th>
      <th>Fandango_votes</th>
      <th>Fandango_Difference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avengers: Age of Ultron (2015)</td>
      <td>74</td>
      <td>86</td>
      <td>66</td>
      <td>7.1</td>
      <td>7.8</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>3.70</td>
      <td>4.3</td>
      <td>...</td>
      <td>3.90</td>
      <td>3.5</td>
      <td>4.5</td>
      <td>3.5</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>1330</td>
      <td>271107</td>
      <td>14846</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Cinderella (2015)</td>
      <td>85</td>
      <td>80</td>
      <td>67</td>
      <td>7.5</td>
      <td>7.1</td>
      <td>5.0</td>
      <td>4.5</td>
      <td>4.25</td>
      <td>4.0</td>
      <td>...</td>
      <td>3.55</td>
      <td>4.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>249</td>
      <td>65709</td>
      <td>12640</td>
      <td>0.5</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 22 columns</p>
</div>




```python
fandango["FILM"][:2].values
```




    array(['Avengers: Age of Ultron (2015)', 'Cinderella (2015)'],
          dtype=object)



# A small dataset
A small data set with no initial column headers


```python
# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel','bob', 'Mary']
births = [968, 155, 77, 578, 973, 100,55]
BabyDataSet = list(zip(names,births))
BabyDataSet
```




    [('Bob', 968),
     ('Jessica', 155),
     ('Mary', 77),
     ('John', 578),
     ('Mel', 973),
     ('bob', 100),
     ('Mary', 55)]




```python
df = pd.DataFrame(data=BabyDataSet)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bob</td>
      <td>968</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jessica</td>
      <td>155</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mary</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>John</td>
      <td>578</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mel</td>
      <td>973</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bob</td>
      <td>100</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mary</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns=['Names', 'Birth_Rates']
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Birth_Rates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bob</td>
      <td>968</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jessica</td>
      <td>155</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mary</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>John</td>
      <td>578</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mel</td>
      <td>973</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bob</td>
      <td>100</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mary</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Names']
```




    0        Bob
    1    Jessica
    2       Mary
    3       John
    4        Mel
    5        bob
    6       Mary
    Name: Names, dtype: object




```python
name_list = [str(name).lower() for name in df['Names']]
print(name_list)
name_string = " ".join(name_list)
name_string
```

    ['bob', 'jessica', 'mary', 'john', 'mel', 'bob', 'mary']





    'bob jessica mary john mel bob mary'




```python
names = name_string.split()
names
```




    ['bob', 'jessica', 'mary', 'john', 'mel', 'bob', 'mary']




```python
from collections import Counter
c = Counter(names)
d = c.most_common(3) #makes a list of tuples with the 3 most common names
d
```




    [('mary', 2), ('bob', 2), ('john', 1)]



Making a list of common words


```python
n = []
for i in d:
    n.append(i[0])
n
```




    ['mary', 'bob', 'john']




```python
df
```




    0                       BobBobBobBobBobBobBobBobBobBob
    1    JessicaJessicaJessicaJessicaJessicaJessicaJess...
    2             MaryMaryMaryMaryMaryMaryMaryMaryMaryMary
    3             JohnJohnJohnJohnJohnJohnJohnJohnJohnJohn
    4                       MelMelMelMelMelMelMelMelMelMel
    5                       bobbobbobbobbobbobbobbobbobbob
    6             MaryMaryMaryMaryMaryMaryMaryMaryMaryMary
    Name: Names, dtype: object




```python
a = df['Names'].value_counts()
a
```




    Mary       2
    John       1
    Jessica    1
    Mel        1
    bob        1
    Bob        1
    Name: Names, dtype: int64




```python
a[:3]
```




    Mary       2
    John       1
    Jessica    1
    Name: Names, dtype: int64




```python
for it,row in a[:2].items():
    print(it,row)
```

    Mary 2
    John 1



```python
df['Names'].apply(lambda x: x*2)
```




    0            BobBob
    1    JessicaJessica
    2          MaryMary
    3          JohnJohn
    4            MelMel
    5            bobbob
    6          MaryMary
    Name: Names, dtype: object




```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Birth_Rates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bob</td>
      <td>968</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jessica</td>
      <td>155</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mary</td>
      <td>77</td>
    </tr>
    <tr>
      <th>3</th>
      <td>John</td>
      <td>578</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Mel</td>
      <td>973</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bob</td>
      <td>100</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mary</td>
      <td>55</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Birth_Rates'] = df['Birth_Rates'].apply(lambda x: x/10)
```
