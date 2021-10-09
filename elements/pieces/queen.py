from elements.base import pieces
from moving_utilities import move_by_pattern
import elements.pieces.rook
import elements.pieces.bishop


def get_id():
    return 6


def get_starting_position():
    return [[0, 3]]


moves = elements.pieces.rook.moves + elements.pieces.bishop.moves


class Queen(pieces.Pieces):

    def possible_eats(self, board):
        m = move_by_pattern.MoveByPattern(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = move_by_pattern.MoveByPattern(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
