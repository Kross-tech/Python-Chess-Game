import os
from .constants import *


class Piece:
    def __init__(self, name, color, row=None, col=None, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.row = row
        self.col = col
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.selected = False

    def set_texture(self, size=80):
        if self.texture is None:
            self.texture = os.path.join(f'images/{self.color}_{self.name}.png')

    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()
        print('it worked')

    def __repr__(self):
        return str(self.color)

class Pawn(Piece):
    def __init__(self, color, row, col):
        self.direction = -1 if color == 'white' else 1
        super().__init__('pawn', color, row, col)

class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__('rook', color, row, col)

class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__('knight', color, row, col)

class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__('bishop', color, row, col)

class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__('queen', color, row, col)

class King(Piece):
    def __init__(self, color, row, col):
        super().__init__('king', color, row, col)
