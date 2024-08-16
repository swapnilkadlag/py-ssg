import textnode
from functools import reduce
from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return list(
        filter(
            lambda n: len(n.text.strip()) != 0,
            reduce(
                lambda a, b: a + b, 
                map(
                    lambda on: __split_node_delimiter__(on, delimiter, text_type),
                    old_nodes
                ),
                [],
            )
        )
    )

def __split_node_delimiter__(old_node, delimiter, text_type):
    if old_node.text_type != textnode.text_type_text:
        return [old_node]
    
    splits = old_node.text.split(delimiter, 2)

    if len(splits) == 1:
        return [old_node]

    if len(splits) != 3:
        raise Exception("Invalid text node")
    
    return [
        TextNode(splits[0], textnode.text_type_text),
        TextNode(splits[1], text_type),
    ] + __split_node_delimiter__(TextNode(splits[2], textnode.text_type_text), delimiter, text_type)
