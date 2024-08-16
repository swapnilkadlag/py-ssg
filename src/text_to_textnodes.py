from split_nodes_content import split_nodes_image
from split_nodes_content import split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
import textnode

def text_to_textnodes(text):
    node = TextNode(text, textnode.text_type_text)
    bold_nodes = split_nodes_delimiter([node], "**", textnode.text_type_bold)
    italic_nodes = split_nodes_delimiter(bold_nodes, "*", textnode.text_type_italic)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", textnode.text_type_code)
    link_nodes = split_nodes_link(code_nodes)
    image_nodes = split_nodes_image(link_nodes)
    return image_nodes