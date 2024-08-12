print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
A=np.array([[5,27,32],[14,53,62],[67,88,19]])
u,s,vt=np.linalg.svd(A)
a_hat=u@np.diag(s)@vt
print("Matrix A:")
print(A)
print("Singular values:")
print(s)
print("Reconstructed matrix :")
print(a_hat)