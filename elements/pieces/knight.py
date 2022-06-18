from elements.base.pieces import Pieces
from moving_utilities.move_with_jump_over import MoveWithJumpOver


def get_id():
    return 2


def get_starting_position():
    return [[0, 1], [0, 6]]


moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, -1], [-2, 1]]


class Knight(Pieces):

    def possible_eats(self, board):
        m = MoveWithJumpOver(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = MoveWithJumpOver(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
