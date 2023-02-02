import copy


class Address:

    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


john = Person('John', Address('Abbey Road', 'London', 'UK'))
jane = copy.deepcopy(john)
print(john)
print(jane)
jane.name = 'Jane'
jane.address.street = 'Baker Street'
print(jane)
