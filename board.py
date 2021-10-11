import elements.base.id
from pandas import DataFrame
import pygame
from pygame_chess.pygame_colors_images import pink
import elements.base.id
import pygame_chess.pygame_board

size_cell = 100
boardLength = 8
screen = pygame.display.set_mode([size_cell * boardLength for i in range(2)])

pg_board = pygame_chess.pygame_board.PygameBoard(pygame, screen)


def init_screen():
    pygame.init()
    screen.fill((0, 0, 0))
    return __create_board__()


def __create_board__():
    global pg_board

    board = []
    instances = []
    for i in range(8):
        board_1 = []
        instances_1 = []
        for j in range(8):
            c = None
            id_num = 0
            pg_board.draw_rect([i, j])
            for t in range(2):
                for f in range(1, 7):
                    check_position = elements.base.id.starting_positions[f]
                    if t == 1:
                        check_position = get_ending_position(check_position)
                    if [i, j] in check_position:
                        c = elements.base.id.starting_positions_classes[f](i, j, t)
                        id_num = f + t * 10
                        break

            board_1.append(id_num)
            instances_1.append(c)
        board.append(board_1)
        instances.append(instances_1)

    pg_board.draw_all_board_images(board)

    pg_board.update()
    return board, instances


def get_ending_position(positions):
    ending = []
    for pos in positions:
        ending.append([8 - pos[0] - 1, 8 - pos[1] - 1])
    return ending


def find_board_position(mouse_pos):
    return [mouse_pos[0] // 100, mouse_pos[1] // 100]


class Board:
    def __init__(self):
        board = init_screen()
        self.running = True
        self.board = board[0]
        self.instances = board[1]
        self.current_glow_positions = []
        self.start_running()

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

    def display_images(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.board[i][j] == 0:
                    pg_board.draw_image([i, j], self.board[i][j])

    def handle_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                pos = find_board_position(mouse_pos)
                instance = self.instances[pos[0]][pos[1]]
                self.draw_possible_move(instance.possible_moves(self.board))
            if event.type == pygame.QUIT:
                self.running = False

    def start_running(self):
        while self.running:
            self.handle_quit()
            pygame.display.flip()
        pygame.quit()

    def draw_possible_move(self, positions):
        for pos in positions:
            pg_board.draw_rect(pos, col=pink)
        self.current_glow_positions = positions
        pg_board.update()

    def clear_possible_move(self, positions):
        for pos in positions:
            pg_board.draw_rect(pos)
            # col = black
            # if (pos[0] + pos[1]) % 2 == 0:
            #     col = white
            # pygame.draw.rect(screen, col, [pos[0] * size_cell, pos[1] * size_cell, 100, 100])
        pg_board.update()
        self.current_glow_positions = []
