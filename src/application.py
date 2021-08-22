from chess import ChessMatch, ChessPosition, Color


class UI():

    white = '\033[1;37m'
    yellow = '\033[1;33m'
    reset = '\033[0;0m'

    @staticmethod
    def readChessPosition():
        value = input()
        if len(value) != 2 :
            raise ValueError('Invalid value')
        return ChessPosition(value[:1], int(value[1:]))

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

    while True:
        UI.printBoard(chessMatch.getPieces())
        print()
        print('Source: ', end='')
        source = UI.readChessPosition()

        print()
        print('Target: ', end='')
        target = UI.readChessPosition()

        capturedPiece = chessMatch.performChessMove(source, target)
