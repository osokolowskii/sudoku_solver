class Board:

    example_board = [
        [0, 0, 0, 9, 0, 5, 0, 6, 0],
        [1, 6, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 1, 3],
        [0, 2, 0, 5, 0, 0, 8, 0, 0],
        [7, 3, 9, 0, 8, 0, 0, 4, 5],
        [0, 0, 8, 0, 0, 0, 2, 0, 9],
        [3, 0, 0, 0, 7, 0, 0, 2, 0],
        [0, 8, 2, 4, 5, 0, 3, 0, 7],
        [9, 5, 0, 0, 0, 0, 0, 8, 0]
    ]

    def print_board(self, board = example_board):
        for i in range(9):
            if i in (3, 6):
                print("- - - - - - - - - - - - -")
            row = []
            for j in range(9):
                if j in (3, 6):
                    row.append(" | ")
                row.append(str(board[i][j]))
            toprint = (" ".join(row))
            print(toprint)