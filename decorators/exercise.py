class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of the radius {self.radius}'


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        # note that a Square doesn't have resize()
        if hasattr(self.shape, 'resize'):
            self.shape.resize(factor)

    def __str__(self):
        return f'{self.shape} has color {self.color}'


if __name__ == '__main__':

    circle = ColoredShape(Circle(5), 'red')
    print(circle)
    circle.resize(2)
    print(circle)
    sq = ColoredShape(Square(3), 'white')
    sq.resize(2)
    print(sq)
