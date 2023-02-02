class CodeBuilder:
    def __init__(self, root_name):
        self.class_name = root_name
        self.fields = []

    def add_field(self, type, name):
        self.fields.append((type, name))
        return self

    def __str__(self):
        if not self.fields:
            return f'class {self.class_name}:\n  pass'

        title = f'class {self.class_name}:\n  def __init__(self):\n' + ' ' * 4
        string_fields = '\n    '.join([f'self.{f[0]} = {f[1]}' for f in self.fields])
        return title + string_fields


cb = CodeBuilder('Foo')
print(cb)

cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)
