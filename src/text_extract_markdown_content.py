import unittest
import re
from extract_markdown_content import extract_markdown_images
from extract_markdown_content import extract_markdown_links

class TextExtractMarkdownContent(unittest.TestCase):
    def test_markdown_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        extracted_values = extract_markdown_images(text)
        self.assertEqual(extracted_values, [("rick roll", "https://i.imgur.com/aKaOqIh.gif")])

    def test_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        extracted_values = extract_markdown_links(text)
        self.assertEqual(extracted_values, [("to boot dev", "https://www.boot.dev")])

if __name__ == "__main__":
    unittest.main()