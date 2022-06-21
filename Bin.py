import pygame
import os

class gameVariables:
    #Game board sreen x by y pixels
    Screen_width, Screen_height = 600, 600
    #Tile height and width
    Square_width  = Screen_width//8
    Square_height = Screen_height//8
    #window name
    GameBoard = pygame.display.set_mode((Screen_width, Screen_height))
    pygame.display.set_caption("Chess Board by Mark DC")


class Chess_Images:
    #Load images of the pieces
    blk_bishop = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_bishop.png")),(gameVariables.Square_width,gameVariables.Square_height))
    blk_rook   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_rook.png")),(gameVariables.Square_width,gameVariables.Square_height))
    blk_king   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_king.png")),(gameVariables.Square_width,gameVariables.Square_height))
    blk_queen  = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_queen.png")),(gameVariables.Square_width,gameVariables.Square_height))
    blk_pawn   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_pawn.png")),(gameVariables.Square_width,gameVariables.Square_height))
    blk_knight = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Blk_knight.png")),(gameVariables.Square_width,gameVariables.Square_height))

    wht_bishop = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_bishop.png")),(gameVariables.Square_width,gameVariables.Square_height))
    wht_rook   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_rook.png")),(gameVariables.Square_width,gameVariables.Square_height))
    wht_king   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_king.png")),(gameVariables.Square_width,gameVariables.Square_height))
    wht_queen  = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_queen.png")),(gameVariables.Square_width,gameVariables.Square_height))
    wht_pawn   = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_pawn.png")),(gameVariables.Square_width,gameVariables.Square_height))
    wht_knight = pygame.transform.scale(pygame.image.load(os.path.join("Chess pieces", "Wht_knight.png")),(gameVariables.Square_width,gameVariables.Square_height))


class colour:
    #Colour constants
    BLUE  = (0,0,255)
    WHITE = (255,255,255)
    GRAY = (150,150,150)
    BLACK = (0,0,0)
    RED   = (255,0,0)
