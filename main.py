import board
import json


def main():
    b = board.Board()
    b.print_board(index=True)

    while True:
        pos = json.loads(input("Type the position of the piece that you want to move: "))
        instance = b.get_instance(pos)
        moves = instance.possible_moves(b.board)
        eats = instance.possible_eats([b.board, b.instances])
        print("You can move to: " + str(moves) + " and eat: " + str(eats))
        b.print_possible_moves(moves, eats=eats)
        eat_move = int(input("Type move 1, eat 2 "))
        index = int(input("Type the index of the position you want to move or eat to: "))

        if eat_move == 1:
            action = moves[index]
        else:
            action = eats[index]
        b.move_from(instance.get_position(), action)
        b.print_board()


if __name__ == '__main__':
    main()
