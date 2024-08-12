print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
size=3
matrix=np.random.randint(10,20,size=(size,size))
print("Original matrix:")
print(matrix)
if np.linalg.matrix_rank(matrix)==size:
    inverse=np.linalg.inv(matrix)
    print("Inverse matrix:")
    print(inverse)
else:
    print("The matrix is not invertible")
rank=np.linalg.matrix_rank(matrix)
print("Rank of Matrix:\n",rank)
deter=np.linalg.det(matrix)
print("Determinant of Matrix:\n",deter)
matrix_1d=matrix.flatten()
print("Matrix as 1d array:\n",matrix_1d)
eigenval,eigenvec=np.linalg.eig(matrix)
print("Eigen values:")
print(eigenval)
print("Eigen vector:")
print(eigenvec)