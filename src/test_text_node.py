import unittest
from textnode import (
    TextNode,
    text_node_to_html_node,
    TextType,)
from markdown_blocks import markdown_to_html_node
def test_link_conversion():
    text_node = TextNode("click me", TextType.LINK, "https://test.com")
    html_node = text_node_to_html_node(text_node)
    print(html_node.to_html())

def test_link_parsing():
    markdown_text = "Here is a [link](https://boot.dev)"
    nodes = markdown_to_html_node(markdown_text)  # or whatever your parsing function is called
    for node in nodes:
        print(f"Type: {node.text_type}, Text: {node.text}, URL: {node.url if hasattr(node, 'url') else 'None'}")