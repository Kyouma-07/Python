import numpy as np

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12]])

print("Original 2D Array:")
print(array_2d)

row_1 = array_2d[0, :]   
col_2 = array_2d[:, 1]   
subarray = array_2d[1:, 1:3]  

print("\nSliced Rows and Columns:")
print("Row 1:", row_1)
print("Column 2:", col_2)
print("Subarray:")
print(subarray)

sum_axis_0 = np.sum(array_2d, axis=0)  
mean_axis_1 = np.mean(array_2d, axis=1)  
transpose_array = array_2d.T  

print("\nOther Operations:")
print("Sum along Axis 0:", sum_axis_0)
print("Mean along Axis 1:", mean_axis_1)
print("Transposed Array:")
print(transpose_array)