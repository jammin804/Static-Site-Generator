from textnode import TextType


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html method")
    
    def props_to_html(self):
        return ' '.join(f'{key}="{value}"' for key, value in (self.props or {}).items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        props_str = self.props_to_html()
        if self.value is None:
            raise ValueError("LeafNode must have a value to convert to HTML")
        if self.tag is None:
            return self.value
        if self.props is None or not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        props_str = self.props_to_html()
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children_html = "".join(child.to_html() for child in self.children)
        if props_str is not None and props_str != "":
            return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
    
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")