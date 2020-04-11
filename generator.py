# encoding


''' this is generator file, this is used to create sudou filled grids
1. one approach could be a native filling algorithm, brute force implemented in randomFiller() fuction

'''


from sudokubase import sudoku
import random
import time


class sudokuGenerator(sudoku):
    def __init__(self):
        super().__init__()


    
    def fillNonDiag(self, row, col):
        ''' fill the non diagonal blocks using recursive backtrack BRUTE FORCE
        to generate the whole game'''
        # BASE CASES
        if (col > self.size-1) and (row < self.size-1):
            # RESET COL
            col = 0
            # GOTO NEXT ROW
            row = row+1

        if (col > self.size-1) and (row > self.size-1):
            # BOTH BOUNDS EXCEEDED, kill the recursion depth (MAX9)
            return True

        # if (col < self.size-1) and (row > self.size-1):
        #     return True

        # if (self.board[row, col] != 0):
        #     # ALREADY FILLED MOVE ONTO NEXT COL
        #     #   THIS FAILS for reasons unknown.
        #     col = col+1

        if (row < self.n):
            # IGNORE THE FIRST BLOCK and fill the other 2
            if (col < self.n):
                col = 3
        elif (row < self.size-3):
            # IN THE SECOND ZONE
            if (col == int(row/3)*3):  # 4th colmn onwards OR 2nd BELT, fill the third BLOC
                col = col + 3  # if COL=ROW=3, COLS=6,7,8 ;
        else:  # IF 3RD BELT
            if (col == self.size-3):  # INCREASE ROW AS SOON AS COLMN HITS 6
                row = row + 1
                col = 0  # goto first colmn
                if (row >= self.size):  # IF ROW INCREMENT HITS RETURN TUR SINCE FILLED
                    return True

        # THE MAIN DRIVER FOR RECURSION ;
        # THIS FILLS EACH NO AND RECURSES
        # IF SUCESSFULL NEXT COL POSITIOON FILLING WITH RECURSION
        # ELSE UNDO THE CHANGE
        for i in self.nos:
            if self.checkValid(i, row, col):
                self.board[row, col] = i
                # FILL THIS POSITION AND GO TO NEXT COLUMN
                if (self.fillNonDiag(row, col+1)):
                    return True
                # IF NOT FILLED RECURSIVELY, UNDO THE CHANGE
                self.board[row, col] = 0
        return False

 

    def GeneratorBackTracker(self, board):
        '''Backtracking algorithm to fill up board'''
        # initialize the location evertime recursion calls
        loc = [0, 0]

        if(not self.FindFirstEmpty(board, loc)):
            # then no place is empty get out of the recursion,boardFULL
            return True

        for num in range(1, self.size+1):
            # check all the numbers in the empty location
            if(self.checkValid(num, loc[0], loc[1])):
                self.board[loc[0], loc[1]] = num
                # put the number and proceed to solver the rest
                if(self.GeneratorBackTracker(board)):
                    return True  # sucessfully solved the lower boards, other locations

                # else
                self.board[loc[0], loc[1]] = 0
                # continue with other nos

        # still if it can't solve the board return false
        return False  # triggers the backtracking when its Not solved, cancel the board arrangement

    # def fillRandomBlock(self, rowbegin, colbegin):
    #     '''Fills the gameboard wth random algorithm
    #     here us begin inclusive and end exclusive=begin=self.n'''
    #     localList = sudoku.nos.copy()
    #     for i in range(rowbegin, rowbegin+sudoku.n):
    #         for j in range(colbegin, colbegin+sudoku.n):
    #             localList = sudoku.nos.copy()
    #             while(self.board[i, j] == 0):
    #                 if(len(localList) > 0):

    #                     choice = random.choice(localList)
    #                     if(self.checkValid(choice, i, j)):
    #                         self.board[i, j] = choice
    #                     localList.remove(choice)
    #             #  else:
    #             #      localList.remove(choice)
    #             #      #this uses linear search so slower

    # def fillRandomBLock(self, rowbegin, colbegin):
    #     pass

    def fillRandomNonDiag(self):
        '''creates tuples of nondiag blocs and fills them'''
        NonDiagBlocks = []
        cols = 0
        for rowbloc in [3*x for x in range(sudoku.n)]:
            # block rows
            while(cols < sudoku.size):
                if(cols != rowbloc):
                    NonDiagBlocks.append((rowbloc, cols))

                cols = cols+3
            cols = 0
        print(NonDiagBlocks)

#Generator Methods
    def GenerateDiag(self):
        self.fillDiag()
        self.fillNonDiag(0, self.n)
        self.RemoveRandom(self.size**2-20) #16 clues needed to make a proper

    def GenerateBacktrack(self):
        self.GeneratorBackTracker(self.board)

    

def main():
    # for testing generators
    startT=time.time()
    g = sudokuGenerator()
    g.GenerateDiag()
    finishT = time.time()-startT
    print(g.board)
    print('time for diag method: ' ,finishT*1000.0, 'ms')

    g2=sudokuGenerator() #by default inherits the previous
    startT2=time.time()
    g2.GeneratorBackTracker(g2.board)
    finishT2 = time.time()-startT2
    print(' time for recursiveBacktrack method : ' ,finishT*1000.0, 'ms')
    created=g2.board.copy()

    print(g2.board)
    print('\n Removing random elements and checking integrity of recursive method : \n')
    g2.RemoveRandom(75)
    print(g2.board)
    print("the cheat board :\n",g2.cheat)
    g2.GeneratorBackTracker(g2.board)#SOLVING IT
    print('solved board : \n' ,g2.board)
    print("IntegrityCheck :\n")
    print((created==g2.board).all())
    # passs


if __name__ == '__main__':
    main()
