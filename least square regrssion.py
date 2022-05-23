import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,101)
y = 1+x+x*np.random.random(len(x))

a = np.vstack([[x,np.ones(len(x))]]).T

y  = y[:,np.newaxis]



#alpha = np.dot(np.dot((np.linalg.inv(np.dot(a.T,a))),a.T),y)
#alpha = np.linalg.lstsq(a,y,rcond=None)[0]
pseudo = np.linalg.pinv(a)
alpha = pseudo.dot(y)
print(alpha)


plt.style.use("seaborn-poster")
plt.figure(figsize=(10,8))
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y,"b")
ynew = alpha[0]*x+alpha[1]
plt.plot(x,ynew,"r")
plt.show()

