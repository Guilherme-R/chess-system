def createMatriz(rows, columns):
    return [[Piece()]*columns for _ in range(rows)]


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

    def Piece(self, row, column):
        return self._pieces[row][column]

    def PiecePosition(self, position):
        return self._pieces[position._rows][position._columns]

    def placePiece(self, piece, position):
        self._pieces[position._row][position._column] = piece
        piece._position = position


class Piece():
    def __init__(self, board=None):
        self._position = None
        self._board = board
