import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple_attributes(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_single_attribute(self):
        node = HTMLNode(props={"class": "btn-primary"})
        self.assertEqual(node.props_to_html(), 'class="btn-primary"')

    def test_props_to_html_empty_attributes(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), '')
        
if __name__ == "__main__":
    unittest.main()