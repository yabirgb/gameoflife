import random
import time
import sys, os


class Board(object):
    def generate_board(self):
        for i in range(self.TABLE_HEIGHT):
            self.BOARD.append([])
            for j in range(self.TABLE_WIDTH):
                self.BOARD[i].append(0)

    def draw(self):
        st = ""
        os.system("clear")
        for i in range(self.TABLE_HEIGHT-1):
            for j in range(self.TABLE_WIDTH-1):
                if self.BOARD[i][j] == 1:
                    st += " O "
                else:
                    st += " . "
            st += "\n"
        print(st)
        time.sleep(1)


    def populate(self):
        for z in range(self.initial_population):
            i = random.randint(0,self.TABLE_HEIGHT-1)
            j = random.randint(0,self.TABLE_WIDTH-1)
            self.BOARD[i][j] = 1

    def play(self):
        cells = []
        for i in range(self.TABLE_HEIGHT):
            for j in range(self.TABLE_WIDTH):
                has_right, has_bottom, has_left, has_above = False, False, False, False
                cell = self.BOARD[i][j]
                if i < self.TABLE_HEIGHT-1:
                    has_bottom = True
                if j < self.TABLE_WIDTH-1:
                    has_right = True
                if i != 0:
                    has_above = True
                if j != 0:
                    has_left = True

                around = 0
                #     +
                #  +  O   +
                #     +
                if has_right:
                    around += self.BOARD[i][j+1]
                if has_bottom:
                    around += self.BOARD[i+1][j]
                if has_left:
                    around += self.BOARD[i][j-1]
                if has_above:
                    around += self.BOARD[i-1][j]
                #  +      +
                #     O
                #  +      +

                if has_above and has_left:
                    around += self.BOARD[i-1][j-1]
                if has_above and has_right:
                    around += self.BOARD[i-1][j+1]
                if has_bottom and has_left:
                    around += self.BOARD[i+1][j-1]
                if has_bottom and has_right:
                    around += self.BOARD[i+1][j+1]

                cells.append((i,j, self.BOARD[i][j], around))
        return cells

    def laws(self, cells):
        for cell in cells:
            if cell[2] == 1 and cell[3] < 2:
                self.BOARD[cell[0]][cell[1]] = 0
            if cell[2] == 1 and cell[3] > 3:
                self.BOARD[cell[0]][cell[1]] = 0
            if cell[2] == 0 and cell[3] == 3:
                self.BOARD[cell[0]][cell[1]] = 1



    def __init__(self):
        #Initial Values
        self.TABLE_WIDTH = 50
        self.TABLE_HEIGHT = 40
        self.initial_population = 250 #max population
        self.number_of_generations = 30
        self.BOARD = []
        #Generate Board with values provided
        self.generate_board()
        self.populate()
        self.draw()

        for i in range(self.number_of_generations):
            self.laws( self.play() )
            self.draw()
bb = Board()
