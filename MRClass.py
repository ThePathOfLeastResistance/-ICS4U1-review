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
import random    
import os 

gameOn = True

#issues: since the program does not know how many number is in each catergory, the user can choose only 1 category that only has 5 questions, and want to be asked 20 questions.

def makeQuestionList(df, numOfQuesions, categories):
    #this is not super efficint since it quries the df every time instead of just once.
    # print('here is the catergory')
    # print(categories)
    # print(numOfQuesions)
    listOfQuestions = df[df['category'] == categories]
    # print(listOfQuestions)

    return listOfQuestions.sample(numOfQuesions)

while gameOn == True:
    player1UserName = input("Input the user name for the first player: ")
    player1Score = 0
    player2UserName = input("Input the user name for the second player: ")
    player2Score = 0
    
    df = pd.read_csv('quiz_questions.csv')
    listOfCategories = df['category'].unique()
    
    # print(df.head())
    # print(listOfCategories)
    lengthOfCategories = len(listOfCategories)
    numOfCategories = int(input(f'How many categories do you want to choose from (1 - {lengthOfCategories}): '))
    numOfQuesions = int(input("Ask them how many questions they wish to have asked: ")) * 2
    sampleCategories = random.sample(range(0, lengthOfCategories), numOfCategories)
    os.system('cls' if os.name == 'nt' else 'clear')

    chosenCategories = []
    
    print("Here are your Chocies: ")
    for i in sampleCategories:
        oneCategroy = listOfCategories[i]
        print(oneCategroy)
        chosenCategories.append(oneCategroy)
    
    # print(listOfQuestions)
    input("\n Enter To Continue")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    randomCategory = random.randint(0, numOfCategories)
    questionList = makeQuestionList(df, numOfQuesions, chosenCategories[randomCategory-1])
    for i in range(0, numOfQuesions, 2):
    
        print(f'{player1UserName} Score: {player1Score}')
        print(f'{player2UserName} Score: {player2Score}')
        print("\n\n-------------")
        questionOne = questionList.iloc[i]
        print(f'{player1UserName}')
        print(f'Question: {questionOne["question"]}')
        print(f'Category: {questionOne["category"]}')
        print(f'Difficulty: {questionOne["difficulty"]}')
        
        answerToOne = input("Enter your Guess, True or False?: ").strip().lower()

        if answerToOne == str(questionOne["correct_answer"]).strip().lower():
            player1Score += 1 
            print("You got it right!!!")
        else:
            print("You got it wrong")
        
        input('Presss Enter to Continue')
        os.system("cls" if os.name == 'nt' else 'clear')
        
        print(f'{player1UserName} Score: {player1Score}')
        print(f'{player2UserName} Score: {player2Score}')
        print("\n\n-------------")
        questionTwo = questionList.iloc[i + 1]
        print(f'{player2UserName}')
        print(f'Question: {questionTwo["question"]}')
        print(f'Category: {questionTwo["category"]}')
        print(f'Difficulty: {questionTwo["difficulty"]}')
        
        answerToTwo = input("Enter your Guess, True or False?: ").strip().lower()

        if answerToTwo == str(questionTwo["correct_answer"]).strip().lower():
            player2Score += 1 
            print("You got it right!!!")
        else:
            print("You got it wrong")
            
        input('Presss Enter to Continue')
        os.system("cls" if os.name == 'nt' else 'clear')
    
    if player1Score > player2Score:
        print(F'{player1UserName} Won!!!')
    if player1Score < player2Score:
        print(F'{player2UserName} Won!!!')
    else:
        print(f'It was a TIE!!!')
    
    gameOn = True if input("Want to continue playing (Yes or NO): ").strip().lower() == 'yes' else False


