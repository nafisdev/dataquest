## 1. Introducing Model Selection ##

import pandas as pd

train=pd.read_csv('train_modified.csv')
holdout=pd.read_csv('holdout_modified.csv')

## 2. Training a Baseline Model ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

all_X = train.drop(['Survived','PassengerId'],axis=1)
all_y = train['Survived']

lr=LogisticRegression()
lr.fit(all_X,all_y)
scores=cross_val_score(lr,all_X,all_y,cv=10)

accuracy_lr=scores.mean()

## 3. Training a Model using K-Nearest Neighbors ##

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=1)
scores=cross_val_score(knn,all_X,all_y,cv=10)
accuracy_knn=scores.mean()

## 4. Exploring Different K Values ##

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

def plot_dict(dictionary):
    pd.Series(dictionary).plot.bar(figsize=(9,6),
                                   ylim=(0.78,0.83),rot=0)
    plt.show()

knn_scores = dict()


for k in range(1,50,2):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn_scores[k]=cross_val_score(knn,all_X,all_y,cv=10).mean()

    
    
plot_dict(knn_scores)

## 5. Automating Hyperparameter Optimization with Grid Search ##

from sklearn.model_selection import GridSearchCV

hyperparameters = {
    "n_neighbors": range(1,20,2),
    "weights": ["distance", "uniform"],
    "algorithm": ['brute'],
    "p": [1,2]
}

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

knn=KNeighborsClassifier(n_neighbors=1)
gnn=GridSearchCV(knn,hyperparameters,cv=10)

gnn.fit(all_X,all_y)
best_params=gnn.best_params_
best_score=gnn.best_score_

## 6. Submitting K-Nearest Neighbors Predictions to Kaggle ##

holdout_no_id = holdout.drop(['PassengerId'],axis=1)
best_knn = grid.best_estimator_

holdout_predictions=best_knn.predict(holdout_no_id)
submission=pd.DataFrame({'PassengerId':holdout['PassengerId'],'Survived':holdout_predictions})
                         
    
submission.to_csv('submission_1.csv')
                         

## 7. Introducing Random Forests ##

from sklearn.ensemble import RandomForestClassifier


rnn = RandomForestClassifier(random_state=1)
scores=cross_val_score(rnn,all_X,all_y,cv=10)
accuracy_rf=scores.mean()

## 8. Tuning our Random Forests Model with GridSearch ##

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

hyperparameters = {"criterion": ["entropy", "gini"],
                   "max_depth": [5, 10],
                   "max_features": ["log2", "sqrt"],
                   "min_samples_leaf": [1, 5],
                   "min_samples_split": [3, 5],
                   "n_estimators": [6, 9]
}
rnn = RandomForestClassifier(random_state=1)
# scores=cross_val_score(rnn,all_X,all_y,cv=10)
# accuracy_rf=scores.mean()


gnn=GridSearchCV(rnn,param_grid=hyperparameters,cv=10)

gnn.fit(all_X,all_y)
best_params=gnn.best_params_
best_score=gnn.best_score_

## 9. Submitting Random Forest Predictions to Kaggle ##

# The `GridSearchCV` object is stored in memory from
# the previous screen with the variable name `grid`

holdout_no_id = holdout.drop(['PassengerId'],axis=1)
best_rf = grid.best_estimator_

holdout_predictions=best_rf.predict(holdout_no_id)
submission=pd.DataFrame({'PassengerId':holdout['PassengerId'],'Survived':holdout_predictions})
                         
    
submission.to_csv('submission_2.csv',index=False)
                         