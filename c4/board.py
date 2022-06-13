import pygame
from .constants import RED, YELLOW, WHITE, BLUE, GREEN, WIDTH, HEIGHT, ROW, COL, SQUARE_SIZE

class Board:
    def __init__(self):
        pass

    def draw_move(self, win, row, col, colour):
        pygame.draw.circle(win, colour, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 35)

    def draw_slots(self, win, row, col):
        if row <= 0:
            pygame.draw.polygon(win, GREEN, [[(SQUARE_SIZE * col) + SQUARE_SIZE//4, 30], [(SQUARE_SIZE * col) + SQUARE_SIZE//2, 60], [(SQUARE_SIZE * col) + 3*SQUARE_SIZE//4, 30]])
        else:
            self.draw_move(win, row, col, WHITE)

    def draw_new_board(self, win):
        win.fill(BLUE)
        for row in range(ROW):
            for col in range(COL):
                self.draw_slots(win, row, col)

    def new_board(self, win, state):
        self.draw_new_board(win)
        for row in range(ROW-1):
            state.append([])
            for col in range(COL):
                state[row].append(WHITE)
        
        #TESTING
        self.print_state(state)
        
    #TESTING
    def print_state(self, state):
        for row in range(ROW-1):
            for col in range(COL):
                print(str(row) + ", " + str(col) + ": ", state[row][col])