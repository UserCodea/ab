import numpy as np
from  numpy.linalg import qr

a = np.array([[0,2],
              [2,3]])

q , r = qr(a)

print(q)
print(r)

b = np.dot(q,r)
print("qr:",b)