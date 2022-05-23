import numpy as np

def normalize(x):
    max = abs(x).max()
    xNew =  x/x.max()
    return max,xNew


x = np.array([1,1])
a = np.array([[0,2],[2,3]])

for i in range(8):
    x = np.dot(a,x)
    y ,x = normalize(x)

print("eignvalues: ",y)
print("eignvector: ",x)

