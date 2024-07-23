from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)




class HTMLNode:                                                                   #HTMLNode
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children else []
        self.props = props if props else {}

    def to_html(self):
        raise NotImplementedError("Must be implemented by subclasses")
    
    def props_to_html(self):                            #converts list of props to key-value pairs in a dictionary
        parts = []
        for key, value in self.props.items():
            parts.append (f'{key}="{value}"')
        props_string = " ".join(parts)
        return props_string
        
    def __repr__(self):
        return f"HTMLNODE(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"
    

class LeafNode(HTMLNode):                           #subclass of HTMLNode. smallest pieces.
    def __init__(self, tag, value, props={}):
        if tag is None:
            tag = ""
        if props is None:
            props = {}
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        
        if not self.tag:
            return self.value
        
        props_string = self.props_to_html()               #converts leafnode to HTML string
        if props_string:
            return f"<{self.tag} {props_string}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
def text_node_to_html_node(text_node):              #function to pass our textnodes into htmlnodes
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text, None)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.src, "alt": text_node.alt})
    else:
        raise ValueError("Unsupported text node type")