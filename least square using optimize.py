import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(0,1,101)
y = 1+x+x*np.random.random(len(x))

def func(x,a,b):
    y = a*x+b
    return y

alpha = optimize.curve_fit(func,xdata=x,ydata=y)[0]


plt.style.use("seaborn-poster")
plt.figure(figsize=(10,8))
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"b")
ynew = alpha[0]*x+alpha[1]
plt.plot(x,ynew,"r")
plt.show()

