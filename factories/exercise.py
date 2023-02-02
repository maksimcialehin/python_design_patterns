class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'I am {self.name} with {self.id} id'


class PersonFactory:
    person_count = 0

    def create_person(self, name):
        p = Person(self.person_count, name)
        self.person_count += 1
        return p


factory = PersonFactory()
print(factory.create_person('Alice'))
print(factory.create_person('Bob'))
print(factory.create_person('Clarissa'))
