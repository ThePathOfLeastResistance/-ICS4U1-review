rows = int(input("enter the number of rows: "))
columns = int(input('enter the number of columns: '))

table = []

#get them to created the table 
for i in range(0, rows):
    rowValue = []
    for k in range(0, columns):
        rowValue.append(int(input("Enter the number")))
    table.append(rowValue)
    
