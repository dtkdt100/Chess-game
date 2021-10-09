from elements.base import pieces
from moving_utilities import move_by_pattern


def get_id():
    return 3


def get_starting_position():
    return [[0, 0], [0, 7]]


moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Rook(pieces.Pieces):

    def possible_eats(self, board):
        m = move_by_pattern.MoveByPattern(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = move_by_pattern.MoveByPattern(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
