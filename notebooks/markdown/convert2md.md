---
title: Jupyter notebooks to markdown

date: 2020-11-10
tags: [python]
summary: "using nbdev to convert notebooks to markdown"
description: "using nbdev to convert notebooks to markdown"
---


This is very meta, but since I only update notebooks once in a while, this here notebook converts all the notebooks in the folder to markdown files and images, which are used to build the blog posts on the site.

The main reason to do this is to save time when rebuilding the blog on github pages, as installing nbdev and converting all the notebooks takes a while.

Later on could add an option to the config to either build notebooks on each build or to just read the converted markdown files.

<div class="codecell" markdown="1">
<div class="input_area" markdown="1">
<details class="description">
    <summary>Code details ...</summary>
    
```python
#collapse-hide
import os
from pathlib import Path
from nbdev.export2html import convert_md
```

</details>

</div>

</div>

Settings used:
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
path_nb: Path = Path(".") # convert notebook is in the notebooks folder

path_md = path_nb / "markdown"
path_nb, path_md, str(path_md)
```

</div>
<div class="output_area" markdown="1">




    (Path('.'), Path('markdown'), 'markdown')



</div>

</div>

helper functions:
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
def make_folder(path, debug: bool = False):
    """makes parent folders if they don't exist for a path"""

    # assume the last thing is a file if there is a dot in the name
    if "." in path.name:
        path = path.parent

    try:
        path.mkdir(parents=True, exist_ok=False)
        if debug:
            print(f"{path} folder made")
    except FileExistsError:
        if debug:
            print(f"{path} folder already exists")
        pass
```

</div>

</div>

Now to convert all the jupyter notebooks to markdown files:
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
nb_paths = [
        f for f in path_nb.rglob("*.ipynb") if ".ipynb_checkpoints" not in str(f)
    ]

print(f"Converting {len(nb_paths)} notebooks to markdown files.")

for nb_path in nb_paths:
    print(f"converting {nb_path}")
    path_img = path_md / f"{nb_path.stem}_files"
    make_folder(path_img) # make _files folder inside markdown output folder
    convert_md(nb_path, dest_path=path_md, img_path=None, jekyll=True)
    # remove extra empty files folder made by nbdev
    Path(path_img.stem).rmdir()
```

</div>
<div class="output_area" markdown="1">

    Converting 9 notebooks to markdown files.
    converting flood_fill.ipynb
    converting knn.ipynb
    converting blogging_with_jupyter_notebooks.ipynb
    converting Advent-of-Code-2015.ipynb
    converting monty_hall.ipynb
    converting quicksort.ipynb
    converting convert2md.ipynb
    converting us_elections_2020.ipynb
    converting monte_carlo_pi.ipynb


</div>

</div>

So now in the markdown output folder we have a list of `.md` files, with each file having a `_files` folder containing output artifacts for that notebook.
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
os.listdir(path_md)
```

</div>
<div class="output_area" markdown="1">




    ['monte_carlo_pi_files',
     'monty_hall.md',
     'flood_fill_files',
     'us_elections_2020_files',
     'convert2md.md',
     'Advent-of-Code-2015_files',
     'Advent-of-Code-2015.md',
     'knn_files',
     'quicksort_files',
     'blogging_with_jupyter_notebooks.md',
     'blogging_with_jupyter_notebooks_files',
     'knn.md',
     'monte_carlo_pi.md',
     'convert2md_files',
     'flood_fill.md',
     'us_elections_2020.md',
     'quicksort.md',
     'monty_hall_files']



</div>

</div>

Taking a look at a sample md file:
<div class="codecell" markdown="1">
<div class="input_area" markdown="1">

```python
txt = [p for p in path_md.rglob("*.md")][0].read_text()
print(txt[:1000])
```

