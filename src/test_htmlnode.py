import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.tag, "p")

    def test_value(self):
        node = HTMLNode(value="this is a paragraph")
        self.assertEqual(node.value, "this is a paragraph")

    def test_props_to_html(self):
        node_props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode(tag="p", value="this is a paragraph", props=node_props)
        props_string = node.props_to_html()
        self.assertEqual(props_string, ' href="https://www.google.com" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()