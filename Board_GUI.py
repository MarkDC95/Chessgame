import pygame
import os


pygame.init()

win_width, win_height = 600, 600
Square_width  = win_width//8
Square_height = win_height//8

# Game board sreen x by y pixels
#GameBoard = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Chess Board")


# Load images of the pieces
blk_bishop = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_bishop.png")),(Square_width,Square_height))

blk_rook = pygame.image.load(os.path.join("Chess pieces", "Blk_rook.png"))
blk_king = pygame.image.load(os.path.join("Chess pieces", "Blk_king.png"))
blk_queen = pygame.image.load(os.path.join("Chess pieces", "Blk_queen.png"))
blk_pawn = pygame.image.load(os.path.join("Chess pieces", "Blk_pawn.png"))
blk_knight = pygame.image.load(os.path.join("Chess pieces", "Blk_knight.png"))

wht_bishop = pygame.image.load(os.path.join("Chess pieces", "Wht_bishop.png"))
wht_rook = pygame.image.load(os.path.join("Chess pieces", "Wht_rook.png"))
wht_king = pygame.image.load(os.path.join("Chess pieces", "Wht_king.png"))
wht_queen = pygame.image.load(os.path.join("Chess pieces", "Wht_queen.png"))
wht_pawn = pygame.image.load(os.path.join("Chess pieces", "Wht_pawn.png"))
wht_knight = pygame.image.load(os.path.join("Chess pieces", "Wht_knight.png"))

#Colour constants
BLUE  = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)



def generate_row_rects (win_width, win_height, window):
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
                colour  = BLACK
            else:
                colour = WHITE

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