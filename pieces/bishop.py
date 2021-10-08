import pieces.pieces
import move_different


def get_id():
    return 4


def get_starting_position():
    return [[0, 2], [0, 5]]


moves = [[1, 1], [1, -1], [-1, 1], [-1, -1]]


class Bishop(pieces.pieces.Pieces):

    def possible_eats(self, board):
        m = move_different.MoveDifferent(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = move_different.MoveDifferent(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
