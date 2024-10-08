import textnode

from textnode import TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case textnode.text_type_text:
            return LeafNode(None, text_node.text)
        case textnode.text_type_bold:
            return LeafNode('b', text_node.text)
        case textnode.text_type_italic:
            return LeafNode('i', text_node.text)
        case textnode.text_type_code:
            return LeafNode("code", text_node.text)
        case textnode.text_type_link:
            return LeafNode('a', text_node.text, {"href":text_node.url})
        case textnode.text_type_image:
            return LeafNode("img", "", {"src":text_node.url})
        case _:
            raise ValueError("Invalid text_type")