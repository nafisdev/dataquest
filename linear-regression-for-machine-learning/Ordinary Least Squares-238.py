## 1. Introduction ##

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X=train[features]
X['bias']=1

# X=X.insert(0,'bias',X.pop('bias'))
X = X[['bias']+features]
y=train['SalePrice']

# np.dot(np.transpose(matrix_23),i_2)
ols_estimation=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X),X)),np.transpose(X)),y)