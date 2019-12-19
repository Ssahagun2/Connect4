from board import *
from Player import *
from AI import AI
from Player import players


class logic:
    def __init__(self):
        self.turn = rand.randint(0, 1)
        self.b1 = None
        self.p1 = None
        self.a1 = None

    def play(self):
        self.b1 = Board(6, 7)
        self.p1 = players(1)
        self.a1 = AI(2)

        Board.print_board(self.b1)
        game_over = False
        while not game_over:
            if self.turn == 0:
                game_over = self.p1.make_move(self.b1)
                self.b1.print_board()
                if self.b1.winning_move(self.p1.piece):
                    print("Player 1 wins")
                    game_over = True
            else:
                col, minimax_score = AI.minimax(self.a1, self.b1, 5, -math.inf, math.inf, True)
                if self.b1.is_valid_location(col):
                    row = self.b1.get_next_open_row(col)
                    self.b1.drop_piece(row, col, self.a1.piece)
                    if self.b1.winning_move(self.a1.piece):
                        print("player 2 wins")
                        game_over = True
                self.b1.print_board()
            self.update_turn()

    def update_turn(self):
        if self.turn == 1:
            self.turn += 1
            self.turn %= 2
        else:
            self.turn += 1

