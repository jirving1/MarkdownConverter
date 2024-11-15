from htmlnode import (
    ParentNode,
    LeafNode,)

node = ParentNode("p", [LeafNode("b", "hello")])
print(node.to_html())

node2 = ParentNode("p",[LeafNode("b", "hello"), LeafNode("b", "world")])
print(node2.to_html())

# Test with properties
node3 = ParentNode("div", [LeafNode("span", "text")], {"class": "highlight"})
print(node3.to_html())

# Test with nested parent nodes
node4 = ParentNode("div", [
    ParentNode("p", [LeafNode("b", "nested")])
    ])
print(node4.to_html())