
## the famous [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz):

- count from 1 to x
- numbers divisible by 3 are Fizz
- numbers divisible by 5 are Buzz
- numbers divisible by 15 are FizzBuzz


```python
def fizzbuzz(n):
    """prints 1 to n, replacing:
    Fizz for numbers divisible by 3
    Buzz for numbers divisible by 5
    FizzBuxzz for numbers divisible by 15"""
    
    for i in range(1,n):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i %5 == 0:
            s += "Buzz"
        
        print(s) if len(s) else print(i)

fizzbuzz(100)
```

    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz
    Fizz
    22
    23
    Fizz
    Buzz
    26
    Fizz
    28
    29
    FizzBuzz
    31
    32
    Fizz
    34
    Buzz
    Fizz
    37
    38
    Fizz
    Buzz
    41
    Fizz
    43
    44
    FizzBuzz
    46
    47
    Fizz
    49
    Buzz
    Fizz
    52
    53
    Fizz
    Buzz
    56
    Fizz
    58
    59
    FizzBuzz
    61
    62
    Fizz
    64
    Buzz
    Fizz
    67
    68
    Fizz
    Buzz
    71
    Fizz
    73
    74
    FizzBuzz
    76
    77
    Fizz
    79
    Buzz
    Fizz
    82
    83
    Fizz
    Buzz
    86
    Fizz
    88
    89
    FizzBuzz
    91
    92
    Fizz
    94
    Buzz
    Fizz
    97
    98
    Fizz


## Now to try a list comprehension


```python
[(not i%3)*"Fizz" + (not i%5)*"Buzz" or i for i in range(1,100)]
```




    [1,
     2,
     'Fizz',
     4,
     'Buzz',
     'Fizz',
     7,
     8,
     'Fizz',
     'Buzz',
     11,
     'Fizz',
     13,
     14,
     'FizzBuzz',
     16,
     17,
     'Fizz',
     19,
     'Buzz',
     'Fizz',
     22,
     23,
     'Fizz',
     'Buzz',
     26,
     'Fizz',
     28,
     29,
     'FizzBuzz',
     31,
     32,
     'Fizz',
     34,
     'Buzz',
     'Fizz',
     37,
     38,
     'Fizz',
     'Buzz',
     41,
     'Fizz',
     43,
     44,
     'FizzBuzz',
     46,
     47,
     'Fizz',
     49,
     'Buzz',
     'Fizz',
     52,
     53,
     'Fizz',
     'Buzz',
     56,
     'Fizz',
     58,
     59,
     'FizzBuzz',
     61,
     62,
     'Fizz',
     64,
     'Buzz',
     'Fizz',
     67,
     68,
     'Fizz',
     'Buzz',
     71,
     'Fizz',
     73,
     74,
     'FizzBuzz',
     76,
     77,
     'Fizz',
     79,
     'Buzz',
     'Fizz',
     82,
     83,
     'Fizz',
     'Buzz',
     86,
     'Fizz',
     88,
     89,
     'FizzBuzz',
     91,
     92,
     'Fizz',
     94,
     'Buzz',
     'Fizz',
     97,
     98,
     'Fizz']




```python

```
