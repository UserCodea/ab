import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,101)
y = 0.1*np.exp(0.3*x) +0.1*np.random.random(len(x))

plt.style.use("seaborn-poster")
plt.figure(figsize=(10,8))
plt.plot(x,y,"b")
plt.xlabel("x")
plt.ylabel("y")
plt.show()