import elements.base.id


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
                        id_num = f + t*10
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

    def get_instance(self, i, j):
        return self.instances[i][j]

    def print_board(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
