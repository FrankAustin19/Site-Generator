import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)
from textnode import split_nodes_delimiter  # make sure this path is correct

class TestTextNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        for n in new_nodes:
            print(n.text, n.text_type)

if __name__ == '__main__':
    unittest.main()