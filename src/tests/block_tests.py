import unittest
import textwrap
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_links,
    extract_markdown_images,
    text_to_textnodes,
    markdown_to_blocks,
    block_to_block_type
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class BlockTypeTests(unittest.TestCase):
    def test_block_to_block_code(self):
        text = "``` this is a code block ```"
        block_type = block_to_block_type(text)
        self.assertEqual("code", block_type)
    
    def test_block_to_block_test_heading(self):
        text = "### This is Heading 3"
        block_type = block_to_block_type(text)
        self.assertEqual("heading", block_type)
    
    def test_block_to_block_test_quote(self):
        text = textwrap.dedent(""" > be me
                > me bee
                > buzz buzz
                """)
        block_type = block_to_block_type(text)
        self.assertEqual("quote", block_type)

    def test_block_to_block_test_unordered_list_a(self):
        text = textwrap.dedent(""" * cat
                * dog
                * possum (male)
                * possom (female) 
                """)
        block_type = block_to_block_type(text)
        self.assertEqual("unordered_list", block_type)

    def test_block_to_block_test_unordered_list_b(self):
        text = textwrap.dedent("""- cat
                - dog
                - possum (male)
                - possom (female) 
                """)
        block_type = block_to_block_type(text)
        self.assertEqual("unordered_list", block_type)

    def test_block_to_block_test_ordered_list(self):
        text = textwrap.dedent(""" 1. Buy seeds
                2. ???
                3. Profit 
                """)
        block_type = block_to_block_type(text)
        self.assertEqual("ordered_list", block_type)

    def test_block_to_block_test_paragraph(self):
        text = "This is a paragraph"
        block_type = block_to_block_type(text)
        self.assertEqual("paragraph", block_type)

if __name__ == "__main__":
    unittest.main()