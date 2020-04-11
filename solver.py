
import time
from sudokubase import sudoku
from generator import sudokuGenerator


def backtrack_solver(board):
    '''recursive solver based on the generated game'''
    pass







def main():
    startT=time.time()
    # s=sudoku() #Creates a board and all
    # s.Generate()
    
    print('CAN BOARD GENERATED BY ONE METHOD BE SOLVED BY ANOTHER?\n')
    g3=sudokuGenerator()
    g3.GenerateDiag()
    print(g3.board+g3.cheat)
    print('ATTEMPTING TO SOLVE :')
    g3.GeneratorBackTracker(g3.board)
    print(g3.board)


    finT=time.time()-startT
    print(finT*1000.0,'ms')
    pass

if __name__=='__main__':
    main()