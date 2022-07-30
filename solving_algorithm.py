from collections import Counter

class Solver:

    def __init__(self, board):
        self.board = []
        for i in range(9):
            self.board.append([])
            for j in range(9):
                self.board[i].append(board[i][j])

    def num_in_row(self, num, row):
        return num in self.board[row]
    
    def num_in_col(self, num, col):
        for rows in self.board:
            if rows[col] == num:
                return True
        return False

    def num_in_subgrid(self, num, row, col):
        starting_row = row // 3
        starting_col = col // 3

        for i in range(starting_row * 3, starting_row*3 + 3):
            for j in range(starting_col * 3, starting_col*3 + 3):
                if self.board[i][j] == num:
                    return True
        return False

    def valid(self, num, row, col):
        return not self.num_in_row(num, row) and not self.num_in_col(num, col) and not self.num_in_subgrid(num, row, col)


    def solve(self):
        empties = []
        valid = False
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    empties.append((i, j))
        while count < len(empties):
            for i in range(self.board[empties[count][0]][empties[count][1]], 10, 1):
                if self.valid(i, empties[count][0], empties[count][1]):
                    self.board[empties[count][0]][empties[count][1]] = i
                    valid = True
                    break
            if valid:
                count += 1
                valid = False
            else:
                self.board[empties[count][0]][empties[count][1]] = 0
                count = count - 1