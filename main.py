import pygame,sys
import os
from Board_GUI import *
import Pieces 
import Bin
import Player as person

pygame.init()
gameVariables = Bin.gameVariables()

class GameFunctions:
    def __init__(self):
        self.Run = True                          #Bool for game Loop
        self.selector = (None , None)
        self.ColourFlag = Bin.colour.BLUE

    def exitWindowFunc(self):
        #Check for close window event
        for event in pygame.event.get():
            if event.type == pygame.QUIT :       #Pygame.QUIT is library defined constant
                sys.exit()
                self.Run = False

    def isOver(self):
        """Checks the mouse input coordinates"""
        mouse = pygame.mouse.get_pos()              
        xCord = (mouse[0]//gameVariables.Square_width) * gameVariables.Square_width
        yCord = (mouse[1]//gameVariables.Square_width) * gameVariables.Square_width
        
        #Selection square GUI indicator using mouse coordinates mapped to grid
        pygame.draw.rect(gameVariables.GameBoard,self.ColourFlag,(xCord,yCord,75,75))

        for event in pygame.event.get():
            if  event.type == pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pressed()[0]):
                    self.selector = (xCord//gameVariables.Square_width, yCord//gameVariables.Square_width)
                    #print(self.selector)
                    self.ColourFlag = Bin.colour.RED if self.ColourFlag == Bin.colour.BLUE else Bin.colour.BLUE
                    return self.selector

            #exit Window function
            if event.type == pygame.QUIT :       #Pygame.QUIT is library defined constant
                sys.exit()
                self.Run = False

    def itemize(self,selector):
        pass


Game = GameFunctions() 
Player1 = person.Player(True)                       # True Black
Player2 = person.Player(False)                      # False White
board = BEboard.boardMapCreate()

while Game.Run :
    #check for close window event
    Game.exitWindowFunc()
    
    #generate background pixels in each run of the loop
    checkered.generate_row_rects(gameVariables.Screen_width, gameVariables.Screen_height, gameVariables.GameBoard)

    #update Player 1 and 2 Pieces data to GUI board 
    for i in Player1.army:
        gameVariables.GameBoard.blit(i.img,(i.y*gameVariables.Square_width,i.x*gameVariables.Square_width))
    for i in Player2.army:
        gameVariables.GameBoard.blit(i.img,(i.y*gameVariables.Square_width,i.x*gameVariables.Square_width))
    
    BEboard.boardupdate(board,Player1.army,Player2.army)


    #gets hover mouse coordinates
    ptr = Game.isOver()
    #tuple pointer[x axis,y axis]
    if ptr is not None:
        x1 = ptr[0]
        y1 = ptr[1]
        #check if the board location of tuple is not empty
        if board[x1][y1].occ:
           print (board[ptr[0]][ptr[1]].name, board[ptr[0]][ptr[1]].bead.name )
           
        else: 
            print(None)

    pygame.display.update();

    

#close window if out of loop -This will get rid of the error when you force close
#pygame.quit()




