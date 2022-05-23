import numpy as np
from numpy.linalg import cond

a = np.array([[1,1,0],
              [0,1,0],
              [1,0,1]
              ])

print("Inverse",cond(a))
