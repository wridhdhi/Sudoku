
import time
from sudokubase import sudoku



def backtrack_solver(board):
    '''recursive solver based on the generated game'''
    pass







def main():
    startT=time.time()
    s=sudoku() #Creates a board and all
    s.Generate()


    finT=time.time()-startT
    print(finT*1000.0,'ms')
    pass

if __name__=='__main__':
    main()