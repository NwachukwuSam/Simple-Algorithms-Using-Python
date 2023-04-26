row = int(input("Input the Number of rows: "))
columns = int(input("Input the Number of Columns: "))

print("                 MULTIPLICATION TABLE")
print("  |", end=" ")
for row in range(1, row+1):
    print(" ",row, end=" ")
print()
print("-------------------------------------------")

for row in range(1, columns+1):
    print(row, "|", end= '')
    for columns in range (1, columns+1):
        print(format(row * columns, "4d"), end='')
    print()