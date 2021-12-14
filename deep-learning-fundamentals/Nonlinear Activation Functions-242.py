## 2. ReLU Activation Function ##

import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(-2, 2, 20)


def relu(l):
    return [0 if x1<0 else x1 for x1 in l]


relu_y=relu(x)

print(x)
print(relu_y)

plt.plot(x,relu_y)

## 3. Trigonometric Functions ##

x = np.linspace(-2*np.pi, 2*np.pi, 100)

def relu(l):
    return [np.tan(x1) for x1 in l]


tan_y=relu(x)

print(x)
print(tan_y)

plt.plot(x,tan_y)

## 5. Hyperbolic Tangent Function ##

x = np.linspace(-40, 40, 100)


tanh_y=[np.tanh(l) for l in x]

print(x)
print(tanh_y)
plt.plot(x,tanh_y)