import unittest
import textnode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertSequenceEqual(
            nodes, 
            [
                TextNode("This is ", textnode.text_type_text),
                TextNode("text", textnode.text_type_bold),
                TextNode(" with an ", textnode.text_type_text),
                TextNode("italic", textnode.text_type_italic),
                TextNode(" word and a ", textnode.text_type_text),
                TextNode("code block", textnode.text_type_code),
                TextNode(" and an ", textnode.text_type_text),
                TextNode("obi wan image", textnode.text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", textnode.text_type_text),
                TextNode("link", textnode.text_type_link, "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()