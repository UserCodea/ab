import numpy as np
from  numpy.linalg import qr

a = np.array([[0,2],
              [2,3]])

p = [1,5,10,20]

for i in range(20):
    q , r = qr(a)
    a = np.dot(r,q)

    if i+1 in p:
        print("Itiration:",i+1)
        print(a)

