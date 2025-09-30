# James Cao
# Sep 29, 2025
# The game of life simulation in Python 

import os
import random



# Functions are here
def print_board(board, columnValue):
    os.system('cls' if os.name == 'nt' else 'clear')
    listOfLifePrints = []
    itemCounter = 0
    for row in board:
        for lifeState in row: 
            itemCounter += 1
            # print(itemCounter)
            # print(itemCounter % 3 == 0)
            if lifeState == 1:
                listOfLifePrints.append(["000", "000"] )
            else:
                listOfLifePrints.append(["xxx", "xxx"] )
        #the * sign unpacks the zip
        # for the list of list, it unpacks the inner list as seperate arguments
    newList = ["   ".join(rowOfText) for rowOfText in zip(*listOfLifePrints)]
    newZipList = list(zip(*listOfLifePrints))
    print("\n")
    for indexValue in range(0, int(len(listOfLifePrints)/columnValue)):
        print(*newZipList[0][indexValue * columnValue : (indexValue + 1)*columnValue])
        print(*newZipList[0][indexValue * columnValue : (indexValue + 1)*columnValue])
        print ("\n")
        
    
    print(board)
    
    
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
print_board(boardLayout, userColumnValue)