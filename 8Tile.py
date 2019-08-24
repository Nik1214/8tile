from random import randint
import copy
from copy import deepcopy
class node(object):
    def __init__(self,b,p,d,a):
        self.board = b
        self.parent = p
        self.depth = d
        self.action = a
        self.goalBoard = [["1","2","3"],["4","5","6"],["7","8","_"]]
        self.count = 0
        self.r = 0
        self.c = 0
        self.numlist = ["1","2","3","4","5","6","7","8","_"]
        for i in range(3):
            for j in range(3):
                self.goalBoard[i][j] = self.numlist.pop(self.count)
                
    def getBoard(self):
        return self.board
    
    def display(self):
        print(self.board)
    
    def checkGoal(self):
        if self.board == self.goalBoard:
            return True
        else:
            return False

    def moveUp(self):
        temp = copy.deepcopy(self)
        self.r = 0
        self.c = 0
        for i in range(3):
            for j in range(3):
                if temp.board[i][j] == "_":
                    self.r = i
                    self.c = j
        if(self.r-1 >= 0):
            temporary = temp.board[self.r][self.c]
            temp.board[self.r][self.c] = temp.board[self.r-1][self.c]
            temp.board[self.r-1][self.c] = temporary
        if(self.parentCheck(temp) == False):
            return
        if(temp.board != self.board):
            self.successors.append(node(temp.board,self,self.depth + 1, "u"))
        return True
    def moveDown(self):
        self.r = 0
        self.c = 0
        temp = copy.deepcopy(self)
        for i in range(3):
            for j in range(3):
                if (temp.board[i][j] == "_"):
                    self.r = i
                    self.c = j
        if(self.r+1 < len(self.board)):
            temporary = temp.board[self.r][self.c]
            temp.board[self.r][self.c] = temp.board[self.r+1][self.c]
            temp.board[self.r+1][self.c] = temporary
        if(self.parentCheck(temp) == False):
            return
        if(temp.board != self.board):
            self.successors.append(node(temp.board,self,self.depth + 1, "d"))
        return True
    
    def moveLeft(self):
        self.r = 0
        self.c = 0
        temp = copy.deepcopy(self)
        for i in range(3):
            for j in range(3):
                if (temp.board[i][j] == "_"):
                    self.r = i
                    self.c = j
        if(self.c-1 >= 0):
            temporary = temp.board[self.r][self.c]
            temp.board[self.r][self.c] = temp.board[self.r][self.c-1]
            temp.board[self.r][self.c-1] = temporary
        if(self.parentCheck(temp) == False):
            return
        if(temp.board != self.board):
            self.successors.append(node(temp.board,self,self.depth + 1, "l"))
        return True
    def moveRight(self):
        self.r = 0
        self.c = 0
        temp = copy.deepcopy(self)
        i=0
        j=0
        for i in range(3):
            for j in range(3):
                if (temp.board[i][j] == "_"):
                    self.r = i
                    self.c = j
        if(self.c+1 < len(self.board)):
            temporary = temp.board[self.r][self.c]
            temp.board[self.r][self.c] = temp.board[self.r][self.c+1]
            temp.board[self.r][self.c+1] = temporary
        if(self.parentCheck(temp) == False):
            return
        if(temp.board != self.board):
            self.successors.append(node(temp.board,self,self.depth + 1, "r"))
        return True
        
    def parentCheck(self,checked):
        
        temp = self
        if(temp.board == checked.board):
            return False
        while (temp.parent != None): # and (self.temp.board != None)
            temp = temp.parent
            if(temp.board == checked.board):
                return False
        return True
    
        
    def expand(self):
        self.successors = []
        self.moveDown()
        self.moveUp()
        self.moveLeft()
        self.moveRight()
       # for x in range(len(self.successors)):
 #           self.successors[x].display()
        return self.successors

def serch():
    input1= [["1","2","3"],["4","5","6"],["7","_","8"]]
    fringe = []
    add = node(input1,None,0,None)
    fringe.append(add)
    while(len(fringe) != 0):
        temp = fringe.pop(0)
        temp.display()
        if(temp.checkGoal()):
            print("done")
            print(temp.board)
            return
        else:
            succProxy = temp.expand()
            nodeCanBeAdded = True
            x = 0
            y = 0
            for(x) in range(len(succProxy)):
                succObj = succProxy.pop(0)
                for(y) in range(len(fringe)):
                    if(fringe[y] == succObj):
                        nodeCanBeAdded = False
                if(nodeCanBeAdded == True):
                    fringe.insert(0,succObj)
serch()
