from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_type_heading

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("Title required")
