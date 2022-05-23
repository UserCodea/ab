import matplotlib.pyplot as plt
import numpy as np

a = [[2,0],[0,1]]
x = [[1],[0]]
b = np.dot(a,x)

def plot_vector(x,y,xlim,ylim):
    plt.figure(figsize=(10,6))
    plt.quiver(0,0,x[0],x[1],color="r",angles="xy",scale_units="xy",scale=1,label="original")
    plt.quiver(0,0,b[0],b[1],color="g",angles="xy",scale_units="xy",scale=1,label="transformed")
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel("X")
    plt.ylabel("y")
    plt.show()


plot_vector(x,b,(0,3),(-0.5,0.5))