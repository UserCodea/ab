import numpy as np

u = np.array([[4,3,-5],
              [0,-2.5,2.5],
              [0,0,12]])

l = np.array([[1,0,0],
              [-0.5,1,0],
              [2,-0.8,1]])


print("LU= ",np.dot(l,u))


