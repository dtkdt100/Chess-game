from elements.base import pieces
from moving_utilities import move_by_pattern, move_with_jump_over


def get_id():
    return 1


def get_starting_position():
    return [[1, i] for i in range(8)]


class Pawn(pieces.Pieces):

    def possible_eats(self, board):
        if self.team == 0:
            eats = [[1, 1], [1, -1]]
        else:
            eats = [[-1, 1], [-1, -1]]
        m = move_with_jump_over.MoveWithJumpOver(self.i, self.j, board[0], eats, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        if self.team == 0:
            moves = [[1, 0]]
        else:
            moves = [[-1, 0]]
        m = move_by_pattern.MoveByPattern(self.i, self.j, board, moves, self.team, min_number=2)
        return m.possible_moves()
