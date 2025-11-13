import copy

#Given a string, count total number of consonants in it (4 marks) . 
def find_constants(stringInput):
    newStringInput = stringInput.strip().lower()
    if len(newStringInput) == 0:
        return 0
    match newStringInput[0]:
        case "a"|"e"|"i"|"o"|"u":
            return 1 + find_constants(stringInput[1:])
    return find_constants(stringInput[1:])

#Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set (8 marks).
def char_and_int(stringInput, integerInput):
    if integerInput == 0:
        return 
    def _interRecur(prefix, integerInput):
        if integerInput == 0:
            print(prefix)
            return 
        for char in stringInput:
            _interRecur(prefix + char, integerInput - 1)
            
    _interRecur("", integerInput)

#Given a string s, find all possible ways to partition it such that every substring in the partition is a palindrome.
def string_Partition(inputString):
    if len(inputString) == 0:
        return 
    def _check(inputList, index):
        if len(inputList) -1  == index:
            return inputList
        if inputList[index] == inputList[-(index+1)]:
            return _check(inputList, index+1)
        else:
            return True
    inputList = inputString.split("") 
    
    for item in inputList:
        if _check(item, 1):
            pass
        else:
           pass  

#Given a string digits containing only digits (0-9) and an integer target, find all possible expressions that evaluate to the target value using the binary operators +, -, and *. If no such expression is possible, return an empty list (10 marks).
#skip 

listOfOperation = ["*", "+", "-", "C"]

def recurisonCal(listIn, operationQue, target):
    if len(listIn) == 0:
        print('before')
        print(operationQue)
        if eval(" ".join(operationQue)) == target:
            print(operationQue)
        return
            
    for i in listOfOperation:
        if i == "C":
            recurisonCal(listIn[1:], operationQue[:-2] + [f"{operationQue[-2]}{listIn[0]}"], target)
        elif len(listIn) == 1:
            recurisonCal(listIn[1:], operationQue + [str(listIn[0])], target)
        else:
            recurisonCal(listIn[1:], operationQue + [str(listIn[0])] + [i], target)
    return recurisonCal

# recurisonCal([1,2,9], [],7 )

#that was the first try, did not work out well

def recFunc(listIn, target):
    def _backtrack(index, exp):
        if index == len(listIn):
            if eval(exp) == target:
                print(exp)
        
            return
        digit = str(listIn[index])  
        
        if index == 0:
            _backtrack(index + 1, digit)
        else: 
            _backtrack(index + 1, exp + "+" + digit)
            _backtrack(index + 1, exp + "-" + digit)
            _backtrack(index + 1, exp + "*" + digit)
            _backtrack(index + 1, exp + digit) 
    _backtrack(0, "")
#Given an array of integers, print a sum triangle from it such that the first level has all array elements. From then, at each level number of elements is one less than the previous level and elements at the level is be the Sum of consecutive two elements in the previous level (8 marks). 

recFunc([1,2,4], 7)


listExample = [1,2,3,4,5]

def levels(listOut, index):
    arrayList = []
    if index == len(listOut):
        return listOut
    if index > len(listOut):
        return[]
    for i in range(len(listOut) - 1):
        arrayList.append(listOut[i] + listOut[i+1])
    listOut = arrayList
    return levels(listOut,  index)
    
# for index in range(1, len(listExample)+1):
#     newList = levels(listExample, index)
#     print(newList)
             
#You are given an array arr[] consisting of n elements. Your task is to generate and print all possible combinations of exactly r elements from this array.

# def N_Element(arr, r):
#     if len(arr) == 0:
#         return
#     suf = arr[0]
#     arr.pop(0)
#     integer = []
#     for i in range(1, ):
#         for i in arr:
#     return N_Element(arr, r)
# N_Element([1,2,3,4, 5,6], 4)

#I realized this way was very inefficent, I asked gpt to see how they would do it as it would be more concise and the way that I choose had limiations and I ran into issues that I do not think I could fix. A
def N_Element(arr, r, current ):
    if r == 0:
        print(current)
        return 
    if len(arr) == 0:
        # this means that you ran out of stuff in the list to pick from
        return
    
    N_Element(arr[1:], r - 1, current + [arr[0]])
    
    N_Element(arr[1:], r, current)
    
#N_Element([1,2,3,4,5,6], 3, [])