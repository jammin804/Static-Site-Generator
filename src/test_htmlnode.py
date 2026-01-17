import unittest

from htmlnode import HTMLNode, LeafNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

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
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        # print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child", props={"class": "text"})
        parent_node = ParentNode("div", [child_node], props={"id": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="container"><span class="text">child</span></div>',
        )
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")