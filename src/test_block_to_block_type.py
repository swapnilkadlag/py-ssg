import unittest
from block_to_block_type import block_type_heading
from block_to_block_type import block_type_code
from block_to_block_type import block_type_quote
from block_to_block_type import block_type_ordered_list
from block_to_block_type import block_type_unordered_list
from block_to_block_type import block_type_paragraph
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        text = "# heading"
        self.assertEqual(block_to_block_type(text), block_type_heading)
        text = "## heading"
        self.assertEqual(block_to_block_type(text), block_type_heading)
        text = "# # heading"
        self.assertEqual(block_to_block_type(text), block_type_heading)

    def test_code(self):
        text = "```code```"
        self.assertEqual(block_to_block_type(text), block_type_code)
        text = "````code ```"
        self.assertEqual(block_to_block_type(text), block_type_code)

    def test_quote(self):
        text = "> q1\n> q2\n> q2"
        self.assertEqual(block_to_block_type(text), block_type_quote)
        text = "> q1\n q2\n> q2"
        self.assertEqual(block_to_block_type(text), block_type_paragraph)

    def test_unordered_list(self):
        text = "* q1\n- q2\n* q2"
        self.assertEqual(block_to_block_type(text), block_type_unordered_list)
        text = "* q1\n1 q2\n* q2"
        self.assertEqual(block_to_block_type(text), block_type_paragraph)

    def test_ordered_list(self):
        text = "1. q1\n2. q2\n3. q2"
        self.assertEqual(block_to_block_type(text), block_type_ordered_list)
        text = "1. q1\n3. q2\n3. q2"
        self.assertEqual(block_to_block_type(text), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()