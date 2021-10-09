from elements.base import pieces
from moving_utilities import move_with_jump_over


def get_id():
    return 5


def get_starting_position():
    return [[0, 4]]


moves = [[1, 1], [1, 0], [1, -1], [0, -1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]


class King(pieces.Pieces):

    def possible_eats(self, board):
        m = move_with_jump_over.MoveWithJumpOver(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = move_with_jump_over.MoveWithJumpOver(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
