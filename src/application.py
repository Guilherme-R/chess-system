from chess import ChessMatch, Color


class UI():

    white = '\033[1;37m'
    yellow = '\033[1;33m'

    reset = '\033[0;0m'

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
            if piece._color == Color.WHITE:
                print(UI.white + f'{piece}', end='')
            else:
                print(UI.yellow + f'{piece}', end='')
        print(' ', end=UI.reset)


if __name__ == '__main__':
    chessMatch = ChessMatch()
    UI.printBoard(chessMatch.getPieces())
