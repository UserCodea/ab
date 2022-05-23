import numpy as np
import matplotlib.pyplot as plt



x = np.array([0,1,2,3,4,5,6,7,8])
y1 = np.array([0,0.8,0.9,0.1,-0.6,-0.8,-1,-0.9,-0.4])

for i in range(1,7):
    y2 = np.polyfit(x,y1,i)
    plt.subplot(2,3,i)
    plt.plot(x,y1,"r")
    plt.plot(x,np.polyval(y2,x))
    plt.title(f"poly order{i}")

plt.xlabel("X")
plt.ylabel("Y")
plt.show()