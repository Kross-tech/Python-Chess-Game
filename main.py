import sys
import pygame
from source.constants import *
from source.display import Display
from source.board import Board
from source.game import Game



# set window size
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# set game title
pygame.display.set_caption("Keonte' Chess Game")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    clock = pygame.time.Clock()
    board = Board()
    display = Display(board)
    game = Game(WINDOW, display, board)

    running = True

    while running:
        # set frame rate
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                if not game.select(row, col):
                    game._move(row, col)

            elif event.type == pygame.KEYDOWN:

                # reset the game
                if event.key == pygame.K_r:
                    game.reset()
                    board = Board()
                    display = Display(board)
                    game = Game(WINDOW, display, board)

                # change the theme of the game
                if event.key == pygame.K_t:
                    display.change_theme()

            # quits the application
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        display.show_background(WINDOW)
        display.show_pieces(WINDOW)

        # applies changes
        pygame.display.update()


if __name__ == '__main__':
    main()
