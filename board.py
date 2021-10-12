import elements.base.id
import pygame
from pygame_chess.pygame_colors_images import pink, orange
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
    return [[8 - pos[0] - 1, 8 - pos[1] - 1] for pos in positions]


def find_board_position(mouse_pos):
    return [(mouse_pos[i] // 100) for i in range(2)]


class Board:
    def __init__(self):
        board = init_screen()
        self.running = True
        self.board = board[0]
        self.instances = board[1]
        self.current_move_positions = []
        self.current_eat_positions = []
        self.current_instance_position = []
        self.start_running()

    def get_instance(self, pos):
        return self.instances[pos[0]][pos[1]]

    def get_id_board(self, pos):
        return self.board[pos[0]][pos[1]]

    def move_from(self, from_pos, to_pos):
        i_from = from_pos[0]
        j_from = from_pos[1]
        i_to = to_pos[0]
        j_to = to_pos[1]

        self.board[i_to][j_to] = self.get_id_board(from_pos)
        self.instances[i_to][j_to] = self.get_instance(from_pos)

        self.board[i_from][j_from] = 0
        self.instances[i_from][j_from] = None

        self.instances[i_to][j_to].move(to_pos)

    def handle_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = find_board_position(pygame.mouse.get_pos())
                if pos in self.current_move_positions:
                    pg_board.move(self.board, self.current_instance_position, pos, self.current_move_positions)
                    self.move_from(self.current_instance_position, pos)
                    self.current_instance_position = []
                    self.current_move_positions = []
                    self.current_eat_positions = []
                elif pos in self.current_eat_positions:
                    pg_board.move(self.board, self.current_instance_position, pos, self.current_eat_positions)
                    self.move_from(self.current_instance_position, pos)
                    self.clear_possible_move()
                elif len(self.current_move_positions) > 0 or len(self.current_eat_positions):
                    self.clear_possible_move()
                else:
                    instance = self.instances[pos[0]][pos[1]]
                    self.current_instance_position = pos
                    self.draw_possible_move(instance.possible_moves(self.board),
                                            instance.possible_eats([self.board, self.instances]))
            if event.type == pygame.QUIT:
                self.running = False

    def start_running(self):
        while self.running:
            self.handle_quit()
            pygame.display.flip()
        pygame.quit()

    def draw_possible_move(self, moves, eats):
        for pos in moves:
            pg_board.draw_rect(pos, col=pink)
        for pos in eats:
            pg_board.draw_rect(pos, col=orange)
        self.current_move_positions = moves
        self.current_eat_positions = eats
        pg_board.update()

    def clear_possible_move(self):
        self.current_instance_position = []
        for pos in self.current_move_positions:
            pg_board.draw_rect(pos)
        for pos in self.current_eat_positions:
            pg_board.draw_rect(pos)
            pg_board.draw_image(pos, self.board[pos[0]][pos[1]])
        pg_board.update()
        self.current_move_positions = []
        self.current_eat_positions = []
