from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props=None)
        self.tag = tag
        self.children = children
        
    def to_html(self):
        if len(self.tag) == 0 or self.tag == None:
            raise ValueError("Missing Tag!")
        if len(self.children) == 0 or self.children == None:
            raise ValueError("Missing Children!")
        html = f"<{self.tag}>"
        for leaf in self.children:
            html = html + leaf.to_html()
        return f"{html}</{self.tag}>"
