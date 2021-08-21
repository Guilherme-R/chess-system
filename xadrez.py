def createMatriz(rows, columns):
    return [[None]*columns for _ in range(rows)]


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
    print(Board(8, 8)._pieces)
