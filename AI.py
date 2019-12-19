import math
from board import *
from Player import playPiece
import random as rand

pieces = None


class AI:
    pieces = None

    def __init__(self, piece):
        self.piece = piece
        AI.pieces = piece
        self.empty = 0

    def piece(self):
        return AI.pieces

    def evaluate_window(self, window):
        score = 0
        if self.piece != playPiece:
            oppPiece = self.piece
        if window.count(1) == 4:
            score += 100
        elif window.count(1) == 3 and window.count(self.empty) == 1:
            score += 5
        elif window.count(1) == 2 and window.count(self.empty) == 2:
            score += 2
        if window.count(2) == 3 and window.count(self.empty) == 1:
            score -= 4
        return score

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = board.get_valid_locations()
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.winning_move(self.piece):
                    return None, 100000000000000
                elif board.winning_move(playPiece):
                    return None, -100000000000000
                else:
                    return None, board.score_position(self.piece)
        if maximizingPlayer:
            value = -math.inf
            x = rand.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_open_row(col)
                b_copy = board.copy()
                b_copy.drop_piece(row, col, self.piece)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    x = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
                return x, value
        else:  # Minimizing player
            value = math.inf
            x = rand.choice(valid_locations)
            for col in valid_locations:
                row = board.get_next_open_row(col)
                b_copy = board.copy()
                b_copy.drop_piece(row, col, playPiece)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    x = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return x, value

    def is_terminal_node(self, board):
        return board.winning_move(playPiece) or board.winning_move(self.piece) or len(board.get_valid_locations()) == 0
