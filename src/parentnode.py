from htmlnode import HTMLNode

from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided")
        if self.children == None:
            raise ValueError("No children found")
        childs = f""
        for child in self.children:
            childs += child.to_html()
        return f"<{self.tag}>{childs}</{self.tag}>"


#grandchild_node = LeafNode("b", "grandchild")
#grandchild_node2 = LeafNode("i", "Grandchild2")
#child_node = ParentNode("href", [grandchild_node, grandchild_node2])
#child_node2 = ParentNode("span", [child_node])
#parent_node2 = ParentNode("p", [child_node2])
#parent_node = ParentNode("div", [parent_node2])
#print(parent_node.to_html())