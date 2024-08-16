import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_no_empty_blocks(self):
        text = "abc\n\n\n\nefg"
        self.assertEqual(len(markdown_to_blocks(text)), 2)

    def test_whitespace_removed(self):
        text = "abc \n\n asd \n\n aaasds"
        blocks = markdown_to_blocks(text)
        self.assertEqual(len(blocks[0]), 3)
        self.assertEqual(len(blocks[1]), 3)

    def text_blocks(self):
        blocks = markdown_to_blocks(
            "# This is a heading \n\n\n" +
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" +
            "\n\n" +
            " * This is the first list item in a list block \n" +
            "* This is a list item\n" +
            "* This is another list item\n"
        )
        self.assertEqual(len(blocks), 3)

if __name__ == "__main__":
    unittest.main()