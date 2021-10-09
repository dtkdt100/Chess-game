# moves: [one possible list of moves, one possible list of moves]
# The "," is or

# one possible list of moves - [how much to move i, how much to move j] - could be negative

# Examples:
# moves = [[1, 0], [2, 0]]

# If the one move is [1, 1], it moves to slant - len()*[1, 1]


class MoveByPattern:
    def __init__(self, i, j, board, moves, team, min_number=7):
        self.i = i
        self.j = j
        self.board = board
        self.moves = moves
        self.team = team
        self.min = min_number

    def __moves_eats(self, check_instances=False, instances=None):
        possible_moves = []
        possible_eats = []
        for one_moves in self.moves:
            n = 0
            i = self.i + one_moves[0]
            j = self.j + one_moves[1]
            for num in range(self.min):
                if i > len(self.board) - 1 or i < 0 or j > len(self.board) - 1 or j < 0:
                    break
                elif self.board[i][j] > 0:
                    if check_instances:
                        if not instances[i][j].team == self.team:
                            possible_eats.append([i, j])
                    break
                else:
                    possible_moves.append([i, j])
                    i += one_moves[0]
                    j += one_moves[1]
                    n += 1

        return possible_moves, possible_eats

    def possible_moves(self):
        return self.__moves_eats()[0]

    def possible_eats(self, instances):
        return self.__moves_eats(check_instances=True, instances=instances)[1]
