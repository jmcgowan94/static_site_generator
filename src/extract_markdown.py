import re

def extract_markdown_images(text):
    tuple_list = []
    alt_texts = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)

    for i in range(len(alt_texts)):
        tuple_to_add = (alt_texts[i], urls[i])
        tuple_list.append(tuple_to_add)

    return tuple_list

def extract_markdown_links(text):
    tuple_list = []
    anchors = re.findall(r"\[(.*?)\]", text)
    urls = re.findall(r"\((.*?)\)", text)

    for i in range(len(anchors)):
        tuple_to_add = (anchors[i], urls[i])
        tuple_list.append(tuple_to_add)

    return tuple_list