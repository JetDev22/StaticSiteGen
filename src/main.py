from textnode import TextNode, TextType

test = TextNode("This is a sample text", TextType.LINK, "https://www.google.de")
print(test.__repr__())
