class HtmlElement:
    indent_size = 2

    def __init__(self, tag='', text=''):
        self.tag = tag
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.tag}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}<{self.text}>')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.tag}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_tag):
        self.root_tag = root_tag
        self.__root = HtmlElement(tag=root_tag)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


# builder = HtmlBuilder('ul')
# builder.add_child('li', '1')
# builder.add_child('li', '2')
builder = HtmlElement.create('li')
builder.add_child_fluent('li', '11111').\
    add_child_fluent('li', '22222')
print(builder)
