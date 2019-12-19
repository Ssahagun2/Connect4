import random as rand

turn = rand.randint(0, 1)

playPiece = None


class players:
    def __init__(self, piece):
        self.piece = piece
        players.playPiece = piece

    def make_move(self, board):
        col = (int)(input("Make a move 0-6: "))
        row = board.get_next_open_row(col)
        board.drop_piece(self.piece, row, col)

    def get_piece(self):
        return self.piece
