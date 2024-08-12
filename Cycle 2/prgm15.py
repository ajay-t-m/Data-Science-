print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
def is_sym(matrix):
    return (matrix==matrix.T).all()
def is_skewsym(matrix):
    return (matrix==-matrix.T).all()
matrix=np.array([[0,1,-2],[-1,0,3],[2,-3,0]])
if is_sym(matrix):
    print("Matrix is symmetric")
elif is_skewsym(matrix):
    print("Matrix is skew symmetric")
else:
    print("Matrix is neither symmetric nor skew symmetric")