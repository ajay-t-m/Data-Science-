print("SJC23MCA-2006 : AJAY T M")
print("Batch : MCA 2023-25")
import numpy as np
even=np.arange(2,31,2)
print("Original Array:",even)
slice=even[2:9:2]
print("Elements from index 2 to 8 with step 2:",slice)
last3=even[-3:]
print("Last 3 element of the array using negative index:",last3)
alternate=even[::2]
print("Alternate elements of the array:",alternate)
last3alt=alternate[-3:]
print("Last 3 alternate:",last3alt)
