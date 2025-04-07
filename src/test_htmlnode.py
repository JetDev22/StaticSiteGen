import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "same text", None, {"href": "https://www.google.de"})
        node2 = HTMLNode("p", "same text", None, {"href": "https://www.google.de"})

        node3 = HTMLNode("p", "test text", None, {"href": "http://www.google.de"})
        node4 = HTMLNode("h1", "test text", None, {"href": "https://www.gogle.de"})

        self.assertEqual(node.props_to_html(), node2.props_to_html())
        self.assertNotEqual(node3.props_to_html(), node4.props_to_html())

if __name__ == "__main__":
    unittest.main()
