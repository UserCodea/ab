import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


x = np.linspace(0,10,101)
y = 0.1*np.exp(0.3*x) +0.1*np.random.random(len(x))

def func(x,a,b):
    y = a*np.exp(b*x)
    return y

alpha , beta = optimize.curve_fit(func,xdata=x,ydata=y)[0]

plt.figure(figsize=(10,8))
plt.plot(x,y,"r")
yNew = alpha*np.exp(beta*x)
plt.plot(x,yNew,"b")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()