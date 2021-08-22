from enum import Enum
from boardgame import Piece, Board, Position


def createMatrizChessPiece(rows, columns):
    return [[ChessPiece()]*columns for _ in range(rows)]


class Color(Enum):
    WHITE = 1,
    BLACK = 2,


class ChessMatch():
    def __init__(self):
        self._board = Board(8, 8)
        self.initialSetup()

    def getPieces(self):
        mat = createMatrizChessPiece(self._board._rows, self._board._columns)
        for i in range(self._board._rows):
            for j in range(self._board._columns):
                mat[i][j] = self._board._pieces[i][j]
        return mat

    def placeNewPiece(self, column, row, piece):
        self._board.placePiece(piece, ChessPosition(column, row).toPosition())

    def initialSetup(self):
        self.placeNewPiece('c', 1, Rook(self._board, Color.WHITE))
        self.placeNewPiece('c', 2, Rook(self._board, Color.WHITE))
        self.placeNewPiece('d', 2, Rook(self._board, Color.WHITE))
        self.placeNewPiece('e', 2, Rook(self._board, Color.WHITE))
        self.placeNewPiece('e', 1, Rook(self._board, Color.WHITE))
        self.placeNewPiece('d', 1, King(self._board, Color.WHITE))

        self.placeNewPiece('c', 7, Rook(self._board, Color.BLACK))
        self.placeNewPiece('c', 8, Rook(self._board, Color.BLACK))
        self.placeNewPiece('d', 7, Rook(self._board, Color.BLACK))
        self.placeNewPiece('e', 7, Rook(self._board, Color.BLACK))
        self.placeNewPiece('e', 8, Rook(self._board, Color.BLACK))
        self.placeNewPiece('d', 8, King(self._board, Color.BLACK))


class ChessPosition():
    def __init__(self, column, row):
        if column < 'a' or column > 'h' or row < 1 or row > 8:
            raise ChessException('Error instantiating ChessPosition. Valid values are from a1 to h8')
        self._row = row
        self._column = column

    def toPosition(self):
        return Position(8 - self._row, ord(self._column) - ord('a'))

    def fromPosition(self):
        return ChessPosition(ord('a') - ord(self._column), 8 - self._row)

    def __str__(self):
        return f'{self._column}{self._row}'


class ChessPiece(Piece):
    def __init__(self, board=None, color=None):
        super().__init__(board)
        self._color = color


class Rook(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)

    def __str__(self):
        return 'R'


class King(ChessPiece):
    def __init__(self, board, color):
        super().__init__(board, color)

    def __str__(self):
        return 'K'


class ChessException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg
