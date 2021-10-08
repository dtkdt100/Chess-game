import pieces.pawn
import pieces.knight
import pieces.rook
import pieces.bishop
import pieces.queen
import pieces.id


def create_board():
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
                    check_position = pieces.id.starting_positions[f]
                    if t == 1:
                        check_position = get_ending_position(check_position)
                    if [i, j] in check_position:
                        c = pieces.id.starting_positions_classes[f](i, j, t)
                        id_num = f
                        break
            board_1.append(id_num)
            instances_1.append(c)
        board.append(board_1)
        instances.append(instances_1)

    return board, instances


def print_2d_list(board):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))


def main():
    board = create_board()
    print_2d_list(board[0])


def paint_pos(board, pos):
    for po in pos:
        board[po[0]][po[1]] = 11
    print_2d_list(board)


def get_ending_position(positions):
    ending = []
    for pos in positions:
        ending.append([8 - pos[0] - 1, 8 - pos[1] - 1])
    return ending


if __name__ == '__main__':
    main()
