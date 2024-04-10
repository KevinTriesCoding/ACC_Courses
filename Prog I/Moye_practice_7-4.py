ROWS = 3
COLUMNS = 4
sum = 0

two_dim_array = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

for r in range (ROWS):
    for c in range (COLUMNS):
        two_dim_array[r][c] = int(input("Please insert values for the list: "))

for r in range (ROWS):
    for c in range (COLUMNS):
        sum += two_dim_array[r][c]
        print (two_dim_array[r][c])

print (sum)
