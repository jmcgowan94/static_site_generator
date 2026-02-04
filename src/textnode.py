from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    tag = None
    value = text_node.text
    props = None
    if text_node.text_type.value == "text":
        pass
    elif text_node.text_type.value == "bold":
        tag = "b"
    elif text_node.text_type.value == "italic":
        tag = "i"
    elif text_node.text_type.value == "code":
        tag = "code"
    elif text_node.text_type.value == "link":
        tag = "a"
        props = {"href": text_node.url}
    elif text_node.text_type.value == "image":
        tag = "img"
        value = ""
        props = {"src": text_node.url, "alt": text_node.text}
    else:
        raise Exception(f"Unrecognized text type: {text_node.text_type.value}")
    return LeafNode(tag, value, props)
