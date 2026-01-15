import unittest

from htmlnode import HTMLNode, LeafNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        expected_html = 'class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_html)
        
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_no_children(self):
        node = HTMLNode(tag="span", props={"style": "color:red;"})
        expected_html = 'style="color:red;"'
        self.assertEqual(node.props_to_html(), expected_html)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click here", props={"href": "http://example.com"})
        self.assertEqual(node.to_html(), '<a href="http://example.com">Click here</a>')
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Just some text")
        self.assertEqual(node.to_html(), "Just some text")