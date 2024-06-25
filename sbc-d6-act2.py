num_row = int(input("Enter the number of rows for the pattern: "))
num_column = int(input("Enter the number of rows for the pattern: "))

row = 1
while row <= num_row:
    if row == 1 or row == num_row:
        print('*' * num_row)
        column = 1
    elif column == 1 or column == num_column:
        print('*' + ' ' * (num_column - 2) + '*')
    else:
        ...
    row += 1

