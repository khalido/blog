"""
Various helper utilities used by me. Put here to avoid retyping in too many notebooks.

to use: import khalido as ko
"""

from IPython.display import display, Markdown


def printmd(txt: str = ""):
    display(Markdown(txt))
