import pygame,sys
import os
from Board_GUI import *
import Pieces 
import Bin
import Player

pygame.init()
gameVariables = Bin.gameVariables()

class GameFunctions:
    def __init__(self):
        self.Run = True                          #Run game Boolean
        
    def exitWindowFunc(self):
        #Check for close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT :       #Pygame.QUIT is library defined constant
                sys.exit()
                self.Run = False

Game = GameFunctions() 
Player1 = Player.Player(True) 
Player2 = Player.Player(False)
while Game.Run :
    #check for close window event
    Game.exitWindowFunc()
    
    generate_row_rects(gameVariables.Screen_width, gameVariables.Screen_height, gameVariables.GameBoard)
    #gameVariables.GameBoard.blit(Bin.Chess_Images.blk_bishop,(75,0))
    for i in Player1.army:
        gameVariables.GameBoard.blit(i.img,(i.y*75,i.x*75))
    for i in Player2.army:
        gameVariables.GameBoard.blit(i.img,(i.y*75,i.x*75))

    pygame.display.update();

#close window if out of loop -This will get rid of the error when you force close
pygame.quit()



