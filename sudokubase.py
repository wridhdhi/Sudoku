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
        self.cheat = self.board.copy()
        # self.rows = np.array([[i for i in range(1, self.size+1)]
        #                       for row in range(1, self.size+1)])
        self.rows = {}
        self.cols = {}
        # self.cols = np.array([[i for i in range(1, self.size+1)]
        #   for col in range(1, self.size+1)])

        # add a box array


# TODO : if using use, self.vairable for class\instance but for interior assignment you can directly use class variable
    def FindFirstEmpty(self, board, loc):
        for i in range(self.size):
            for j in range(self.size):
                if(board[i, j] == 0):
                    loc[0] = i
                    loc[1] = j
                    return True
        return False  # if no location found

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
        ''' fills a independent square region in the board of the given range [0,n-1]'''
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
            self.cheat[row, col] = self.board[row, col]
            self.board[row, col] = 0

    


def main():

    # just for testing
    s = sudoku()
    startT = time.time()
    # s.fillDiag()
    # s.Updater()
    # s.fillNonDiag(0, 3)
    # s.RemoveRandom(68)
    finishT = time.time()-startT
    print(s.inBlock(9, 4, 5))
    print(s.board)
    print(s.cheat)

    print(finishT*1000.0, 'ms')
    # pass


if __name__ == '__main__':
    main()
