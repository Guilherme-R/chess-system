from chess import ChessMatch


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
        if piece == None:
            print('-', end='')
        else:
            print(piece, end='')
        print(' ', end='')


if __name__ == '__main__':
    chessMatch = ChessMatch()
    UI.printBoard(chessMatch.getPieces())
