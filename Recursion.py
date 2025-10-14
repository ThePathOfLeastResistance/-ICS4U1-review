'''

    Given a string, count total number of consonants in it (4 marks) . 

    Given a set of characters and a positive integer k, print all possible strings of length k that can be formed from the given set (8 marks).

    Examples:

    Input: 
    set[] = {'a', 'b'}, k = 3

    Output:
    aaa
    aab
    aba
    abb
    baa
    bab
    bba
    bbb
aaa 0
aab 3
aba
abb
baa
bba
bab
bbb 

2
baa 1
abb
bba -1
bab -2
-5
bbb -4

    Given a string s, find all possible ways to partition it such that every substring in the partition is a palindrome.

    Examples: 

        Input: s = "geeks"
        Output: [[g, e, e, k, s], [g, ee, k, s]]
        Explanation: [g, e, e, k, s] and [g, ee, k, s] are the only partitions of "geeks" where each substring is a palindrome.

    Given a string digits containing only digits (0-9) and an integer target, find all possible expressions that evaluate to the target value using the binary operators +, -, and *. If no such expression is possible, return an empty list (10 marks).

        Input : digits = "124", target = 9
        Output : [“1+2*4”]
        Explanation: The valid expressions that evaluate to 9 are (1 + 2 * 4).

        Input : digits = “125”, target = 7
        Output : [“1*2+5”, “12-5”]
        Explanation: The two valid expressions that evaluate to 7 are (1 * 2 + 5) and (12 - 5). 

    Given an array of integers, print a sum triangle from it such that the first level has all array elements. From then, at each level number of elements is one less than the previous level and elements at the level is be the Sum of consecutive two elements in the previous level (8 marks).  Example :
     

    Input : A = {1, 2, 3, 4, 5}
    Output : [48]
             [20, 28] 
             [8, 12, 16] 
             [3, 5, 7, 9] 
             [1, 2, 3, 4, 5] 

    You are given an array arr[] consisting of n elements. Your task is to generate and print all possible combinations of exactly r elements from this array.
    Note: A combination is a selection of items where the order does not matter. Ensure that each unique group of r elements is printed only once, regardless of order (8 marks).

    Example:

        Input: arr = [1, 2, 3, 4], r = 2
        Output: 1 2
        1 3
        1 4
        2 3
        2 4
        3 4
'''

def find_constants(stringInput):
    newStringInput = stringInput.strip().lower()
    if len(newStringInput) == 0:
        return 0
    match newStringInput[0]:
        case "a"|"e"|"i"|"o"|"u":
            return 1 + find_constants(stringInput[1:])
    return find_constants(stringInput[1:])

# print(find_constants("aasdfesadfiouasdf"))

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

# char_and_int(['a', 'b'], 3)

def string_Partition(inputString):
    if len(inputString) == 0:
        return 
    def _check(inputList, index, listIndex):
        if len(inputList) -1  == index:
            return inputList
        if inputList[index] == inputList[-(index+1)]:
            return _check(inputList, index+1)
        else:
            return True
    inputList = inputString.split("") 
    
    for item in inputList:
        if _check("geag", 1):
            break
        else:
            
    
    

my_list = ['apple', 'banana', 'cherry', 'date']

# Combine 'banana' and 'cherry' into a single string
combined_element = my_list[1] + ' ' + my_list[2]

# Replace the original elements with the combined one
my_list[0:3] = [combined_element]

print(my_list)
# Output: ['apple', 'banana cherry', 'date']