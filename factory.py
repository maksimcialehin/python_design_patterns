from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def person_method():
        """Interface method"""


class Student(IPerson):

    def __init__(self):
        self.name = 'Student name'

    def person_method(self):
        print(f'I am a {self.name}')


class Teacher(IPerson):

    def __init__(self):
        self.name = 'Teacher name'

    def person_method(self):
        print(f'I am a {self.name}')


class PersonFactory:

    @staticmethod
    def build_person(person_type: str):
        match person_type:
            case 'student':
                return Student()
            case 'teacher':
                return Teacher()
            case _:
                print('Invalid type')


if __name__ == '__main__':
    choice = input('What type of person do you want to create?\n')
    person = PersonFactory.build_person(choice)
    person.person_method()
