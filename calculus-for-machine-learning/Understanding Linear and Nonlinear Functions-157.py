## 1. Why Learn Calculus? ##

import numpy as np
import matplotlib.pyplot as plt



x=np.linspace(0,3,100)

y=(-1*(x**2))+(3*x)-1

plt.plot(x,y)

## 4. Math Behind Slope ##

def slope(x1,x2,y1,y2):
    ## Finish the function here
    
    return ((y2-y1)/(x2-x1))
slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)

## 6. Secant Lines ##

import seaborn
seaborn.set(style='darkgrid')

def draw_secant(x_values):
    x = np.linspace(-20,30,100)
    y = -1*(x**2) + x*3 - 1
    plt.plot(x,y)
    # Add your code here.
    x1=x_values[0]
    x2=x_values[1]
    y1 = -1*(x1**2) + x1*3 - 1
    y2 = -1*(x2**2) + x2*3 - 1
    # xp=np.linspace(x1,x2,100)
    m=((y2-y1)/(x2-x1))
    c=y2-(m*x2)
    yp=(m*x)+c
    plt.plot(x,yp, color='green')
    
draw_secant([3,5])
# draw_secant([3,10])
# draw_secant([3,15])