import random
from random import randint


class Generator:
    @staticmethod
    def generate(count):
        array = list(range(1, count + 1))
        random.shuffle(array)
        return array


class Splitter:
    @staticmethod
    def split(array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    @staticmethod
    def get_matrix(array, size):
        result = []
        start = 0
        for i in range(size):
            result.append(array[(start + (size * i)):(size * (i + 1))])
        return result

    def generate(self, size):
        while True:
            flat_array = Generator.generate(size * size)
            matrix = self.get_matrix(flat_array, size)
            split = Splitter.split(matrix)
            if Verifier.verify(split):
                break
        return matrix


if __name__ == '__main__':
    ms = MagicSquareGenerator()
    array = Generator.generate(9)
    print(ms.generate(3))
