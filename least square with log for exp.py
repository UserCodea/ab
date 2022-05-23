import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,101)
y = 0.1*np.exp(0.3*x) +0.1*np.random.random(len(x))

a = np.vstack([x,np.ones(len(x))]).T

beta , logAlpha = np.linalg.lstsq(a,np.log(y),rcond=None)[0]

alpha = np.exp(logAlpha)

plt.style.use("seaborn-poster")
plt.figure(figsize=(10,8)) 
yNew = alpha * np.exp(beta*x)
plt.plot(x,y,"r")
plt.plot(x,yNew,"b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()