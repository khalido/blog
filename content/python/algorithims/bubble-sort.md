
bubble sort all the things


```python
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display

import random
import numpy as np
```

First up, generating a random list to sort then actually sorting it:


```python
data = [random.randint(0,100) for i in range(100)]
plt.title("The Unsorted data")
plt.bar(np.arange(len(data)), data)
plt.show()

def bubble_sort(data):
    done = False
    while not done:
        swapped = False
        for i in range(0, len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
        if not swapped:
            done = True
        
    return data

plt.title("All sorted")
plt.bar(np.arange(len(data)), bubble_sort(data));
```


![png](bubble-sort_3_0.png)



![png](bubble-sort_3_1.png)


# eyeballing bubble sort

todo for now, using plotly or some other library.


```python
NUMS = 10
x = np.arange(NUMS)
y = np.random.randint(0, 100, size=NUMS)
x,y
```




    (array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
     array([97,  4, 97,  7, 84, 92, 84, 53, 59, 76]))



changing bubble sort to get back a list containing all the steps from the initial list to the final sorted list:


```python
def bubble_sort_2(data):
    done = False
    all_the_sorts = []
    all_the_sorts.append(data)
    while not done:
        swapped = False
        for i in range(0, len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                all_the_sorts.append(data)
                swapped = True
        if not swapped:
            done = True
        
    return all_the_sorts

print(y)
bs_sorts = bubble_sort_2(y)
bs_sorts
```

    [97  4 97  7 84 92 84 53 59 76]





    [array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97]),
     array([ 4,  7, 53, 59, 76, 84, 84, 92, 97, 97])]



now to eyeball it:


```python
y = bs_sorts
fig, ax = plt.subplots()
fig.set_size_inches(8,6)
ax.set_title("Bubble Sort")
ax.set_xlabel('X')
ax.set_ylabel('Y')

# this displays the data to be sorted as a scatter plot
original_line = ax.scatter(x,y[0], alpha = 0.2, label = "original data")
# the final sorted line.
sorted_line = ax.plot(x,y[-1], lw=2, alpha = 0.7, label="sorted")

# this displays the data being sorted in a scatter plot
scatterplot = ax.scatter(x,y[0], label="sorting")

def animate(i):
    scatterplot.set_offsets(np.c_[x,y[i]])

ani = animation.FuncAnimation(fig, animate, 
                frames=len(y), interval=150, repeat=False) 

#print(f"it took {len(qs_steps)-1} steps to sort {len(qs_steps[0])} items")
plt.legend()
ani.save("bubblesort_animate.mp4")
```

    WARNING:matplotlib.animation:MovieWriter ffmpeg unavailable.



    --------------------------------------------------------------------------

    ValueError                               Traceback (most recent call last)

    <ipython-input-106-e7558f6a9a3e> in <module>()
         22 #print(f"it took {len(qs_steps)-1} steps to sort {len(qs_steps[0])} items")
         23 plt.legend()
    ---> 24 ani.save("bubblesort_animate.mp4")
    

    /data/data/com.termux/files/usr/lib/python3.6/site-packages/matplotlib/animation.py in save(self, filename, writer, fps, dpi, codec, bitrate, extra_args, metadata, extra_anim, savefig_kwargs)
       1190                           "animation.")
       1191                 rcParams['savefig.bbox'] = None
    -> 1192             with writer.saving(self._fig, filename, dpi):
       1193                 for anim in all_anim:
       1194                     # Clear the initial frame


    /data/data/com.termux/files/usr/lib/python3.6/contextlib.py in __enter__(self)
         79     def __enter__(self):
         80         try:
    ---> 81             return next(self.gen)
         82         except StopIteration:
         83             raise RuntimeError("generator didn't yield") from None


    /data/data/com.termux/files/usr/lib/python3.6/site-packages/matplotlib/animation.py in saving(self, fig, outfile, dpi, *args, **kwargs)
        235         '''
        236         # This particular sequence is what contextlib.contextmanager wants
    --> 237         self.setup(fig, outfile, dpi, *args, **kwargs)
        238         try:
        239             yield self


    /data/data/com.termux/files/usr/lib/python3.6/site-packages/matplotlib/animation.py in setup(self, fig, outfile, dpi, frame_dir)
        885         root, ext = os.path.splitext(outfile)
        886         if ext not in ['.html', '.htm']:
    --> 887             raise ValueError("outfile must be *.htm or *.html")
        888 
        889         if not self.embed_frames:


    ValueError: outfile must be *.htm or *.html



![png](bubble-sort_9_2.png)



```python

```
