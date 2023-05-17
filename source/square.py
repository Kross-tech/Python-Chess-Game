class Square:
    # # represents the row and col coordinates of a square and the piece placed on it
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None

    # def isempty(self):
    #     return not self.has_piece()

    # allows me to call a method without creating an object for it
    @staticmethod
    # *args can receive a lot of parameters
    def is_within_bounds(*args):
        # checks if the argument is outside the board
        for arg in args:
            if arg < 0 or arg > 7:
                return False

        return True
