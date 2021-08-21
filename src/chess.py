from enum import Enum
from boardgame import Piece, Board


def createMatrizChessPiece(rows, columns):
    return [[ChessPiece()]*columns for _ in range(rows)]


class Color(Enum):
    WHITE = 1,
    BLACK = 2,


class ChessPiece(Piece):
    def __init__(self, board=None, color=None, piece=None):
        if piece:
            super().__init__(piece._board)
        else:
            super().__init__(board)
            self._color = color


class ChessMatch():
    def __init__(self):
        self._board = Board(8, 8)

    def getPieces(self):
        mat = createMatrizChessPiece(self._board._rows, self._board._columns)
        for i in range(self._board._rows):
            for j in range(self._board._columns):
                mat[i][j] = ChessPiece(piece=self._board._pieces[i][j])
        return mat
