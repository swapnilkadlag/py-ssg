import unittest
import textnode
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_not_text_node(self):
        not_textnode = TextNode("hi", textnode.text_type_bold)
        new_nodes = split_nodes_delimiter([not_textnode], "**", textnode.text_type_bold)
        self.assertEqual(not_textnode, new_nodes[0])

    def test_missing_delimiter(self):
        not_textnode = TextNode("hey, **hi", textnode.text_type_text)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([not_textnode], "**", textnode.text_type_bold)

    def test_bold_delimiter(self):
        not_textnode = TextNode("hey, **hi** are **you?**", textnode.text_type_text)
        new_nodes = split_nodes_delimiter([not_textnode], "**", textnode.text_type_bold)
        self.assertEqual(new_nodes[1].text_type, textnode.text_type_bold)

if __name__ == "__main__":
    unittest.main()