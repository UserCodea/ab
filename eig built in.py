import numpy as np
from  numpy.linalg import eig

a = np.array([[0,2],
              [2,3]])


evalues , evectors = eig(a)

print("eignvalues",evalues)
print("eignvectors",evectors)