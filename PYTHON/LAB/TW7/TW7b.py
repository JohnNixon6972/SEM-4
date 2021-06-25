# Write a NumPy program to convert a list of numeric values into a onedimensional NumPy array and then reverse it. Also search for a specific 
# element; if found display all its positions in the reversed array; else an error 
# message

import numpy as np

rows = int(input("Enter the number of rows :: "))
columns = int(input("Enter the number of columns :: "))

list = []
print("Enter the elements one by one :: ")
for _ in range(rows):
    col = []
    for _ in range(columns):
        col.append(int(input()))
    list.append(col)

print("Original array :: ")
for rows in list:
    print(*rows)

arr = np.array(list)

flattened_arr = arr.flatten()
print("Flattened Array :: ")
print(*flattened_arr)

rev_arr = np.flip(flattened_arr) 
print("Reversed Array :: ")
print(*rev_arr)

key = int(input("Enter the number to be searched :: "))
indexes = np.where(rev_arr == key)

if indexes[0].size == 0:
    print("Number not present!!")
else:
    print("Number ",key," is present at indexes :: ",*indexes[0])