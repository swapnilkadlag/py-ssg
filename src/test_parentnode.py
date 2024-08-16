import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_no_child_raises_error(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode('', None).to_html()

    
    def test_no_tag_raises_error(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None, [LeafNode(None, "Normal text")]).to_html()

    def test_parent(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {"alt":"sadadas"}),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(parent_node.to_html(), "<p><b alt=\"sadadas\">Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()