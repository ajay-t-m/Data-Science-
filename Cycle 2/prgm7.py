print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
m2=np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Matrix 1:\n",m1)
print("Matrix 2:\n",m2)
mat_sum=m1+m2
print("Matrix sum:\n",mat_sum)
mat_diff=m1-m2
print("Matrix Difference:\n",mat_diff)
mat_prod=m1*m2
print("Matrix Element wise product:\n",mat_prod)
mat_div=m1/m2
print("Matrix Divison:\n",mat_div)
mat_mul=np.dot(m1,m2)
print("Matrix multiplication:\n",mat_mul)
mat_trans=np.transpose(m1)
print("Matrix 1 transpose:\n",mat_trans)