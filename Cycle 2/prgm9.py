print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
ar_1d=np.array([1,2,3,4,5])
diag_mat=np.diag(ar_1d)
print("1D array:")
print(ar_1d)
print("Diagonal matrix:")
print(diag_mat)
arr_2d_sq=np.array([[1,2,3],[4,5,6],[7,8,9]])
diag_ele=np.diag(arr_2d_sq)
print("2d array square:")
print(arr_2d_sq)
print("Diagonal element:")
print(diag_ele)
arr_2d_nonsq=np.array([[1,2,3],[4,5,6]])
diag_ele_nonsq=np.diag(arr_2d_nonsq)
print("2d array non square:")
print(arr_2d_nonsq)
print("Diagonal element non square:")
print(diag_ele_nonsq)