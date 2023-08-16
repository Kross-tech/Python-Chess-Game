from .constants import *
from .square import Square
from .piece import *


def add_pieces(board, color):
    row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
    # loops through each column and places a pawn in rows 6 and 7 based on color
    for col in range(COLS):
        board.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color, row_pawn, col))
    # uses Square class to place Knights in row 7 or 0, column 1 or 6 depending on color
    # knights
    board.squares[row_other][1] = Square(row_other, 1, Knight(color, row_other, 1))
    board.squares[row_other][6] = Square(row_other, 6, Knight(color, row_other, 6))

    # bishops
    board.squares[row_other][2] = Square(row_other, 2, Bishop(color, row_other, 2))
    board.squares[row_other][5] = Square(row_other, 5, Bishop(color, row_other, 5))

    # rooks
    board.squares[row_other][0] = Square(row_other, 0, Rook(color, row_other, 0))
    board.squares[row_other][7] = Square(row_other, 7, Rook(color, row_other, 7))

    # queen
    board.squares[row_other][3] = Square(row_other, 3, Queen(color, row_other, 3))

    # king
    board.squares[row_other][4] = Square(row_other, 4, King(color, row_other, 4))
