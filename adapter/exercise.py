class Square:
    def __init__(self, side=0):
        self.side = side


# Calculating square of rectangle
def calculate_area(rc):
    return rc.width * rc.height


# class SquareToRectangleAdapter:
#     def __init__(self, square):
#         self.width = square.side
#         self.height = square.side


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


sq = Square(11)
print(calculate_area(SquareToRectangleAdapter(sq)))
