class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        html_string = ""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props=props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Props: {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if len(self.children) == 0:
            raise ValueError("ParentNode must have at least one child node")
        children_html_str = ""
        for child in self.children:
            children_html_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html_str}</{self.tag}>"
