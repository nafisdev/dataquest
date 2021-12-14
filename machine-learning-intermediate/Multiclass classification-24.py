## 1. Introduction to the Data ##

import pandas as pd
cars = pd.read_csv("auto.csv")


unique_regions=cars['origin'].unique()

print(unique_regions)

## 2. Dummy Variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years= pd.get_dummies(cars["year"], prefix="year")
cars = pd.concat([cars, dummy_years], axis=1)

cars=cars.drop(columns=['year','cylinders'])

print(cars.head())

## 3. Multiclass Classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]


train=shuffled_cars.iloc[:int(0.7*len(shuffled_cars.index)),:]

test=shuffled_cars.iloc[int(0.7*len(shuffled_cars.index)):,:]

## 4. Training a Multiclass Logistic Regression Model ##

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}

# def startswith():
#     return True
X=cars.columns[cars.columns.str.startswith("year") | cars.columns.str.startswith("cyl")]

for a in unique_origins:
    model = LogisticRegression()
    
    model.fit(cars[X], cars["origin"]==a)
    models[a]=model
    

## 5. Testing the Models ##

testing_probs = pd.DataFrame(columns=unique_origins)
X=cars.columns[cars.columns.str.startswith("year") | cars.columns.str.startswith("cyl")]

for a in unique_origins:
    testing_probs[a]=models[a].predict_proba(test[X])[:,1]
    

# for a in unique_origins:
#     model = LogisticRegression()
    
#     model.fit(cars[X], cars["origin"]==a)
#     models[a]=model

## 6. Choose the Origin ##

cars['predicted_origins']=testing_probs.idxmax(axis=1)

predicted_origins=testing_probs.idxmax(axis=1)
print(predicted_origins)