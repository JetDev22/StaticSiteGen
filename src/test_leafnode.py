import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("b", "Some Text", {"color": "green"})
        print(node2.to_html())
        print(node2.props)
        


if __name__ == "__main__":
    unittest.main()
