## 3. Bias-Variance Tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


def train_and_test(cols):
    model=LinearRegression()
    model.fit(filtered_cars[cols],filtered_cars['mpg'])
    pre=model.predict(filtered_cars[cols])
    mse=mean_squared_error(pre,filtered_cars['mpg'])
    variance=np.var(pre)
    
    
    return(mse,variance)
    
    
cyl_mse,cyl_var=train_and_test(['cylinders'])

weight_mse,weight_var=train_and_test(['weight'])

## 4. Multivariate Models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

one_mse, one_var = train_and_test(["cylinders"])
two_mse, two_var = train_and_test(['cylinders', 'displacement'])
three_mse, three_var = train_and_test(['cylinders', 'displacement', 'horsepower'])
four_mse, four_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight'])
five_mse, five_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'])
six_mse, six_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year'])
seven_mse, seven_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin'])

## 5. Cross Validation ##

from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import numpy as np
from statistics import mean
  
def avg(lst):
    return mean(lst)


def train_and_cross_val(cols):
    # Split into features & target.
    
    # np.random.seed(3)
    mses=[]
    variances=[]
    kf = KFold(n_splits=10,random_state=3,shuffle=True)
    for train, test in kf.split(filtered_cars):
        # print("%s %s" % (train, test))
        train=filtered_cars.iloc[train,:]
        test=filtered_cars.iloc[test,:]
        features = train[cols]
        target = train["mpg"]
        tfeatures = test[cols]
        ttarget = test["mpg"]
        # Fit model.
        lr = LinearRegression()
        lr.fit(features, target)
        # Make predictions on training set.
        predictions = lr.predict(tfeatures)
        # Compute MSE and Variance.
        mses.append(mean_squared_error(ttarget, predictions))
        variances.append(np.var(predictions))
    
    return(avg(mses), avg(variances))


one_mse, one_var = train_and_cross_val(["cylinders"])
two_mse, two_var = train_and_cross_val(['cylinders', 'displacement'])
three_mse, three_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower'])
four_mse, four_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight'])
five_mse, five_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration'])
six_mse, six_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year'])
seven_mse, seven_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin'])
    
    

## 6. Plotting Cross-Validation Error vs. Cross-Validation Variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

mse=[two_mse,three_mse,four_mse,five_mse,six_mse,seven_mse]
var=[two_var,three_var,four_var,five_var,six_var,seven_var]
no=[2,3,4,5,6,7]
plt.scatter(x=no,y=mse, color='red')
plt.scatter(x=no,y=var,color='blue')
plt.show()