
num_rows = int(input("Enter the number of rows for the pattern: "))


for i in range(num_rows, 1, -1):
    print("*" * i)

print("*" + " " * (num_rows-2) + "*")

for x in range(2, num_rows+1):
    print("*" * x)
print('BINI')