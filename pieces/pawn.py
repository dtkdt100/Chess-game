import pieces.pieces
import move_different
import move


def get_id():
    return 1


def get_starting_position():
    return [[1, i] for i in range(8)]


class Pawn(pieces.pieces.Pieces):

    def possible_eats(self, board):
        eats = [[1, 1], [1, -2]]
        m = move.Move(self.i, self.j, board[0], eats, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        moves = [[1, 0]]
        m = move_different.MoveDifferent(self.i, self.j, board, moves, self.team, min_number=2)
        return m.possible_moves()
