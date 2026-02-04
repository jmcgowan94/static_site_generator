import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()