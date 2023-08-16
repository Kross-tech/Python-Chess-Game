import pygame
from .constants import *
from .board import Board
from .configuration import Configuration


class Display:
    def __init__(self, board):
        self.board = board
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.configuration = Configuration()

    # blit methods
    def show_background(self, window):
        theme = self.configuration.theme

        # iterates over each row and column and determines the color based off the position
        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                # rect
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                # blit
                pygame.draw.rect(window, color, rect)

    def show_pieces(self, window):
        for row in range(8):
            for col in range(8):
                square = self.board[row][col]
                if square is not None and square.has_piece():
                    piece = square.piece
                    texture = pygame.image.load(piece.texture)
                    # center the piece on the square
                    x = col * SQUARE_SIZE + SQUARE_SIZE // 2 - texture.get_width() // 2
                    y = row * SQUARE_SIZE + SQUARE_SIZE // 2 - texture.get_height() // 2
                    window.blit(texture, (x, y))

    def change_theme(self):
        self.configuration.change_theme()

