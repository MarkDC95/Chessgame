
import Pieces

class Player():
    def __init__(self,side):
        self.side = side
        self.army = []
        if self.side:
            R1  = Pieces.Rook(0,0,side) 
            Kn1 = Pieces.Knight(0,1,side) 
            B1  = Pieces.Bishop(0,2,side)
            Q   = Pieces.Queen(0,3,side)
            K   = Pieces.King(0,4,side)
            B2  = Pieces.Bishop(0,5,side)
            Kn2 = Pieces.Knight(0,6,side)
            R2  = Pieces.Rook(0,7,side)
            
            P1 = Pieces.Pawn(1,0,side)
            P2 = Pieces.Pawn(1,1,side)
            P3 = Pieces.Pawn(1,2,side)
            P4 = Pieces.Pawn(1,3,side)
            P5 = Pieces.Pawn(1,4,side)
            P6 = Pieces.Pawn(1,5,side)
            P7 = Pieces.Pawn(1,6,side)
            P8 = Pieces.Pawn(1,7,side)

        else:
            R1  = Pieces.Rook(7,0,side)
            Kn1 = Pieces.Knight(7,1,side) 
            B1  = Pieces.Bishop(7,2,side)
            Q   = Pieces.Queen(7,3,side)
            K   = Pieces.King(7,4,side)
            B2  = Pieces.Bishop(7,5,side)
            Kn2 = Pieces.Knight(7,6,side)
            R2  = Pieces.Rook(7,7,side)
            
            P1 = Pieces.Pawn(6,0,side)
            P2 = Pieces.Pawn(6,1,side)
            P3 = Pieces.Pawn(6,2,side)
            P4 = Pieces.Pawn(6,3,side)
            P5 = Pieces.Pawn(6,4,side)
            P6 = Pieces.Pawn(6,5,side)
            P7 = Pieces.Pawn(6,6,side)
            P8 = Pieces.Pawn(6,7,side)

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









