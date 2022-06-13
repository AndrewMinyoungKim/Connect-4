import pygame

from c4 import WIDTH, HEIGHT, SQUARE_SIZE
from c4.game import Game

class Play:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Connect 4')

    def get_row_col_from_mouse(self, pos):
        x, y = pos  #tuple
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.game = Game(self.window)

        while not self.done:

            self.clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.row, self.col = self.get_row_col_from_mouse(self.pos)

                    self.done = self.game.mouseclick(self.row, self.col)

            self.game.update()
        
        pygame.quit()

if __name__ == '__main__':
    play = Play()
    play.run()