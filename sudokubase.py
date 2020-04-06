# encoding


''' This is the basic game representation containing the functions and the board representation
and rules for the game. Solver and generator algorithms are written in a seperate file

'''

import time
import numpy as np
import matplotlib.pyplot as mpl  # to visualize in jupyter notebooks
import random


class sudoku:
    # global common to all object variables
    n = 3
    size = n**2
    nos = [i for i in range(1, size+1)]
    

    # object variables
    def __init__(self):
        # while using these are objects' common variables so use self always(or even classname)
        self.board = np.zeros((self.size, self.size))
        self.cheat=self.board.copy()
        # self.rows = np.array([[i for i in range(1, self.size+1)]
        #                       for row in range(1, self.size+1)])
        self.rows = {}
        self.cols = {}
        # self.cols = np.array([[i for i in range(1, self.size+1)]
        #   for col in range(1, self.size+1)])

        # add a box array


# TODO : if using use, self.vairable for class\instance but for interior assignment you can directly use class variable

    def fillRandom(self, n=size):
        '''Fills the gameboard wth random algorithm'''

    def inBlock(self, val, row, col):
        '''gets the block given indices'''
        beginr = int(row / self.n) * self.n
        beginc = int(col / self.n) * self.n
        # slicing [being:end(exclu)]
        block = self.board[beginr:beginr+self.n, beginc:beginc+self.n]
        isthere = np.where(block == val)
        if block[isthere].size > 0:
            return True
        else:
            return False  # not in block

    def checkValid(self, toEnter, row, col):
        '''checks the square region [begin,end] and sees if numbers repeat in a completely
        LINEAR SEARCH ALGORITHM ; improvement'''
        self.Updater()
        if toEnter in self.rows[row]:
            return False
        elif toEnter in self.cols[col]:
            return False
        elif self.inBlock(toEnter, row, col):
            return False
        return True

    def fillBlock(self, begin, end):
        ''' fills a square region in the board of the given range [0,n-1]'''
        # makes a local copy of the avl nos
        localCopy = self.nos.copy()
        random.shuffle(localCopy)
        # print('begin=', begin, ' , end=', end)
        for i in range(begin, end):
            for j in range(begin, end):
                choice = localCopy.pop()
                self.board[i, j] = choice

    def fillDiag(self):
        ''' fills the diagonal boxes'''
        for i in range(self.n):
            k = i*self.n
            self.fillBlock(k, k+self.n)

    def fillNonDiag(self, row, col):
        ''' fill the non diagonal blocks using recursive backtrack BRUTE FORCE'''
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

    def Updater(self):
        # WORK NEEDED FOR DIFFERENCE ARRAYS
        '''run this to clear the row and col arrays for faster searching; returns none'''
        for i in range(0, self.size):
            # for elts in enumerate(self.board[i:]): #check rows
            rowelts = self.board[i, self.board[i, :].nonzero()]
            self.rows[i] = rowelts
            colelts = self.board[self.board[:, i].nonzero(), i]
            self.cols[i] = colelts

            # self.rows[i] = np.delete(self.nos, rowelts)
            # print('row=', i, colelts)

            # for elts in enumerate(self.board[:i]):  #check cols
            #     self.cols[i,:].remove(elts)
            #     print('cols=',i,self.cols[i])
        # print(self.rows)

    def RemoveRandom(self, toRemove):

        removal = random.sample(
            [i for i in range(0, self.size**2)], toRemove)
        for elt in removal:
            row = int(elt/self.size)
            col = elt % self.size
            self.cheat[row,col]=self.board[row,col]
            self.board[row, col] = 0

    def Generate(self):
        self.fillDiag()
        self.fillNonDiag(0,3)
        self.RemoveRandom(68)


def main():

    # just for testing
    s = sudoku()
    startT = time.time()
    # s.fillDiag()
    # s.Updater()
    # s.fillNonDiag(0, 3)
    # s.RemoveRandom(68)
    s.Generate()
    finishT = time.time()-startT
    print(s.inBlock(9, 4, 5))
    print(s.board)
    print(s.cheat)

    print(finishT*1000.0, 'ms')
    # pass


if __name__ == '__main__':
    main()
