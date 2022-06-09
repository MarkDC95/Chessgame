import pygame,sys
import os
from Board_GUI import *
from test import *

pygame.init()

# Game board sreen x by y pixels
Screen_width, Screen_height = 600, 600
#window name
GameBoard = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Chess Board by Mark DC")


class GameFunctions:
    def __init__(self):
        self.Turn  = 0 
        self.Player1 = 0 
        self.player2 = 0
        self.Run = True


    def exitWindowFunc(self):
        #checkfor close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT : #Pygame.QUIT is library defined constant
                sys.exit()
                self.Run = False

Game = GameFunctions() 
while Game.Run :
    #check for close window event
    Game.exitWindowFunc()
    
    generate_row_rects(Screen_width, Screen_height, GameBoard)
    #GameBoard.blit(blk_bishop,board[0][2].drawCord)
    #GameBoard.blit(blk_queen,board[0][3].drawCord)
    pygame.display.update();
    

#close window if out of loop -This will get rid of the error when you force close-
pygame.quit()



