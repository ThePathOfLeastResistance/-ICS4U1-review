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


def print_matrix(m):
  for i in range(0, len(m)):
    row = ""
    for k in range(0, len(m[0])):
      row += str(m[i][k]) + " "
    print(row)
  print("----------")


#adding two valid matrices together

def m_check_Symmetry(m1, m2):
  symmetry = True 
  if len(m1) == len(m2):
    for i in range(0, len(m1)):
      if len(m1[i]) != len(m2[i]):
        symmetry = False 
  else: 
    symmetry = False
  return symmetry
  

def m_addition(m1, m2):
  if m_check_Symmetry(m1, m2):
    m_sum = []
    for row in range(0, len(m1)):
      m_row = []
      for column in range(0, len(m1[row])):
        total = m1[row][column] + m2[row][column]
        m_row.append[total]
      m_sum.append[m_row]
  else:
    m_sum = "error"

  return m_sum


def m_subtraction(m1, m2):
  if m_check_Symmetry(m1, m2):
    m_result = []
    for row in range(0, len(m1)):
      m_row = []
      for column in range(0, len(m1[row])):
        total = m1[row][column] - m2[row][column]
        m_row.append[total]
      m_result.append[m_row]
  else:
    m_result = "error"

  return m_result


def scalar_mult(m1):
  return False


def m_mult(m1, m2):
  return False


rows_m1 = int(input("Please enter in the rows of the first matrix: "))
columns_m1 = int(input("Please enter in the columns of the first matrix: "))

rows_m2 = int(input("Please enter in the rows of the first matrix: "))
columns_m2 = int(input("Please enter in the columns of the first matrix: "))



m1 = create_matrix(rows_m1, columns_m1)
m2 = create_matrix(rows_m2, columns_m2)


m_sum = m_addition(m1, m2)
print_matrix(m_sum)
