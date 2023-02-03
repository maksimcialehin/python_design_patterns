from abc import ABC


class Shape:
    def __init__(self, renderer):
        self.name = None
        self.renderer = renderer


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as()}'


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as()}'


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    def what_to_render_as(self):
        return 'pixels'


# reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
print(str(Triangle(RasterRenderer())))
