
# Binary search

Binary search is a divide and conquer search algorithim. It takes a sort array or list of items, say a phone dictionary of names, and looks for each item in the middle of the list. If the item in the middle of the list is bigger than the item to be found, it discards the top half of the list, and if the middle is smaller, it discards the bottom half of the list.

### Sources

- [Khan Academy](https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search)
- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)


```python
def binary_search(list, item, verbose=False):
    """takes in item and a sorted list. returns position of item if found in the list
    or returns None if item isn't there"""
    
    low = 0
    high = len(list) - 1
    
    count = 1
    while low <= high:
        mid = (low + high) // 2 # discards the decimal
        if verbose: print("Pass {}, the middle value is: {} ".format(count, list[mid]))
        if list[mid] == item:
            if verbose==True: print("Eureka! Found {} after {} passes".format(item, count))
            return mid
        elif list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
        count += 1
```


```python
items = [i*2 for i in range(100)]
items[:5], items[-5:]
```




    ([0, 2, 4, 6, 8], [190, 192, 194, 196, 198])




```python
binary_search(items, 2, verbose=True)
```

    Pass 1, the middle value is: 98 
    Pass 2, the middle value is: 48 
    Pass 3, the middle value is: 22 
    Pass 4, the middle value is: 10 
    Pass 5, the middle value is: 4 
    Pass 6, the middle value is: 0 
    Pass 7, the middle value is: 2 
    Eureka! Found 2 after 7 passes





    1



Binary search halves the list on each pass. So the max passes through quicksort is the log of the length of the array:


```python
import math
math.ceil(math.log2(len(items)))
```




    7



## testing time it takes to run


```python
print('length', len(items))
%timeit binary_search(items,2)
```

    length 100
    100000 loops, best of 3: 2.88 µs per loop



```python
items = [i*2 for i in range(100000)]
print('length', len(items))
%timeit binary_search(items,2)
```

    length 100000
    100000 loops, best of 3: 7.4 µs per loop



```python

```
