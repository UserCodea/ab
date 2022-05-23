import numpy as np
import numpy.linalg
from scipy.linalg import lu


a = np.array([[8,3,-3],[-2,-8,5],[3,5,10]])


p , l , u = lu(a)

print(u)
print(np.dot(l,u))