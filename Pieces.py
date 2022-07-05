from Bin import Chess_Images
from abc import ABC, abstractmethod

class Pieces(ABC):
    @abstractmethod
    def __init__(self,x:int,y:int,side:bool):
        self.x = x
        self.y = y
        self.side  = side                       # True = Black
        self.tag = 'Blk' if side else 'Wht'     # Naming automation
        self.Alive = True                       # Alive = on board

    def Inbound(x,y):
        pass

class King(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)                    
        self.img = Chess_Images.blk_king if self.side else Chess_Images.wht_king
        self.name = self.tag + ' ' + 'King'+ ' ' + str(self.y) +str(self.x)
    
class Queen(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_queen if self.side else Chess_Images.wht_queen
        self.name = self.tag + ' ' + 'Queen'+ ' ' + str(self.y) +str(self.x)

class Bishop(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_bishop if self.side else Chess_Images.wht_bishop
        self.name = self.tag + ' ' + 'Bishop'+ ' ' + str(self.y) +str(self.x)

class Rook(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_rook if self.side else Chess_Images.wht_rook
        self.name = self.tag + ' ' + 'Rook'+ ' ' + str(self.y) +str(self.x)

class Knight(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_knight if self.side else Chess_Images.wht_knight
        self.name = self.tag + ' ' + 'Knight'+ ' ' + str(self.y) +str(self.x)

class Pawn(Pieces):
    def __init__(self,x,y,side):
        Pieces.__init__(self,x,y,side)
        self.img = Chess_Images.blk_pawn if self.side else Chess_Images.wht_pawn
        self.name = self.tag + ' ' + 'Pawn'+ ' ' + str(self.y) +str(self.x)

    def move(self,xnew,ynew,):
        if self.side:
            self.x +=1



