def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    trimmed_blocks = [block.strip() for block in split_blocks]
    final_blocks = [block for block in trimmed_blocks if len(block) > 0]
    return final_blocks