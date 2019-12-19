from copy import copy

import numpy as np
from AI import *


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((self.rows, self.cols))
        self.window_len = 4

    def __getitem__(self, item):
        return item

    def print_board(self):
        print(np.flip(self.board, 0))

    def get_next_open_row(self, col):
        for rows in range(self.rows):
            if self.board[rows][col] == 0:
                return rows

    def drop_piece(self, piece, row, col):
        self.board[row][col] = piece

    def winning_move(self, piece):
        return self.vertical_win(piece) or self.horizontal_win(piece) or self.dia_up_win(piece) or self.dia_down_win(
            piece)

    def vertical_win(self, piece):
        for cols in range(self.cols):
            for rows in range(self.rows - 3):
                if self.board[rows][cols] == piece and \
                        self.board[rows][cols + 1] == piece and \
                        self.board[rows][cols + 2] == piece and \
                        self.board[rows][cols + 3] == piece:
                    return True
            return False

    def horizontal_win(self, piece):
        for cols in range(self.cols - 3):
            for rows in range(self.rows):
                if self.board[rows][cols] == piece and \
                        self.board[rows + 1][cols] == piece and \
                        self.board[rows + 2][cols] == piece and \
                        self.board[rows + 3][cols] == piece:
                    return True
            return False

    def dia_up_win(self, piece):
        for cols in range(self.cols - 3):
            for rows in range(self.rows - 3):
                if self.board[rows][cols] == piece and \
                        self.board[rows + 1][cols + 1] == piece and \
                        self.board[rows + 2][cols + 2] == piece and \
                        self.board[rows + 3][cols + 3] == piece:
                    return True
            return False

    def dia_down_win(self, piece):
        for cols in range(self.cols - 3):
            for rows in range(3, self.rows):
                if self.board[rows][cols] == piece and \
                        self.board[rows - 1][cols + 1] == piece and \
                        self.board[rows - 2][cols + 2] == piece and \
                        self.board[rows - 3][cols + 3] == piece:
                    return True
            return False

    def is_valid_location(self, col):
        return self.board[self.rows - 1][col] == 0

    def score_position(self, piece):
        score = 0

        center = [int(i) for i in list(self.board[:, self.cols // 2])]
        center_count = center.count(piece)
        score += center_count * 3

        for r in range(self.rows):
            row_array = [int(i) for i in list(self.board[r, :])]
            for c in range(self.cols - 3):
                window = row_array[c:c + self.window_len]
                score += AI.evaluate_window(piece, window)

            ## Score Vertical
        for c in range(self.cols):
            col_array = [int(i) for i in list(self.board[:, c])]
            for r in range(self.rows - 3):
                window = col_array[r:r + self.window_len]
                score += AI.evaluate_window(piece, window)

            ## Score posiive sloped diagonal
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                window = [self.board[r + i][c + i] for i in range(self.window_len)]
                score += AI.evaluate_window(piece, window)

        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                window = [self.board[r + 3 - i][c + i] for i in range(self.window_len)]
                score += AI.evaluate_window(piece, window)

        return score

    def copy(self):
        self.board = copy(self.board)
        return self.board

    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.cols):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def is_valid_locations(self, col):
        return self.board[self.rows - 1][col] == 0
