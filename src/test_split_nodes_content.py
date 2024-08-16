import unittest
import textnode
from split_nodes_content import split_nodes_image
from split_nodes_content import split_nodes_link
from textnode import TextNode


class TestSplitNodesContent(unittest.TestCase):

    def test_image(self):
        text_node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            textnode.text_type_text,
        )
        new_nodes = split_nodes_image([text_node])
        self.assertEqual(len(new_nodes), 4)

    def test_links(self):
        text_node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            textnode.text_type_text,
        )
        new_nodes = split_nodes_link([text_node])
        self.assertEqual(len(new_nodes), 4)

if __name__ == "__main__":
    unittest.main()

