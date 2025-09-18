''''
Author: James Cao
Date Modified: Sep 16, 2025
Description: The code for an assignment in a cs class 
'''




''''
Create a small console game where the program will choose a random number and the player must try and guess the number (10 marks)
        If the guess is too low, tell the user to guess higher and vice versa
        Have the round continue until the user guesses the correct number
        Once the round has ended ask the user if they want to play again
        Exit the game if they choose not to play again
    '''




''' 
import random

gamEnd = False
while gamEnd == False:
    ranNum = random.randint(1, 10)
    # print(f"backend - number is {ranNum}")
    rigAnw = False
    while rigAnw == False:
        useGus = int(input("Guess the number, its 1 - 10: "))
        if useGus == ranNum:
            newsta = input("YOU GUESSED THE RIGHT NUMBER, do you want to contine playing? Say 'Yes' to continue, and 'No' to stop: ")
            rigAnw = True
            if newsta == "No":
                gamEnd = True
            else:
                continue
        if useGus > ranNum:
            print("Your guess is too big, choose smaller ")
        elif useGus < ranNum:
            print("Your guess is too small, choose bigger ")
'''


'''
    Create a console version of the game hangman (split the string into a list of characters) (20 marks)
'''


hanlis= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+

  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

'''
import os
print("hello")
os.system('cls' if os.name=='nt' else 'clear')


def checkForMis(list):
    misCou = 0
    for i in list:
        if i == "_":
             misCou += 1
    if misCou == 0:
        return True
    else:
        return False
        
gamEnd = False
while gamEnd == False:
    wordAns = input("Eneter the word you want the other person to guess: ")
    os.system('cls' if os.name=='nt' else 'clear')
    worLis = list(wordAns)
    print(worLis)
    print("switch people")
    rigAnw = False
    hanNum = 0
    corLis = []
    for i in worLis:
        corLis.append("_")
    guslis = []
    
    while rigAnw == False:
        useGus = input("Guess the letter: ").strip().lower()
        length = len(worLis)
        corGus = []
        guealr = False
        for i in range(len(guslis)):
            if guslis[i] == useGus:
                print("You already guessed this number before!!:  ")
                guealr = True
            
        if guealr == False:
            for i in range(length):
                if worLis[i] == useGus:
                    corLis[i] = useGus
                    corGus.append(useGus)
                
            if len(corGus) != 0:
                print(hanlis[hanNum])
                print("You guessed it!!")
                print(corLis)
            else:
                hanNum += 1
                print(hanlis[hanNum])
                print("You got it wrong!!")
                print(corLis)
            
            if checkForMis(corLis):
                    rigAnw = True
                    os.system('cls' if os.name=='nt' else 'clear')
                    print("You WON !!!")  
            guslis.append(useGus)
'''

'''
    Create  a trivia game (2 players) that reads the questions and categories in from the file provided in the assignment (40 marks). Your game should:
        Ask the players their username (stored as a variable)
        Ask them how many categories they wish to choose from
        Ask them how many questions they wish to have asked
        Display the categories (these should be randomly selected)
        Randomly select a category and randomly select 2 questions from the category. Each player has a chance to answer one. Keep track of each question you have asked so you don't have any duplicates
        Keep track of their scores (display at the start of each round)
        End the game and display the winner
        Ask them if they wish to play again

'''

import pandas as pd

while gameOn == True:
    

df = pd.read_csv('quiz_questions.csv')
a = df['category'].unique()
print(sorted(a))