</div>
<div class="output_area" markdown="1">

    ---
    title: Monty Hall
    
    date: 2019-07-05
    tags: [python]
    summary: "Monty Hall brain teaser"
    description: "Monty Hall brain teaser"
    ---
    
    
    The famous [Monty Hall brain teaser](https://en.wikipedia.org/wiki/Monty_Hall_problem):
    > Suppose you're on a game show, and you're given the choice of three doors:Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
    There is a really [fun discussion over at Marilyn vos Savant's site](http://marilynvossavant.com/game-show-problem/).
    
    Ok, now to setup the problem, along with some kind of visuals and what not.
    
    ## setting up a game
    
    There are many ways to do this, but to keep it simple and human comprehensible I'm going to do it one game at a time. 
    
    First up, a helper function which takes the door number guessed and the door opened up the host to reveal a goat, and returns the switched door:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    def switch_door(guess, goat_door_opened):
        """takes in the guessed door and the goat door opened
        and returns the switched door number"""
        doors = [0,1,2]
        doors.remove(goat_door_opened)
        doors.remove(guess)
        return doors[0]
    ```
    
    </div>
    
    </div>
    
    Now the actual monty hall function - it takes in a guess and whether you want to switch your guess, and returns True or False depending on whether you win
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    def monty_hall(guess=0, switch_guess=False, open_goat_door=True):
        """sets up 3 doors 0-2, one which has a pize, and 2 have goats.
        takes in the door number guessed by the player and whether he/she switched door
        after one goat door is revealed"""
        
        doors = [door for door in range(3)]
        np.random.shuffle(doors)
        prize_door = doors.pop()
        
        goat_door_opened = doors[0]
        
        if goat_door_opened == guess:
            goat_door_opened = doors[1]
            
        if switch_guess:
            return switch_door(guess, goat_door_opened) == prize_door
        else:
            return guess == prize_door
    ```
    
    </div>
    
    </div>
    
    Now to run through a bunch of monty hall games:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    no_switch = np.mean([monty_hall(random.randint(0,2), False) for _ in range(100000)])
    no_switch
    ```
    
    </div>
    <div class="output_area" markdown="1">
    
    
    
    
        0.33196
    
    
    
    </div>
    
    </div>
    
    Not switching doors wins a third of the time, which makes intuitive sense, since we are choosing one door out of three.
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    yes_switch = np.mean([monty_hall(random.randint(0,2), True) for _ in range(100000)])
    yes_switch
    ```
    
    </div>
    <div class="output_area" markdown="1">
    
    
    
    
        0.66534
    
    
    
    </div>
    
    </div>
    
    This is the suprising result, since switching our guess increases the win rate to two third! To put it more graphically:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    <details class="description">
        <summary>Code details ...</summary>
        
    ```python
    #collapse-hide
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_title("Switching", fontsize=16)
    ax.pie([yes_switch, no_switch], labels=["Switching win %", "Not switching win %"],
           autopct='%1.1f%%', explode=(0, 0.05));
    ```
    
    </details>
    
    </div>
    <div class="output_area" markdown="1">
    
    
    ![svg](convert2md_files/monty_hall_files/output_10_0.svg)
    
    
    </div>
    
    </div>
    
    So our chances of winning essentially double if we switch our guess once a goat door has been opened.
    
    This is a good [monty hall infographic](https://somethingaweek.wordpress.com/2010/08/19/22-lets-make-a-deal/).
    
    ## the no reveal month
    
    So what if Monty never opens a goat door, and just gives us a change to switch the guessed door? Does the winning % still change?
    
    So first we change the switch door function to remove the reveal option:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    def switch_door_no_revel(guess):
        """takes in the guessed door
        and returns the switched door number"""
        doors = [0,1,2]
        doors.remove(guess)
        np.random.shuffle(doors)
        return doors[0]
    ```
    
    </div>
    
    </div>
    
    Then I removed the revealing the goat door code from the original monty hall function above:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    def monty_hall_no_reveal(guess=0, switch_guess=False):
        """sets up 3 doors 0-2, one which has a pize, and 2 have goats.
        takes in the door number guessed by the player and whether he/she switched door
        """
        
        doors = [door for door in range(3)]
        np.random.shuffle(doors)
        prize_door = doors.pop()
            
        if switch_guess:
            return switch_door_no_revel(guess) == prize_door
        else:
            return guess == prize_door
    ```
    
    </div>
    
    </div>
    
    Now to run some sims:
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    no_switch_no_reveal = np.mean([monty_hall_no_reveal(random.randint(0,2), False) for _ in range(100000)])
    yes_switch_no_reveal = np.mean([monty_hall_no_reveal(random.randint(0,2), True) for _ in range(100000)])
    ```
    
    </div>
    
    </div>
    <div class="codecell" markdown="1">
    <div class="input_area" markdown="1">
    
    ```python
    plt.bar([0,1], [yes_switch_no_reveal, no_switch_no_reveal], 
    tick_label=["Switched Guess","Didn't Switch"], color=["blue","red"], alpha=0.7)
    print("Switching a door if a goat door hasn't been revealed")
    ```
    
    </div>
    <div class="output_area" markdown="1">
    
        Switching a door if a goat door hasn't been revealed
    
    
    
    ![svg](convert2md_files/monty_hall_files/output_18_1.svg)
    
    
    </div>
    
    </div>
    
    There is no impact of switching our guess if a goat door hasn't been revealed. Which makes sense to, since whatever door we choose, it has 1/3 probablity of winning. 
    


</div>

</div>
