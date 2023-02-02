import copy


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:

    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        n_start = copy.deepcopy(self.start)
        n_end = copy.deepcopy(self.end)
        return Line(n_start, n_end)

    def __str__(self):
        return f'{self.start}, {self.end}'
