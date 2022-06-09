"""Test board format DB for chess Pieces"""
from pandas import array


alphaClassList = ['A','B','C','D','E','F','G','H']
class ChessTile:
    def __init__(self, row:int, col:int):
        self.name = alphaClassList[row] + ',' + str(col)
        self.row = row
        self.col = col
        self.occ = False
        self.drawCord = (75*self.col, 75*self.row)

def namingFunc():
    player_1_NP = ["R1","Kn1","B1","Q","K","B2","Kn2","R2"]
    player_1_P  = ["P1","P2","P3","P4","P5","P6","P7","P8"]

    player_2_NP = ["R1","Kn1","B1","Q","K","B2","Kn2","R2"]
    player_2_P  = ["P1","P2","P3","P4","P5","P6","P7","P8"]

def boardMapCreate() -> list[list]:
    '''Returns 2D array with class of chess tile variables'''
    grid = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            grid[i][j] = ChessTile(i,j)
    return grid

board = boardMapCreate()


