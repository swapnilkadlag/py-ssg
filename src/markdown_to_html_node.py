from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type
from block_to_block_type import block_type_heading
from block_to_block_type import block_type_code
from block_to_block_type import block_type_quote
from block_to_block_type import block_type_ordered_list
from block_to_block_type import block_type_unordered_list
from block_to_block_type import block_type_paragraph
from block_to_block_type import block_to_block_type
from textnode import TextNode
from parentnode import ParentNode
from split_nodes_delimiter import split_nodes_delimiter
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown_content):
    nodes = []
    blocks = markdown_to_blocks(markdown_content)
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == block_type_heading:
            node = __block_to_heading_node__(block)
            nodes.append(node)

        if block_type == block_type_code:
            node = __block_to_code_node__(block)
            nodes.append(node)

        if block_type ==  block_type_quote:
            node = __block_to_quote_node__(block)
            nodes.append(node)

        if block_type == block_type_unordered_list:
            node = __block_to_unordered_list_node__(block)
            nodes.append(node)

        if block_type == block_type_ordered_list:
            node = __block_to_ordered_list_node__(block)
            nodes.append(node)

        if block_type == block_type_paragraph:
            node = __block_to_paragraph_node__(block)
            nodes.append(node)

    return ParentNode('html', nodes)

def __block_to_heading_node__(block):
    size = __get_heading_size__(block)
    content = __get_heading_content__(block, size)
    child_nodes = text_to_textnodes(content)
    node = ParentNode(f"h{size}", child_nodes)
    return node

def __block_to_code_node__(block):
    content = __get_code_content__(block)
    child_nodes = text_to_textnodes(content)
    node = ParentNode("code", child_nodes)
    return ParentNode('pre', [node])

def __block_to_quote_node__(block):
    content = __get_quote_content__(block)
    joined_content = '\n'.join(content).strip()
    child_nodes = text_to_textnodes(joined_content)
    node = ParentNode("blockquote", child_nodes)
    return node

def __block_to_unordered_list_node__(block):
    items = __get_unordered_list_content__(block)
    nodes = []
    for item in items:
        child_nodes = text_to_textnodes(item)
        node = ParentNode('li', child_nodes)
        nodes.append(node)
    parent_node = ParentNode('ul', nodes)
    return parent_node

def __block_to_ordered_list_node__(block):
    items = __get_ordered_list_content__(block)
    nodes = []
    for item in items:
        child_nodes = text_to_textnodes(item)
        node = ParentNode('li', child_nodes)
        nodes.append(node)
    parent_node = ParentNode('ol', nodes)
    return parent_node

def __block_to_paragraph_node__(block):
    nodes = text_to_textnodes(block)
    parent_node = ParentNode('p', nodes)
    return parent_node

def __get_heading_content__(content, size):
    return content[size+1:]

def __get_heading_size__(content):
    return content.split(' ', 1)[0].count('#')

def __get_code_content__(content):
    return content[3:][:-3]

def __get_quote_content__(content):
    splits = content.split('\n')
    quote_lines = []
    index = 1
    for s in splits:
        line = s[1:]
        quote_lines.append(line)
    return quote_lines

def __get_unordered_list_content__(content):
    splits = content.split('\n')
    quote_lines = []
    index = 1
    for s in splits:
        line = s[2:]
        quote_lines.append(line)
        index += 1
    return quote_lines

def __get_ordered_list_content__(content):
    splits = content.split('\n')
    quote_lines = []
    index = 1
    for s in splits:
        line = s.lstrip(f"{index}. ")
        quote_lines.append(line)
        index += 1
    return quote_lines