import pygame
import Bin

class checkered: 
    def generate_row_rects(win_width:int, win_height:int, window:pygame.Surface)-> None:
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
                    colour  = Bin.colour.WHITE
                else:
                    colour = Bin.colour.GRAY

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
    #alphaClassList = ['A','B','C','D','E','F','G','H']

    def __init__(self, row:int, col:int):
        self.name = str(row) + ',' + str(col)
        self.row = row
        self.col = col
        self.occ = False
        self.bead = None
        self.drawCord = (Bin.gameVariables.Square_width*self.col, Bin.gameVariables.Square_width*self.col*self.row)

class BEboard:
    def boardMapCreate() -> list[list]:
        '''Returns 2D array with class of chess tile variables'''
        #blank 2D 8x8 array 
        grid = [[0 for _ in range(8)] for _ in range(8)]
        #add chesstiles to blank slots
        for i in range(8):
            for j in range(8):
                grid[i][j] = ChessTile(i,j)
        return grid

    def boardupdate(grid,army_list1:list,army_list2:list):
        """updates player 1 and 2 piece objects"""
        if army_list1 and army_list2 :
            for i in army_list1:
                grid[i.y][i.x].occ = True
                grid[i.y][i.x].bead = i
            
            for i in army_list2:
                grid[i.y][i.x].occ = True
                grid[i.y][i.x].bead = i
        
        





    



