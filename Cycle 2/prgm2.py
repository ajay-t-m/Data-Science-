print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
arr=np.array([[1+2j,2+9j,4+1j],[8+2j,7+3j,3+6j]],dtype=complex)
print("2D Array:")
print(arr)

row,col=arr.shape
print("\nNumber of rows:",row)
print("Number of columns:",col)

dim=arr.ndim
print("\nDimension of array is:",dim)

re_arr=arr.reshape(3,2)
print("\nReshaped array is")
print(re_arr)