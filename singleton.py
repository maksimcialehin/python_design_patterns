from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_data():
        """ Implement in child class """


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton('Default tag', 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance:
            raise Exception("Singleton can be created only once")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def get_data():
        print(f'Name: {PersonSingleton.__instance.tag}, '
              f'age: {PersonSingleton.__instance.age}')


p = PersonSingleton('Leo', 4)
print(p)
p.get_data()

p2 = PersonSingleton.get_instance()
print(p)
p2.get_data()

p3 = PersonSingleton('Mike', 3)

