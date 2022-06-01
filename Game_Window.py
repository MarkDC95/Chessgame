import pygame,sys
import os
from Board_GUI import *

pygame.init()

# Game board sreen x by y pixels
Screen_width, Screen_height = 600, 600

#window name
GameBoard = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Chess Board by Mark DC")

Run = True

#game loop 
while Run :
    #checkfor close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT : #Pygame.QUIT is library defined constant
            sys.exit()
            Run = False
    
    generate_row_rects(Screen_width, Screen_height, GameBoard)
    GameBoard.blit(blk_bishop,(75,0))
    pygame.display.update();
    
    





#close window if out of loop -This will get rid of the error when you force close-
pygame.quit()
