"""
converts jupyter notebooks to markdown using nbconvert  

though for now the cli tool is good enough.
Still, this allows more customization.
"""

from traitlets.config import Config
import nbconvert

# Setup config
c = Config()

c.MarkdownExporter.preprocessors = [
    "nbconvert.preprocessors.RegexRemovePreprocessor",
    "nbconvert.preprocessors.TagRemovePreprocessor",
]

exporter = nbconvert.MarkdownExporter(config=c)