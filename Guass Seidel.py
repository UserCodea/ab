import numpy as np

a = np.array([[8,3,-3],[-2,-8,5],[3,5,10]])

diag = np.diag(np.abs(a))

off_diag = np.sum(np.abs(a),axis=1)-diag

if np.all(diag > off_diag):
    print("Matrix is Diagonally dominant")
else:
    print("Not Diagonally")

x1=0
x2=0
x3=0

epsilom = 0.01
converged = False

xOld = np.array([x1,x2,x3])

print("Itiration Result")
print("k , x1 , x2 , x3")

for k in range(1,50):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/(-8)
    x3 = (-8-3*x1-5*x2)/10

    x= np.array([x1,x2,x3])
    dx = np.sqrt(np.dot(x-xOld,x-xOld))

    print(k,"\t",x1,"\t",x2,"\t",x3,"\t")
    if dx<epsilom:
        converged = True
        print("Converged")
        break

    xOld = x

if not converged:
    print("Not Converged")