from elements.base.pieces import Pieces
from moving_utilities.move_by_pattern import MoveByPattern
import elements.pieces.rook
import elements.pieces.bishop


def get_id():
    return 6


def get_starting_position():
    return [[0, 3]]


moves = elements.pieces.rook.moves + elements.pieces.bishop.moves


class Queen(Pieces):

    def possible_eats(self, board):
        m = MoveByPattern(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = MoveByPattern(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
