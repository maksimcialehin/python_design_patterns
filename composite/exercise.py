from collections.abc import Iterable
from abc import ABC


class Sum(Iterable, ABC):
    def sum(self):
        result = 0
        for s in self:
            for obj in s:
                result += obj
        return result


class SingleValue(Sum):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Sum):
    pass


single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)

all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)
print(all_values.sum())
