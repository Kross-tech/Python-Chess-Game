import pygame
from source.board import Board


class Game:
    def __init__(self, win, display, board):
        self.win = win
        self.display = display
        self.selected = None
        self.board = board

    def select(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece is not None:
            self.selected = piece
            return True
        return False

    def _move(self, row, col):
        if self.selected:
            success = self.board.move(self.selected, row, col)
            if success:
                #self.selected = None
                self.display.show_background(self.win)
                self.display.show_pieces(self.win)
                return True
        return False

    def reset(self):
        # Initializes the Game object with the same instances which resets the game
        self.__init__(self.win, self.display, self.board)


