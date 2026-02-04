from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text_list = node.text.split(delimiter)
            for i in range(len(text_list)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text_list[i], TextType.TEXT))
                else:
                    if delimiter == "**":
                        new_nodes.append(TextNode(text_list[i], TextType.BOLD))
                    elif delimiter == "_":
                        new_nodes.append(TextNode(text_list[i], TextType.ITALIC))
                    elif delimiter == "`":
                        new_nodes.append(TextNode(text_list[i], TextType.CODE))
                    else:
                        raise Exception(f"Unknown delimiter: {delimiter}")
    return new_nodes
