import pygame
from .constants import WHITE, RED, YELLOW, ROW, COL
from .board import Board

class Game:
    def __init__(self, win):
        self.win = win
        self.state = []
        self._init(win, self.state)

    def _init(self, win, state):
        self.turn = RED
        self.board = Board()
        self.board.new_board(win, state)
        self.champ = None

    def reset(self):
        self._init()

    def update(self):
        pygame.display.update()

    def winner(self, colour):
        self.champ = colour
        print("WINNER: ", self.champ)

    def mouseclick(self, row, col):

        #if self.selected:

        if row <= 0:
            full_column = False
            valid_move = False
            available_row = 0
            while not full_column and not valid_move:
                if(self.state[available_row][col] == WHITE):
                    self.board.draw_move(self.win, 6-available_row, col, self.turn)

                    self.state[available_row][col] = self.turn

                    self.board.print_state(self.state)

                    if(self.check_win()):
                        return True

                    if(self.turn == RED):
                        self.turn = YELLOW
                        print("Yellow's Turn")
                    else:
                        self.turn = RED
                        print("Red's Turn")
                    
                    valid_move = True

                available_row += 1

                if(available_row >= 6):
                    full_column = True
            
            return False

    def check_win(self):

        #check for horizontal wins
        for x in range(ROW-1):
            counter = 0
            colour = WHITE
            for y in range(COL):

                #check for win
                if counter >= 4:
                    self.winner(colour)
                    return True

                #break the chain
                if counter != 0 and self.state[x][y] != colour:
                    counter = 0
                    colour = self.state[x][y]

                #continuing count with piece
                if counter > 0 and self.state[x][y] == colour:
                    counter += 1

                #starting counter with new piece
                if counter == 0 and self.state[x][y] != WHITE:
                    counter += 1
                    colour = self.state[x][y]

        #check for vertical wins
        for y in range(COL):
            counter = 0
            colour = WHITE
            for x in range(ROW-1):

                #check for win
                if counter >= 4:
                    self.winner(colour)
                    return True

                #break the chain
                if counter != 0 and self.state[x][y] != colour:
                    counter = 0
                    colour = self.state[x][y]

                #continuing count with piece
                if counter > 0 and self.state[x][y] == colour:
                    counter += 1

                #starting counter with new piece
                if counter == 0 and self.state[x][y] != WHITE:
                    counter += 1
                    colour = self.state[x][y]

        #check for diagonal wins
        # for x in range(3):
        #     counter = 0
        #     colour = WHITE
        #     j = 0
        #     for i in range(ROW-1):
                
        #         if(self.state[i][j] == colour and self.state != WHITE):
        #             counter += 1
        #             if(counter >= 4):
        #                 return True
        #         else:
        #             counter = 0

        # for y in range(COL):
        #     for x in range(ROW-1):
        #         pass

        # diagonal NE
        for x in range(ROW-1):
            i = x
            j = 0
            while i+3 < 6 and j+3 < 7:
                if self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] and self.state[i][j] != WHITE:
                    colour = self.state[i][j]
                    self.winner(colour)
                    return True
                
                i += 1
                j += 1

        for y in range(1, COL):
            i = 0
            j = y
            while i+3 < 6 and j+3 < 7:
                if self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] and self.state[i][j] != WHITE:
                    colour = self.state[i][j]
                    self.winner(colour)
                    return True

                i += 1
                j += 1

        #diagonal SE
        for x in range(3, ROW-1):
            i = x
            j = 0
            while i-3 >= 0 and j+3 < 7:
                if self.state[i][j] == self.state[i-1][j+1] == self.state[i-2][j+2] == self.state[i-3][j+3] and self.state[i][j] != WHITE:
                    colour = self.state[i][j]
                    self.winner(colour)
                    return True
                
                i -= 1
                j += 1

        for y in range(1, COL):
            i = ROW-2
            j = COL
            while i-3 >= 0 and j+3 < 7:
                if self.state[i][j] == self.state[i-1][j+1] == self.state[i-2][j+2] == self.state[i-3][j+3] and self.state[i][j] != WHITE:
                    colour = self.state[i][j]
                    self.winner(colour)
                    return True
                
                i -= 1
                j += 1
        
        
        #win = straight_win or diagonal_win
        #return straight_win or diagonal_win
        return False