import pieces.pieces
import move_different
import pieces.rook
import pieces.bishop


def get_id():
    return 6


def get_starting_position():
    return [[0, 3]]


moves = pieces.rook.moves + pieces.bishop.moves


class Queen(pieces.pieces.Pieces):

    def possible_eats(self, board):
        m = move_different.MoveDifferent(self.i, self.j, board[0], moves, self.team)
        return m.possible_eats(board[1])

    def possible_moves(self, board):
        m = move_different.MoveDifferent(self.i, self.j, board, moves, self.team)
        return m.possible_moves()
