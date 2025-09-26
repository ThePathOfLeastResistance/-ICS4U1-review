"""
Matrix Math Assignment
/30

Create a program that will do the following:

1. Have the user create two matrices (nested lists) with the dimensions of their choosing (you may randomnly create the values for each cell instead of having the user enter them)
- Note each matrix can have its own dimensions as dictated by the user

2. Prompt the user for whether they wish to add, subtract, or multiply their matrices

3. Determine if the chosen action (add, subtract, multiply) can be performed on the matrix and then perform it if possible

4. Print out the original two matrices (rows on different lines)
ie.
Matrix 1:
1 2 3
4 5 6
7 8 9
Matrix 2:
10 11 12
13 14 15
16 17 18

5. Print out the resulting matrix

Mark Breakdown:

2 Marks: Authoring Statement

2 Marks: Appropriate commenting throughout
1 Mark: Usability/User flow

5 Marks: Getting and creating the initial matrices based on user input 

8 Marks: Successfully determining if matrix addition or subtraction can be performed and performing it

12 Marks: Successfully determining if matrix multiplication can be performed and performing it

Matrix Addition/Subtraction Review:
https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:adding-and-subtracting-matrices/a/adding-and-subtracting-matrices

Matrix Multiplication Review:
https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/v/multiplying-a-matrix-by-a-matrix 

"""

# James Cao
# Sep 25, 2025
#Reviewing and learning about matrix operations

from random import randint


#creates a matrix of defined rows and columns with random values from 1-20
def create_matrix(rows, columns):
  matrix = []
  for i in range(0, rows):
    row = []
    for k in range(0, columns):
      row.append(randint(1, 20))
    matrix.append(row)
  return matrix


#did not see this functin so did not use it
def print_matrix(m):
  for i in range(0, len(m)):
    row = ""
    for k in range(0, len(m[0])):
      row += str(m[i][k]) + " "
    print(row)
  print("----------")


#checking if two matrices are the same size for adding and subtracting
def m_check_Symmetry(m1, m2):
  symmetry = True 
  if len(m1) == len(m2):
    for i in range(0, len(m1)):
      if len(m1[i]) != len(m2[i]):
        symmetry = False 
  else: 
    symmetry = False
  return symmetry

#check if the columns and rows match for the two given matrices so we can multiply them
def m_mult_check(m1, m2):
  factor = 0
  if len(m1[0]) == len(m2):
    factor = len(m1[0])
  return factor
  
#first check if the matrices are the same, then goes through each row and value to add them together
def m_addition(m1, m2):
  if m_check_Symmetry(m1, m2):
    m_sum = []
    for row in range(0, len(m1)):
      m_row = []
      for column in range(0, len(m1[row])):
        total = m1[row][column] + m2[row][column]
        print(f'here is the m_row: {m_row}')
        print(f'here is the total: {total}')
        m_row.append(total)
      m_sum.append(m_row)
  else:
    #if the sizes are different return 
    m_sum = "the two matrixs are not the same dimensions"
  return m_sum


#subtracting matrices
def m_subtraction(m1, m2):
  if m_check_Symmetry(m1, m2):
    m_result = []
    for row in range(0, len(m1)):
      m_row = []
      for column in range(0, len(m1[row])):
        total = m1[row][column] - m2[row][column]
        m_row.append(total)
      m_result.append(m_row)
  else:
    m_result = "error"

  return m_result


#takes the first matrix and multplies by a constant inputed by the user, the output is a matrix or a string stating the error 
def scalar_mult(m1):
  scalar = int(input("What do you want to multiply the Matrix by ?"))
  m_result = []
  for row in m1:
    new_row = []
    for column in row:
      new_row.append(column * scalar)
    m_result.append(new_row)
  return m_result


#use compatibility function, then does the matrix multiplcation, the result is rather a matrix or a string if there is an erorr
def m_mult(m1, m2):
  compatibility = m_mult_check(m1, m2)
  # print(compatibility)
  m_result = []
  if compatibility != 0:
    for row_m1 in m1:
      new_row = []
      
      for column_m2_value in range(0, len(m2[0])):
        sum = 0
        for value in range(0, compatibility):
          sum += row_m1[value] * m2[value][column_m2_value]
        new_row.append(sum)
      m_result.append(new_row)
  else:
    m_result = "the row and columns are not equal"
  return m_result

#checks what operation the user wants and matches it with the function
#match and case is basicly a if statement but less writing, thought to give it a try 
def check_operations(prompt, m1, m2):
  match prompt:
    case "add":
      return m_addition(m1, m2)
    case "subtract":
      return m_subtraction(m1,m2)
    case "scalar multiplication":
      return scalar_mult(m1)
    case "m":
    # case "maxtrix multiplication":
      return m_mult(m1, m2)

rows_m1 = int(input("Please enter in the rows of the first matrix: "))
columns_m1 = int(input("Please enter in the columns of the first matrix: "))

rows_m2 = int(input("Please enter in the rows of the first matrix: "))
columns_m2 = int(input("Please enter in the columns of the first matrix: "))



m1 = create_matrix(rows_m1, columns_m1)
m2 = create_matrix(rows_m2, columns_m2)

#ask the uswer for the input and gets ride of the space and captials for the if statements later 
m_operations = input("Input if you want to add, subtract, scalar multiplication, or maxtrix multiplication the matrices: ").strip().lower()

m_answer = check_operations(m_operations, m1, m2 )

#print all the martices here 
print("Here is the first martrix:")
for row in m1:
  print(row)

print("Here is the second martrix:")
for row in m2:
  print(row)

#if the operation could be done, the function will just return a martix which is just a list, this checks for that. 
if isinstance(m_answer, list):
  print(f'The result is: ')
  for row in m_answer:
    print(row)
else:
  print(f'There is an error, the reason is: {m_answer}')
  
#test test