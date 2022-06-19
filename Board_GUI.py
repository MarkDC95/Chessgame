import pygame
import os

pygame.init()

win_width, win_height = 600, 600
Square_width  = win_width//8
Square_height = win_height//8

# Game board sreen x by y pixels
#GameBoard = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Chess Board")

#Colour constants
BLUE  = (0,0,255)
WHITE = (255,255,255)
GRAY = (220,220,220)
BLACK = (0,0,0)
RED   = (255,0,0)



def generate_row_rects (win_width:int, win_height:int, window:pygame.Surface)-> None:
    """Function generates alternating black and white squares"""
    #chessboard pixels
    Square_width  = win_width//8
    Square_height = win_height//8
    #rectangle of each block 
    x0,y0 = 0, 0 
    colour_index = True
    
    for jj in range(8):
        #this one iterates horizontally on odd rows w then b 
        for ii in range (8):
            colour_ind = True

            if colour_index == True:
                colour  = RED
            else:
                colour = GRAY

            if ii % 2 == 0:
                rect = pygame.Rect(x0,y0,Square_width,Square_height)
                pygame.draw.rect(window, colour, rect)
            else:
                rect = pygame.Rect(x0,y0,Square_width,Square_height)
                pygame.draw.rect(window, colour, rect)
            x0 += Square_width
            colour_index = not(colour_index)
        y0 += Square_height
        colour_index = not(colour_index)
        x0 = 0

class ChessTile:
    alphaClassList = ['A','B','C','D','E','F','G','H']

    def __init__(self, row:int, col:int):
        self.name = ChessTile.alphaClassList[row] + ',' + str(col)
        self.row = row
        self.col = col
        self.occ = False
        self.drawCord = (75*self.col, 75*self.row)

def boardMapCreate() -> list[list]:
    '''Returns 2D array with class of chess tile variables'''
    grid = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            grid[i][j] = ChessTile(i,j)
    return grid

board = boardMapCreate()

