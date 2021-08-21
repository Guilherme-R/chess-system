def createMatriz(rows, columns):
    return [[None]*columns for _ in range(rows)]


class Position():
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def __str__(self):
        return f'{self._row}, {self._column}'


class Board():
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._pieces = createMatriz(rows, columns)


class Piece():
    def __init__(self, board=None):
        self._position = None
        # self._color = color
        self._board = board


if __name__ == '__main__':
    print(Position(3,5))
