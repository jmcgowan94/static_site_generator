from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    trimmed_blocks = [block.strip() for block in split_blocks]
    final_blocks = [block for block in trimmed_blocks if len(block) > 0]
    return final_blocks

def block_to_block_type(block):
    if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or
        block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
        return BlockType.HEADING
    elif block.startswith("```\n") and block.endswith("```"):
        return  BlockType.CODE
    elif block.startswith(">"):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        quote = True
        for line in lines:
            if not line.startswith(">"):
                quote = False
        if quote:
            return  BlockType.QUOTE
    elif block.startswith("-"):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        unordered_list = True
        for line in lines:
            if not line.startswith("-"):
                unordered_list = False
        if unordered_list:
            return  BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        lines = block.split("\n")
        lines = [line for line in lines if line != ""]
        ordered_list = True
        for n in range(len(lines)):
            i = n + 1
            if not lines[n].startswith(f"{i}. "):
                ordered_list = False
        if ordered_list:
            return  BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
