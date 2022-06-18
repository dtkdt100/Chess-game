from elements.base.pieces import Pieces
from moving_utilities.move_by_pattern import MoveByPattern


def get_id():
    return 3


def get_starting_position():
    return [[0, 0], [0, 7]]


moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Rook(Pieces):

    def possible_eats(self, board):
        m = MoveByPattern(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = MoveByPattern(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
