print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
arr2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Original 2D array:\n",arr2d)
exlrow=arr2d[1:]
print("Element excluding the first row:\n",exlrow)
exlcol=arr2d[:,:-1]
print("Element excluding the last column:\n",exlcol)
colinrow=arr2d[1:3,0:2]
print("Elements of the 1st and 2nd column in the 2nd and 3rd row:\n",colinrow)
col23=arr2d[0,1:3]
print("2nd and 3rd element of the 1st row:\n",col23)
descending=arr2d.ravel()[::-1][4:11]
print("Descending order:",descending)