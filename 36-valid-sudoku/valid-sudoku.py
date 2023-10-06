class Solution(object):
 def isValidSudoku(self,board):
    
    def check(lis):
        uniq = ['1','2','3','4','5','6','7','8','9']
        for i in lis:
            if (i in uniq):
                val = i
                uniq.remove(val)
                if (i == lis[8]):
                    i='.'
                    
            elif(i=="."):
                continue
            elif(i not in uniq):
                break
            
        if (i not in uniq and i!="." and len(uniq)!=0 ):
                return False
        return True
    def getblock(bo,x):
        lis = [(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        i,j = lis[x]
        return [bo[i-1][j-1], bo[i-1][j], bo[i-1][j+1], bo[i][j-1], bo[i][j], bo[i][j+1], bo[i+1][j-1], bo[i+1][j], bo[i+1][j+1] ]

    #check rows
    for i in range(0,9):
        if not check(board[i]):
            return False
    
    #check columns
    transposed_board = [[board[j][i] for j in range(9)] for i in range(9)]
    for i in range(0,9):
        if not check(transposed_board[i]):
            return False

    #check for blocks
    for i in range (0,9):
        block = getblock(board,i)
        if not check(block):
            return False       


    return True