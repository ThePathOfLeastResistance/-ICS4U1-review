# James Cao
# Sep 29, 2025
# The game of life simulation in Python 


#test tes ttes

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
        print(self.gridOfCells)
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
        # print("the NEW BOARD")
        # print(newBoard)
        self.gridOfCells = newBoard
        # print("the New grid of Cells")
        # print(self.gridOfCells)

    def NextGeneration(self, boardIndex):
        for rowIndex in range(0, len(self.gridOfCells)):
            for columnIndex in range(0, len(self.gridOfCells[0])):
                cell = Cell()
                # print("the current grid of cells")
                # print(self.gridOfCells)
                self.gridOfCells[rowIndex][columnIndex] = 1 if cell.CheckNeighbours(boardIndex, rowIndex, columnIndex) else 0
                # print("the NEW grid of cells")
                # print(self.gridOfCells)

                    
class Cell:
    def __init__(self):
        self.neighboursLayout = [[[],[],[]], [[],[],[]], [[],[],[]]]
    
    def CheckNeighbours(self, boardIndex, rowIndex, columnIndex):
        print("____________________") 
        neighbourCount = 0
        for yIndex in range(-1, 2):
            for xIndex in range(-1, 2):
                referenceYIndex = rowIndex + yIndex
                referenceXIndex = columnIndex + xIndex
               
                if 0 <= referenceXIndex < len(boardIndex[0]) and 0<= referenceYIndex < len(boardIndex) and not (yIndex == 0 and xIndex == 0):
                    print('pass NUmber ONe')
                    print("ReferenceYIndex")
                    print(referenceYIndex)
                    print("ReferenceXIndex")
                    print(referenceXIndex)
                    print(yIndex, xIndex)
                    print(rowIndex, columnIndex)
                    print(boardIndex)
                    if boardIndex[referenceYIndex][referenceXIndex] == 1:
                        print('added Neighbour')
                        neighbourCount += 1

        print("neighbourCOUnt")    
        print(neighbourCount)
        if boardIndex[rowIndex][columnIndex] == 1:
            if neighbourCount < 2:
                print("false 1")
                return False
            elif neighbourCount == 2 or neighbourCount == 3: 
                print("True 2") 
                return True
                
            elif neighbourCount > 3:
                print('False 3 ') 
                return False
            else:
                print("Somthing is not right!!")
        elif boardIndex[rowIndex][columnIndex] == 0:
            if neighbourCount == 3:
                print("true 4") 
                return True
            else:
                print("false 5") 
                return False
            
            
loopState = True
Grid = GridClass()
Grid.PopulateRandom()
generation = 0 

while loopState:
    generation += 1
    print(f'generation: {generation}')
    print("showing the display")
    Grid.Display()
    # print("find the nextgeneration")
    boardIndex = Grid.gridOfCells
    Grid.NextGeneration(boardIndex)
    # print("going to sleep")
    input("")
    # os.system('cls' if os.name == 'nt' else 'clear')
