# moves: [one possible list of moves, one possible list of moves]
# The "," is or

# one possible list of moves - [how much to move i, how much to move j] - could be negative

# Examples:
# moves = [[1, 0], [2, 0]]


class MoveWithJumpOver:
    def __init__(self, i, j, board, moves, team):
        self.i = i
        self.j = j
        self.board = board
        self.moves = moves
        self.team = team

    def _condition_i_last(self, one_moves):
        return not self.i + one_moves[0] > len(self.board) - 1

    def _condition_i_begin(self, one_moves):
        return not self.i + one_moves[0] < 0

    def _condition_j_last(self, one_moves):
        return not self.j + one_moves[1] > len(self.board) - 1

    def _condition_j_begin(self, one_moves):
        return not self.j + one_moves[1] < 0

    def _all_conditions(self, one_moves):
        return self._condition_i_last(one_moves) and self._condition_i_begin(one_moves) and self._condition_j_last(
            one_moves) and self._condition_j_begin(one_moves)

    def possible_moves(self):
        possible_moves = []
        for one_moves in self.moves:
            if self._all_conditions(one_moves):
                if self.board[self.i + one_moves[0]][self.j + one_moves[1]] == 0:
                    possible_moves.append([self.i + one_moves[0], self.j + one_moves[1]])

        return possible_moves

    def possible_eats(self, instances):
        possible_eats = []
        for one_moves in self.moves:
            if self._all_conditions(one_moves):
                if (not self.board[self.i + one_moves[0]][self.j + one_moves[1]] == 0) and not self.team == \
                        instances[self.i + one_moves[0]][self.j + one_moves[1]].team:
                    possible_eats.append([self.i + one_moves[0], self.j + one_moves[1]])

        return possible_eats
