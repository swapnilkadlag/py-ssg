import unittest
import textnode_to_htmlnode
import textnode

from leafnode import LeafNode
from textnode import TextNode

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        text_node = TextNode("Text Node", textnode.text_type_text)
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "Text Node"
        )
        
    def test_bold(self):
        text_node = TextNode("Text Node", textnode.text_type_bold)
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "<b>Text Node</b>"
        )

    def test_italic(self):
        text_node = TextNode("Text Node", textnode.text_type_italic)
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "<i>Text Node</i>"
        )
        
    def test_code(self):
        text_node = TextNode("Text Node", textnode.text_type_code)
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "<code>Text Node</code>"
        )
        
    def test_link(self):
        text_node = TextNode("Text Node", textnode.text_type_link, "url")
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "<a href=\"url\">Text Node</a>"
        )
        
    def test_image(self):
        text_node = TextNode("Text Node", textnode.text_type_image, "url")
        self.assertEqual(
            textnode_to_htmlnode.text_node_to_html_node(text_node).to_html(),
            "<img src=\"url\"></img>"
        )

if __name__ == "__main__":
    unittest.main()