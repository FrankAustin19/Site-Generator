import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):


    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode(tag="div", children=[], props=None)
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode(tag=None, children=[LeafNode(tag="p", value="text")], props=None)
            parent.to_html()
        self.assertEqual(str(context.exception), "Object has no tag")

if __name__ == "__main__":
    unittest.main()