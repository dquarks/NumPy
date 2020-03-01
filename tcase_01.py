import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([4,5,7,2,9])

#print(a*b) # You can multiple arrays or 1-dimensional matrices

block = np.array([[1,2,3,4,5], [6,7,8,9,10]]) # 2-dimensional array or matrix

#print(b * block) # Multiply a 1-dimensional matrix by a 2-dimensional matrix

cmat = block[:, 1:3] # Define a block matrix using columns 1 and 2
bmat = block[:, 2:4] # Define a block matrix using columns 2 and 3

res = cmat * bmat

print(res[1:2]) # Multiple block matrices

print(np.sqrt(res[1:2])) # Calculate square root of the second row
