import pygame
from .constants import *
from .board import Board


class Display:
    def __init__(self, board):
        self.board = board
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

    # blit methods
    def show_background(self, window):
        # iterates over each row and column and determines the color based off the position
        for row in range(ROWS):
            for col in range(COLS):
                # color
                if (row + col) % 2 == 0:
                    color = 'red'
                else:
                    color = 'blue'
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



