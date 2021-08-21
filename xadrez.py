from enum import Enum


def createMatriz(rows, columns):
    return [[Piece()]*columns for _ in range(rows)]


def createMatrizChessPiece(rows, columns):
    return [[ChessPiece()]*columns for _ in range(rows)]


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


class Piece():
    def __init__(self, board=None):
        self._position = None
        self._board = board


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


class UI():

    @staticmethod
    def printBoard(pieces):
        for i in range(len(pieces)):
            print(f'{8 - i} ', end='')
            for j in range(len(pieces)):
                UI.printPiece(pieces[i][j])
            print()
        print('  a b c d e f g h')

    @staticmethod
    def printPiece(piece):
        if piece._board == None:
            print('-', end='')
        else:
            print(piece, end='')
        print(' ', end='')


if __name__ == '__main__':
    chessMatch = ChessMatch()
    UI.printBoard(chessMatch.getPieces())
