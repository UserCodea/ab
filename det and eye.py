import numpy as np
from numpy.linalg import det

m = np.array([[0,2,1,3],
              [3,2,8,1],
              [1,0,0,3],
              [0,3,2,1]])

print("Determinant",det(m))
i = np.eye(4)
print(i)
print(np.dot(m,i))