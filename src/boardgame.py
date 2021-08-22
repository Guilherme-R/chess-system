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
        if rows < 1 or columns < 1:
            raise ValueError()
        self._rows = rows
        self._columns = columns
        self._pieces = createMatriz(rows, columns)

    def Piece(self, row, column):
        if not self._positionExists(row, column):
            raise BoardException('Position not on the board!')
        return self._pieces[row][column]

    def PiecePosition(self, position):
        if not self.positionExists(position):
            raise BoardException('Position not on the board!')
        return self._pieces[position._row][position._column]

    def placePiece(self, piece, position):
        if self.thereIsAPiece(position):
            raise BoardException(f'There is already a piece on position {position}')
        self._pieces[position._row][position._column] = piece
        piece._position = position

    def _positionExists(self, row, column):
        return row >= 0 and row < self._rows and column >= 0 and column < self._columns

    def positionExists(self, position):
        return self._positionExists(position._row, position._column)

    def thereIsAPiece(self, position):
        if not self.positionExists(position):
            raise BoardException('Position not on the board!')
        return self.PiecePosition(position) is not None


class Piece():
    def __init__(self, board=None):
        self._position = None
        self._board = board


class BoardException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg
