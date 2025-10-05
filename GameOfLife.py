# James Cao
# Sep 29, 2025
# The game of life simulation in Python 



import os
import random
import time 
import copy
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
        self.gridOfCells = newBoard

    def NextGeneration(self):
        boardIndex = copy.deepcopy(self.gridOfCells)
        # boardIndex = self.gridOfCells, does not amke a copy, but instead creates a new reference to it, so each tho it is out of the loop, when the checkneighbour function is ran, it will reference the the newly changed grid of cells
        for rowIndex in range(0, len(self.gridOfCells)):
            for columnIndex in range(0, len(self.gridOfCells[0])):
                cell = Cell()
                self.gridOfCells[rowIndex][columnIndex] = 1 if cell.CheckNeighbours(boardIndex, rowIndex, columnIndex) else 0

                    
class Cell:
    def __init__(self):
        self.neighboursLayout = [[[],[],[]], [[],[],[]], [[],[],[]]]
    
    def CheckNeighbours(self, boardIndex, rowIndex, columnIndex):
        neighbourCount = 0
        for yIndex in range(-1, 2):
            for xIndex in range(-1, 2):
                referenceYIndex = rowIndex + yIndex
                referenceXIndex = columnIndex + xIndex
               
                if 0 <= referenceXIndex < len(boardIndex[0]) and 0<= referenceYIndex < len(boardIndex) and not (yIndex == 0 and xIndex == 0):
                    if boardIndex[referenceYIndex][referenceXIndex] == 1:
                        neighbourCount += 1

        if boardIndex[rowIndex][columnIndex] == 1:
            if neighbourCount < 2:
                return False
            elif neighbourCount == 2 or neighbourCount == 3: 
                return True
                
            elif neighbourCount > 3:
                return False
            else:
                print("Somthing is not right!!")
        elif boardIndex[rowIndex][columnIndex] == 0:
            if neighbourCount == 3:
                return True
            else:
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
    Grid.NextGeneration()
    input("")
    # os.system('cls' if os.name == 'nt' else 'clear')
