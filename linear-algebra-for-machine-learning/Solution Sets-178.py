## 2. Inconsistent Systems ##

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,20,1000)


y1=5/4 -2*x
y2=5/2-2*x



plt.plot(x,y1)
plt.plot(x,y2)

## 5. Homogenous Systems ##

def test_homog(x3):
    x1=4/3*x3
    x2=0
    
    mat = np.asarray([
    [x1],
    [x2],
    [x3]
    ])
    
    eq = np.asarray([
    [3,5,-4],
    [0,3,0],
    [0,0,0]
    ])
    ans= np.asarray([
    [0],
    [0],
    [0]
    ])
    arr=np.dot(eq,mat)
    print(arr)
    return np.array_equal(ans,arr)
    
    
b_one=test_homog(1)
b_two=test_homog(-10)
    