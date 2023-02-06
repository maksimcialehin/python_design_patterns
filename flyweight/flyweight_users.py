import string
import random

from itertools import product


class User:
    def __init__(self, name):
        self.name = name


class UserFlyweight:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split()]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []

    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    # User uses 10 000 names in memory
    # for first, last in product(first_names, last_names):
    #     users.append(User(f'{first} {last}'))

    # UserFlyweight uses 200 names in memory, instead of this it uses indexes of names
    for first, last in product(first_names, last_names):
        users.append(UserFlyweight(f'{first} {last}'))

    print(users[0])
