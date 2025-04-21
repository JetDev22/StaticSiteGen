from htmlnode import HTMLNode 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.children = [] #no children allowed!
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("Missing Inner Text, please provide")
        if self.tag == None:
            return self.value
        if self.props != None:
            attr = ""
            for key, value in self.props.items():
                attr = attr + ' ' + key + '=' + '"' + value + '"'
            return f"<{self.tag}{attr}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
