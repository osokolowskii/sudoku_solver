from board import *
from solving_algorithm import *

board = Board()
solver = Solver(board.example_board)

print(solver.is_num_in_subgrid(4, 8, 3))