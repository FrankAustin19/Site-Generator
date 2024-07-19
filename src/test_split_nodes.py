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
from textnode import split_nodes_link


class SplitNodesLinkTest(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        expected_result = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode("to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"),
        ]
        
        result = split_nodes_link([node])
        self.assertEqual(result, expected_result)

    def test_split_nodes_link_first(self):
        node = TextNode("[Welcome to Google](https://www.google.com), please don't [check out our competition](https://www.yahoo.com).", text_type_text)

        expected_result = [
            TextNode("Welcome to Google", text_type_link, "https://www.google.com"),
            TextNode(", please don't ", text_type_text),
            TextNode("check out our competition", text_type_link, "https://www.yahoo.com"),
            TextNode(".", text_type_text)
        ]                        
        result = split_nodes_link([node])
        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()