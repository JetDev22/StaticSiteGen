import unittest

from converter import *
from textnode import TextNode, TextType 
from htmlnode import HTMLNode 
from splitdelimeter import *


class splitDelimiterTest(unittest.TestCase):
    def delimiterTest(self):
        old = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        result = split_nodes_delimiter(old, "`", TextType.CODE)
        print(result)


if __name__ == "__main__":
    unittest.main()
