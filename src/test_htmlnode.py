import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "test text")
        print(node.__repr__())

        node2 = HTMLNode("p", "test text", None, {"href": "https://www.google.de", "target": "_blank"})
        print(node2.props_to_html())

if __name__ == "__main__":
    unittest.main()
