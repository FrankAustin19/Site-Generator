class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        parts = []
        for key, value in self.props.items():
            parts.append (f'{key}="{value}"')
        props_string = " ".join(parts)
        return props_string
        
    def __repr__(self):
        return f"HTMLNODE(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})"