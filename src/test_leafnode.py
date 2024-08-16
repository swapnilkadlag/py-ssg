import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_value_error(self):
        leaf_node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            leaf_node.to_html()

    def test_no_tag_returns_value(self):
        leaf_node = LeafNode(None, "No tag, raw value")
        self.assertEqual(leaf_node.to_html(), "No tag, raw value")

    def test_no_props_returns_tag(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.", )
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")
        
    def test_props_returns_tag(self):
        leaf_node = LeafNode( "a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

if __name__ == "__main__":
    unittest.main()