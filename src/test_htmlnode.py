import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_empty(self):
        html_node = HTMLNode()
        self.assertEqual(html_node.props_to_html(),"")

    def test_props_given(self):
        html_node = HTMLNode(props={
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(html_node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()