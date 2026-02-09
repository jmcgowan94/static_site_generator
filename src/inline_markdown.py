import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_list = node.text.split(delimiter)
        for i in range(len(text_list)):
            if i % 2 == 0:
                new_nodes.append(TextNode(text_list[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(text_list[i], text_type))
            
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text_list = node.text.split("!")
            for text in text_list:
                if "[" not in text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    image = text[1:text.index("]")]
                    url = text[text.index("(")+1:text.index(")")]
                    remaining_text = text[text.index(")")+1:].replace("!", "")
                    new_nodes.append(TextNode(image, TextType.IMAGE, url))
                    if len(remaining_text) > 0:
                        new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text_list = node.text.split("[")
            for text in text_list:
                if "]" not in text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    image = text[:text.index("]")]
                    url = text[text.index("(")+1:text.index(")")]
                    remaining_text = text[text.index(")")+1:]
                    new_nodes.append(TextNode(image, TextType.LINK, url))
                    if len(remaining_text) > 0:
                        new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    parsed_bold = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
    parsed_italic = split_nodes_delimiter(parsed_bold, "_", TextType.ITALIC)
    parsed_code = split_nodes_delimiter(parsed_italic, "`", TextType.CODE)
    parsed_images = split_nodes_image(parsed_code)
    parsed_links = split_nodes_link(parsed_images)
    final_nodes = parsed_links
    return final_nodes


def extract_markdown_images(text):
    tuple_list = []
    alt_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)

    if len(alt_texts) != len(urls):
        raise Exception("Uneven number of alt texts and urls!")

    for i in range(len(alt_texts)):
        tuple_to_add = (alt_texts[i], urls[i])
        tuple_list.append(tuple_to_add)

    return tuple_list

def extract_markdown_links(text):
    tuple_list = []
    anchors = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)

    if len(anchors) != len(urls):
        raise Exception("Uneven number of anchors and urls!")

    for i in range(len(anchors)):
        tuple_to_add = (anchors[i], urls[i])
        tuple_list.append(tuple_to_add)

    return tuple_list
