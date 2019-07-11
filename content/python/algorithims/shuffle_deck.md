
Using [Wikipedia's standard card deck definition](https://en.wikipedia.org/wiki/Standard_52-card_deck) I used two character string per card, with the first character being the rank of the card (2-10,JQKA) and the second being the suit.

So we end up with a list of 52 two character strings: 


```python
deck = [rank + suit for rank in '23456789TJQKA' for suit in 'SHDC']
print(deck)
```

    ['2S', '2H', '2D', '2C', '3S', '3H', '3D', '3C', '4S', '4H', '4D', '4C', '5S', '5H', '5D', '5C', '6S', '6H', '6D', '6C', '7S', '7H', '7D', '7C', '8S', '8H', '8D', '8C', '9S', '9H', '9D', '9C', 'TS', 'TH', 'TD', 'TC', 'JS', 'JH', 'JD', 'JC', 'QS', 'QH', 'QD', 'QC', 'KS', 'KH', 'KD', 'KC', 'AS', 'AH', 'AD', 'AC']


Now to shuffle and deal cards from the deck:


```python
import random

def deal(numhands=1, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """takes in numhands, and optionaly a deck, shuffles and returns a list of numhands hands"""
    assert numhands*n <= len(deck), "you're trying to deal more cards then are in the deck"    
    random.shuffle(deck)
    return [deck[i*n:n*(i+1)] for i in range(numhands)]

deal(3)
```




    [['AS', '8C', '8H', 'TD', '7C'],
     ['3D', 'JH', 'KC', '7S', 'TC'],
     ['AH', '5H', 'KD', '3C', 'QD']]



## more

- use [Unicode](https://en.wikipedia.org/wiki/Playing_cards_in_Unicode) to represent card hands directly.


```python

```
