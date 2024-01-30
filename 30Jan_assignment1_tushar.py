import numpy as np

print("\nQ1\n")
arr = np.array([1, 2, 3, 6, 4, 5])
reversed_arr = arr[::-1]

print("Original array:", arr)
print("Reversed array:", reversed_arr)

print("\nQ2\n")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

# Compare arrays
if np.array_equal(arr1, arr2):
    print("Arrays arr1 and arr2 are equal.")
else:
    print("Arrays arr1 and arr2 are not equal.")
    
print("\nQ3\n")
arr = np.array([1,2,2,3,4,3,5,5,5])
print("Original array:")
print(arr)

print("Most frequent value in the above array:")
print(np.bincount(arr).argmax())

print("\nQ4\n")
arr = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')


total_sum = np.sum(arr)


row_sum = np.sum(arr, axis=1)

col_sum = np.sum(arr, axis=0)

print("Matrix:")
print(arr)

print("\ni. Sum of all elements:", total_sum)

print("\nii. Sum of all elements row-wise:")
print(row_sum)

print("\niii. Sum of all elements column-wise:")
print(col_sum)
