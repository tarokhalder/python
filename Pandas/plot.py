import matplotlib.pyplot as plt
import numpy as np

#show simple plot

xpoints = list(map(int , input().split()))
ypoints = list(map(int , input().split()))

if len(xpoints) != len(ypoints):
    print("You have to give same length")
else:  
    plt.xlabel("xpoints")
    plt.ylabel("ypoints")
    plt.plot(xpoints, ypoints , marker = 'o')
    plt.grid()
    plt.show()
