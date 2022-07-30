from board import *
from solving_algorithm import *

board = Board()
solver = Solver(board.example_board)

board.print_board()
solver.solve()
print('..')
board.print_board(solver.board)