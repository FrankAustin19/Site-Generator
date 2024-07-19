text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

import re

class TextNode:
    def __init__(self, text, text_type, url=None ):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
        return False
            
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type == text_type_text:
            parts = node.text.split(delimiter)
            
            if len(parts) % 2 == 0:
                raise ValueError("Unmatched delimiter found in text: " + node.text)
                
            for i, part in enumerate(parts):
                if i % 2 == 0:  
                    new_node = TextNode(part, text_type_text)
                else:  
                    new_node = TextNode(part, text_type)
                new_nodes.append(new_node)
        else:
            
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    pattern = r'!\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_link(old_nodes):
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    new_nodes = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = link_pattern.split(node.text)

            while parts:
                text = parts.pop(0)
                if text:
                    new_nodes.append(TextNode(text, text_type_text))
                
                if parts:
                    display_text = parts.pop(0)
                    url = parts.pop(0)
                    new_nodes.append(TextNode(display_text, text_type_link, url))
        else:
            new_nodes.append(node)
    return new_nodes

import re

def split_nodes_image(old_nodes):
    
    image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = image_pattern.split(node.text)
            
            while parts:
                text = parts.pop(0)
                if text:
                    new_nodes.append(TextNode(text, text_type_text))
                if parts:
                    alt_text = parts.pop(0)
                    url = parts.pop(0)
                    new_nodes.append(TextNode(alt_text, text_type_image, url))
        else:
            new_nodes.append(node)
    
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

        
         
         

def main():
    node = TextNode("this is a text node", "bold", "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()