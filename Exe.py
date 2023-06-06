import numpy as np
M1 = np.array([[1,2,3],[4,5,6]])
M2 = np.array([[10,20,30],[40,50,60]])
arr = np.concatenate((M1,M2),axis=0)
print(f"{arr}")