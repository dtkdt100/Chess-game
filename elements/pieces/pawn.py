from elements.base.pieces import Pieces
from moving_utilities.move_by_pattern import MoveByPattern
from moving_utilities.move_with_jump_over import MoveWithJumpOver


def get_id():
    return 1


def get_starting_position():
    return [[1, i] for i in range(8)]


class Pawn(Pieces):

    def possible_eats(self, board):
        if self.team == 0:
            eats = [[1, 1], [1, -1]]
        else:
            eats = [[-1, 1], [-1, -1]]
        m = MoveWithJumpOver(self.i, self.j, board[0], eats, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        if self.team == 0:
            moves = [[1, 0]]
        else:
            moves = [[-1, 0]]
        m = MoveByPattern(self.i, self.j, board, moves, self.team, min_number=2)
        return m.possible_moves()
