import Pieces

class Player():
    def __init__(self,side = True):
        self.side = side
        self.army = []

        if self.side:
            R1  = Pieces.Rook(0,0,self.side) 
            Kn1 = Pieces.Knight(0,1,self.side) 
            B1  = Pieces.Bishop(0,2,self.side)
            Q   = Pieces.Queen(0,3,self.side)
            K   = Pieces.King(0,4,self.side)
            B2  = Pieces.Bishop(0,5,self.side)
            Kn2 = Pieces.Knight(0,6,self.side)
            R2  = Pieces.Rook(0,7,self.side)
            
            P1 = Pieces.Pawn(1,0,self.side)
            P2 = Pieces.Pawn(1,1,self.side)
            P3 = Pieces.Pawn(1,2,self.side)
            P4 = Pieces.Pawn(1,3,self.side)
            P5 = Pieces.Pawn(1,4,self.side)
            P6 = Pieces.Pawn(1,5,self.side)
            P7 = Pieces.Pawn(1,6,self.side)
            P8 = Pieces.Pawn(1,7,self.side)
            
        else:
            R1  = Pieces.Rook(7,0,self.side)
            Kn1 = Pieces.Knight(7,1,self.side) 
            B1  = Pieces.Bishop(7,2,self.side)
            Q   = Pieces.Queen(7,3,self.side)
            K   = Pieces.King(7,4,self.side)
            B2  = Pieces.Bishop(7,5,self.side)
            Kn2 = Pieces.Knight(7,6,self.side)
            R2  = Pieces.Rook(7,7,self.side)
            
            P1 = Pieces.Pawn(6,0,self.side)
            P2 = Pieces.Pawn(6,1,self.side)
            P3 = Pieces.Pawn(6,2,self.side)
            P4 = Pieces.Pawn(6,3,self.side)
            P5 = Pieces.Pawn(6,4,self.side)
            P6 = Pieces.Pawn(6,5,self.side)
            P7 = Pieces.Pawn(6,6,self.side)
            P8 = Pieces.Pawn(6,7,self.side)

        self.army.append(R1)
        self.army.append(Kn1)
        self.army.append(B1)
        self.army.append(Q)
        self.army.append(K)
        self.army.append(B2)
        self.army.append(Kn2)
        self.army.append(R2)
        
        self.army.append(P1)
        self.army.append(P2)
        self.army.append(P3)
        self.army.append(P4)
        self.army.append(P5)
        self.army.append(P6)
        self.army.append(P7)
        self.army.append(P8)









