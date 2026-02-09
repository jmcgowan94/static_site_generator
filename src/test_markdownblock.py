import unittest

from markdownblock import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, "heading")

    def test_block_to_block_type_code(self):
        block = """```
This is a code block
```"""

        result = block_to_block_type(block)
        self.assertEqual(result, "code")
        print(block[:5])

    def test_block_to_block_type_quote(self):
        block = """> This is a quote
>And another
"""
        result = block_to_block_type(block)
        self.assertEqual(result, "quote")

    def test_block_to_block_type_unordered_list(self):
        block = """- This is an unordered list
- And another item
"""
        result = block_to_block_type(block)
        self.assertEqual(result, "unordered_list")

    def test_block_to_block_type_ordered_list(self):
        block = """1. This is an ordered list
2. With a second item
3. And a third
"""
        result = block_to_block_type(block)
        self.assertEqual(result, "ordered_list")

    def test_block_to_block_type_paragraph(self):
        block = "this is a paragraph"
        result = block_to_block_type(block)
        self.assertEqual(result, "paragraph")

