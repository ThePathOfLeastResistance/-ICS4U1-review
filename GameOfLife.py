# James Cao
# Sep 29, 2025
# The game of life simulation in Python 

import os
import random
import time 
# # Functions are here
# def print_board(board, columnValue):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     listOfLifePrints = []
#     itemCounter = 0
#     for row in board:
#         for lifeState in row: 
#             itemCounter += 1
#             # print(itemCounter)
#             # print(itemCounter % 3 == 0)
#             if lifeState == 1:
#                 listOfLifePrints.append(["000", "000"] )
#             else:
#                 listOfLifePrints.append(["[ ]", "[ ]"] )
#         #the * sign unpacks the zip
#         # for the list of list, it unpacks the inner list as seperate arguments
#     newList = ["   ".join(rowOfText) for rowOfText in zip(*listOfLifePrints)]
#     newZipList = list(zip(*listOfLifePrints))
#     print("\n")
#     for indexValue in range(0, int(len(listOfLifePrints)/columnValue)):
#         print(*newZipList[0][indexValue * columnValue : (indexValue + 1)*columnValue])
#         print(*newZipList[1][indexValue * columnValue : (indexValue + 1)*columnValue])        
#         print('\n')
#     print(board)

class GridClass:
    def __init__(self):
        self.gridOfCells = [[], [],[]]
        
    # Functions are here
    def Display(self):
        board = self.gridOfCells
        # os.system('cls' if os.name == 'nt' else 'clear')
        listOfLifePrints = []
        columnValue = len(board[0])
        for row in board:
            for lifeState in row: 
                listOfLifePrints.append("0000" if lifeState == 1 else "[  ]")

        for indexValue in range(0, int(len(listOfLifePrints)/columnValue)):
            print("  ".join(listOfLifePrints[indexValue * columnValue : (indexValue + 1)*columnValue]))
            print("  ".join(listOfLifePrints[indexValue * columnValue : (indexValue + 1)*columnValue]))
            dashboardDiv = ''
            n = int(len(listOfLifePrints)/columnValue)
            dashboardDiv += "----" * (n) + "--" * (n - 1) 
            print(dashboardDiv)
            
        
    def PopulateRandom(self):
        userRowValue = int(input("Enter a number for the number of rows for the game of life: "))
        userColumnValue = int(input("Enter a number for the number of column for the game of life: "))
        newBoard = []
        for row in range(0, userRowValue):
            newColumn = []
            for column in range(0, userColumnValue):
                newColumn.append(random.randint(0,1))
            newBoard.append(newColumn)
        print("the NEW BOARD")
        print(newBoard)
        self.gridOfCells = newBoard
        print("the New grid of Cells")
        print(self.gridOfCells)

    def NextGeneration(self):
        for rowIndex in range(0, len(self.gridOfCells)):
            for columnIndex in range(0, len(self.gridOfCells[0])):
                cell = Cell()
                print("the current grid of cells")
                print(self.gridOfCells)
                self.gridOfCells[rowIndex][columnIndex] = 1 if cell.CheckNeighbours(self.gridOfCells) else 0
                print("the NEW grid of cells")
                print(self.gridOfCells)

                    
class Cell:
    def __init__(self):
        self.neighboursLayout = [[], [], []]
        self.neighborCount = 0
    
    def FetchNeighbours(self, rowIndex, columnIndex):
        yIndex = -1 
        for i in range(yIndex, 1):
            xIndex = -1
            for i in range(xIndex, 1):
                referenceYIndex = rowIndex + yIndex
                referenceXIndex = columnIndex + xIndex
                self.neighboursLayout[yIndex+1].append([referenceXIndex, referenceYIndex] if referenceXIndex >= 0 and referenceYIndex >= 0 else [])
        # return self.neighboursLayout
    
    def CheckNeighbours(self, board):
        self.FetchNeighbours
        neighbourCount = 0
        for rowOfIndex in self.neighboursLayout:
            for columnOfIndex in rowOfIndex:
                if columnOfIndex == [] or (rowOfIndex == 1 and columnOfIndex == 1):
                    pass
                else:
                    if board[rowOfIndex][columnOfIndex] == 1:
                        neighbourCount += 1
        if board[1][1] == 1:
            if neighbourCount < 2:
                return False
            elif neighbourCount == 2 or neighbourCount == 3: 
                return True
            elif neighbourCount > 3:
                return True
            else:
                print("Somthing is not right!!")
        elif board[1][1] == 0:
            if neighbourCount == 3:
                return True
            else: 
                return False
            
            
loopState = True
gridOfCells = GridClass()
gridOfCells.PopulateRandom()

while loopState:
    print("showing the display")
    gridOfCells.Display()
    print("find the nextgeneration")
    gridOfCells.NextGeneration()
    print("going to sleep")
    time.sleep(1)
    # os.system('cls' if os.name == 'nt' else 'clear')
