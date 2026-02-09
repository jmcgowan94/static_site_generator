from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or
        block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
        return "heading"
    elif block.startswith("```\n") and block.endswith("```"):
        return "code"
    elif block.startswith(">"):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        quote = True
        for line in lines:
            if not line.startswith(">"):
                quote = False
        if quote:
            return "quote"
    elif block.startswith("-"):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        unordered_list = True
        for line in lines:
            if not line.startswith("-"):
                unordered_list = False
        if unordered_list:
            return "unordered_list"
    elif block.startswith("1. "):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        ordered_list = True
        for n in range(len(lines)):
            i = n + 1
            if not lines[n].startswith(f"{i}. "):
                ordered_list = False
        if ordered_list:
            return "ordered_list"
    else:
        return "paragraph"
