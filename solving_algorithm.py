from math import floor

class Solver:

    def __init__(self, board):
        self.board = board

    original_board = []

    def save_original_board(self):
        for row in self.board:
            self.original_board.append(row)

    def is_num_in_row(self, num, row):
        return num in self.board[row]
    
    def is_num_in_col(self, num, col):
        for rows in self.board:
            if rows[col] == num:
                return True
        return False

    def is_num_in_subgrid(self, num, row, col):
        for i in (0, 3, 6):
            if row >= i and row < i + 3:
                starting_row = i
            if col >= i and col < i + 3:
                starting_col = i
        print(starting_row, starting_col)
        for j in range(starting_row, starting_row + 2):
            for k in range(starting_col, starting_col + 2):
                if self.board[j][k] == num:
                    return True
        return False