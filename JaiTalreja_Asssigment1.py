row_number = int(input("input number of rows: "))
col_number = int(input("input number of columns: "))
res= [[0 for col in range(col_number)] for row in range(row_number)]

for row in range(row_number):
    for col in range(col_number):
        res[row][col]= row*col

print(res)