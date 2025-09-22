rows = int(input("enter the number of rows: "))
columns = int(input('enter the number of columns: '))

table = []

#get them to created the table 
for i in range(0, rows):
    rowValue = []
    for k in range(0, columns):
        rowValue.append(int(input("Enter the number")))
    table.append(rowValue)
    
#Create a user defined 2D list and sum a row of their choice

rowRequest = int(input("Which Row do you want the sum of?: "))
sum = 0 

#debug section here 
print(table)
print(table[rowRequest-1])

for i in table[rowRequest-1]:
    sum += i
print(f'The sum of all the values in that row is {sum}')