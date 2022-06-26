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

    def isOver(self):
        mouse = pygame.mouse.get_pos()
        x = (mouse[0]//75) * 75
        y = (mouse[1]//75) * 75
        pygame.draw.rect(gameVariables.GameBoard,Bin.colour.BLUE,(x,y,75,75))


Game = GameFunctions() 
Player1 = Player.Player(True) 
Player2 = Player.Player(False)
board = BEboard.boardMapCreate()

while Game.Run :
    #check for close window event
    Game.exitWindowFunc()
    
    checkered.generate_row_rects(gameVariables.Screen_width, gameVariables.Screen_height, gameVariables.GameBoard)

    for i in Player1.army:
        gameVariables.GameBoard.blit(i.img,(i.y*75,i.x*75))
    for i in Player2.army:
        gameVariables.GameBoard.blit(i.img,(i.y*75,i.x*75))
    
    BEboard.boardupdate(board,Player1.army,Player2.army)

    Game.isOver()

    pygame.display.update();

    

#close window if out of loop -This will get rid of the error when you force close
pygame.quit()




