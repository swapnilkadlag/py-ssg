import functools

from textnode_to_htmlnode import text_node_to_html_node
from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError()
        if self.children == None or len(self.children) == 0:
            raise ValueError("Must have atleast 1 child node")


        def child_to_html(child):
            if isinstance(child, HTMLNode):
                return child.to_html()
            return text_node_to_html_node(child).to_html()

        child_nodes = functools.reduce(
            lambda a,b: a + b,
            map(
                child_to_html, 
                self.children
            )
        )
        if self.props == None:
            return f"<{self.tag}>{child_nodes}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{child_nodes}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({super().__repr__()})"
