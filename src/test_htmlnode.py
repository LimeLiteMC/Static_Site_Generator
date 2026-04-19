import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props2html_is_not_eq(self):
        node = HTMLNode("p", "Hello there", None, {"href" : "https://www.nitrome.com"})
        node2 = HTMLNode("h1", "How to Speak", [node], {"href" : "https://docs.python.org/3/library"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_props2html_is_equal(self):
        node = HTMLNode("h1", "How to Speak", None, {"href" : "https://docs.python.org/3/library"})
        node2 = HTMLNode("h1", "How to Speak", None, {"href" : "https://docs.python.org/3/library"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
        
    def test_repr_returns_string(self):
        node = HTMLNode("p", "Hello there", None, {"href" : "https://www.nitrome.com"})
        self.assertIsInstance(repr(node), str)

if __name__ == "__main__":
    unittest.main()