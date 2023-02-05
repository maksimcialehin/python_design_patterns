from abc import ABC


class Shape(ABC):
    def __str__(self):
        return ''


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape(Shape):
    # decorator
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('You cannot apply same decorator twice')
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


class TransparentShape(Shape):
    # another decorator
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has transparency {self.transparency * 100}%'


if __name__ == '__main__':
    circle = Circle(4)
    print(circle)

    red_circle = ColoredShape(circle, 'red')
    # red_circle.resize(2)
    print(red_circle)

    red_half_circle = TransparentShape(red_circle, 0.5)
    print(red_half_circle)

    mixed = ColoredShape(ColoredShape(Square(3), 'red'), 'white')
    print(mixed)
