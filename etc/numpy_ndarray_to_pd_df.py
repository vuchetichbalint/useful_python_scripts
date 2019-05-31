import pandas as pd
import numpy as np




a = np.ndarray(shape=(8,4), dtype=float)
b = np.ndarray(shape=(8,2), dtype=float)
#b = np.ndarray(shape=(2,2), dtype=float, order='F')
#c = np.hstack((a,b))
c = np.column_stack((a,b)) 

print(a)
print(b)
print(c)



