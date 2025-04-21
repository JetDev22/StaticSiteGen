from textnode import TextNode, TextType 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            if node.text.find(delimiter) != -1:
                first = node.text.find(delimiter)
                last = node.text.find(delimiter, first+1)
                if last != -1:
                    # Cut the node until found delimeter and add to list
                    begin = (TextNode(node.text[0:first], TextType.TEXT))
                    if len(begin.text) != 0:
                        result.append(begin)
                    result.append(TextNode(node.text[first: last+1], text_type))
                    end = (TextNode(node.text[last+1:], TextType.TEXT))
                    if len(end.text) != 0:
                        result.append(end)
                else:
                    raise Exception(f"Closing delimeter for {text_type} not found")
            else:
                raise Exception("Delimeter is not valid markdown syntax")
    return result
