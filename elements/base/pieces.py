import abc


class Pieces:

    def __init__(self, i, j, team):
        self.i = i
        self.j = j
        self.team = team

    @abc.abstractmethod
    def possible_moves(self, board):
        pass

    @abc.abstractmethod
    def possible_eats(self, board):
        pass

    def get_position(self):
        return [self.i, self.j]
