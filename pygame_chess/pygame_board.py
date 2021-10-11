from pygame_chess.pygame_colors_images import black, white, images

size_cell = 100


class PygameBoard:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    def draw_rect(self, pos, col=black):
        if (pos[0] + pos[1]) % 2 == 0 and col == black:
            col = white
        self.pygame.draw.rect(self.screen, col, [size_cell * pos[0], size_cell * pos[1], size_cell, size_cell])

    def update(self):
        self.pygame.display.update()

    def draw_all_board_images(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 0:
                    self.draw_image([i, j], board[i][j])

    def draw_image(self, pos, id_number):
        image = self.pygame.image.load(images[id_number])
        image = self.pygame.transform.scale(image, (80, 80))
        self.screen.blit(image, (10 + pos[0] * 100, 10 + pos[1] * 100))
