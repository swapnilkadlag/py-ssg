from textnode import TextNode
from functools import reduce
from extract_markdown_content import extract_markdown_images
from extract_markdown_content import extract_markdown_links
import textnode

def split_nodes_link(old_nodes):
    return list(
        filter(
            lambda n: len(n.text) != 0,
            reduce(
                lambda a, b: a + b, 
                map(
                    lambda on: __split_node_link__(on),
                    old_nodes
                ),
                [],
            )
        )
    )

def __split_node_link__(old_node):
    links = extract_markdown_links(old_node.text)
    if len(links) == 0:
         return [old_node]
    link = links[0]
    splits = old_node.text.split(f"[{link[0]}]({link[1]})", 1)
    return [
        TextNode(splits[0], textnode.text_type_text),
        TextNode(link[0], textnode.text_type_link, link[1]),
    ] + __split_node_link__(TextNode(splits[1], textnode.text_type_text))

def split_nodes_image(old_nodes):
    return list(
        filter(
            lambda n: len(n.text) != 0,
            reduce(
                lambda a, b: a + b, 
                map(
                    lambda on: __split_node_image__(on),
                    old_nodes
                ),
                [],
            )
        )
    )

def __split_node_image__(old_node):
    images = extract_markdown_images(old_node.text)
    if len(images) == 0:
         return [old_node]
    image = images[0]
    splits = old_node.text.split(f"![{image[0]}]({image[1]})", 1)
    return [
        TextNode(splits[0], textnode.text_type_text),
        TextNode(image[0], textnode.text_type_image, image[1]),
    ] + __split_node_image__(TextNode(splits[1], textnode.text_type_text))