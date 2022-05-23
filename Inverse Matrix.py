import numpy as np
from numpy.linalg import inv

m = np.array([[0,2,1,3],
              [3,2,8,1],
              [1,0,0,3],
              [0,3,2,1]])

print("Inverse",inv(m))
