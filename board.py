import elements.base.id
from pandas import DataFrame
from IPython.display import HTML


def __create_board__():
    board = []
    instances = []
    for i in range(8):
        board_1 = []
        instances_1 = []
        for j in range(8):
            c = None
            id_num = 0
            for t in range(2):
                for f in range(1, 7):
                    check_position = elements.base.id.starting_positions[f]
                    if t == 1:
                        check_position = __get_ending_position(check_position)
                    if [i, j] in check_position:
                        c = elements.base.id.starting_positions_classes[f](i, j, t)
                        id_num = f + t * 10
                        break
            board_1.append(id_num)
            instances_1.append(c)
        board.append(board_1)
        instances.append(instances_1)

    return board, instances


def __get_ending_position(positions):
    ending = []
    for pos in positions:
        ending.append([8 - pos[0] - 1, 8 - pos[1] - 1])
    return ending


class Board:
    def __init__(self):
        board = __create_board__()
        self.board = board[0]
        self.instances = board[1]

    def get_instance(self, pos):
        return self.instances[pos[0]][pos[1]]

    def print_board(self, board2=None, index=False):
        if board2 is None:
            board = self.board
        else:
            board = board2

        if index:
            print(DataFrame(board).to_string())
        else:
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))

    def move_from(self, from_pos, to_pos):
        i_from = from_pos[0]
        j_from = from_pos[1]
        i_to = to_pos[0]
        j_to = to_pos[1]

        self.board[i_to][j_to] = self.board[i_from][j_from]
        self.instances[i_to][j_to] = self.instances[i_from][j_from]

        self.board[i_from][j_from] = 0
        self.instances[i_from][j_from] = None

        self.instances[i_to][j_to].move(to_pos)

    def print_possible_moves(self, positions, eats=None):
        if eats is None:
            eats = []
        board2 = [row.copy() for row in self.board]
        for pos in positions:
            board2[pos[0]][pos[1]] = -1
        for pos in eats:
            board2[pos[0]][pos[1]] = -2
        self.print_board(board2=board2)
