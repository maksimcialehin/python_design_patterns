class Person:

    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as {self.position}'

    @staticmethod
    def new_person():
        return PersonBuilder()


class PersonBuilder:

    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):

    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):

    def work_as(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):

    def born(self, date):
        self.person.date_of_birth = date
        return self


pb = PersonBirthDateBuilder()
person = pb\
    .called('Leo')\
    .work_as('Turtle')\
    .born('1/1/1990')\
    .build()
print(person)

