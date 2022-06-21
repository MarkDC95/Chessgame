from Bin import Chess_Images
from abc import ABC,abstractmethod

class Pieces(ABC):
    @abstractmethod
    def __init__(self,x:int,y:int,side:bool):
        self.x = x
        self.y = y
        self.side  = side                       # True = Black
        self.Alive = True                       # Alive = on board

class King(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)                    
        self.img = Chess_Images.blk_king if self.side else Chess_Images.wht_king
        self.name = 'King' + str(self.x) +str(self.y)
    
class Queen(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_queen if self.side else Chess_Images.wht_queen
        self.name = 'Queen' + str(self.x) +str(self.y)

class Bishop(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_bishop if self.side else Chess_Images.wht_bishop
        self.name = 'Bishop' + str(self.x) +str(self.y)

class Rook(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_rook if self.side else Chess_Images.wht_rook
        self.name = 'Rook' + str(self.x) +str(self.y)

class Knight(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_knight if self.side else Chess_Images.wht_knight
        self.name = 'Knight' + str(self.x) +str(self.y)

class Pawn(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_pawn if self.side else Chess_Images.wht_pawn
        self.name = 'Pawn' + str(self.x) +str(self.y)
