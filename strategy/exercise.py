from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b ** 2 - 4 * a * c
        return d


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d < 0:
            return float('nan')
        return d


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        d = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


q = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(q.solve(5, 3, -26))
print(q.solve(5, 1, 5))
