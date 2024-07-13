import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_paragraph_node(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")

    def test_anchor_node(self):
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_raw_text_node(self):
        leaf3 = LeafNode(None, "Just some raw text.")
        self.assertEqual(leaf3.to_html(), "Just some raw text.")
        
    

if __name__ == '__main__':
    unittest.main()