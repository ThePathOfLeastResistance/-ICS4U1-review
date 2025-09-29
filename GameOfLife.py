# James Cao
# Sep 29, 2025
# The game of life simulation in Python 

import os
import random



# Functions are here
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        listOfLifePrints = []
        for lifeState in row: 
            if lifeState == 1:
                listOfLifePrints.append(["000", "000", "000"])
            else:
                listOfLifePrints.append(["   ", "   ", "   "])
        print("\n".join(" ".join(rowOfText) for rowOfText in zip(listOfLifePrints)))
        #this is a really cool way of printing in a 3 by 3 

def populate_board(rowValue, columnValue):
    newBoard = []
    for row in range(0, rowValue):
        newColumn = []
        for column in range(0, columnValue):
            newColumn.append(random.randint(0,1))
        newBoard.append(newColumn)
    return newBoard

userRowValue = int(input("Enter a number for the number of rows for the game of life: "))
userColumnValue = int(input("Enter a number for the number of column for the game of life: "))

boardLayout = populate_board(userRowValue, userColumnValue)
print(boardLayout)
print_board(boardLayout)