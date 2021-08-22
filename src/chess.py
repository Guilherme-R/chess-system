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

    def initialSetup(self):
        self._board.placePiece(Rook(self._board, Color.WHITE), Position(2, 1))
        self._board.placePiece(King(self._board, Color.WHITE), Position(7, 4))
        self._board.placePiece(King(self._board, Color.BLACK), Position(0, 4))


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
