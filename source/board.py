from .constants import *
from .square import Square
from .utils import add_pieces

class Board:
    def __init__(self):
        # initialize the chess board with Square objects
        self.squares = [[Square(row, col) for col in range(8)] for row in range(8)]
        # replaces squares with pieces
        add_pieces(self, 'white')
        add_pieces(self, 'black')

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, col = index
            return self.squares[row][col]
        elif isinstance(index, int):
            return self.squares[index]
        else:
            raise TypeError("Invalid index type: {}".format(type(index)))

    def move(self, piece, row, col):
        self.squares[piece.row][piece.col], self.squares[row][col] = self.squares[row][col], self.squares[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        square = self.squares[row][col]
        if square is not None and square.has_piece():
            return square.piece
        else:
            return None

    # def get_valid_moves(self, piece):
    #     moves = {}








