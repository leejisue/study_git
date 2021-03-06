# 실습 : RandomizedSearch, GridSearch와 Pipeline를 엮음
import numpy as np
from sklearn.datasets import load_wine

from sklearn.preprocessing import MinMaxScaler, StandardScaler  
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline, make_pipeline

# from sklearn.svm import LinearSVC, SVC
# from sklearn.neighbors import KNeighborsClassifier  
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression 

import warnings
warnings.filterwarnings('ignore')
import pandas as pd 

# Data
wine = load_wine()
data = wine.data 
target = wine.target 
# print(data.shape, target.shape)

# preprocessing
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=44)
# Minmax등을 통해 Scale을 하지 않아도 됨

# Modeling
# pipline : 파라미터튜닝에 전처리까지 합침

# # [1] Pipeline
parameters=[
    {'model__n_estimators' : [100, 200, 300], 'model__max_depth' : [6, 8, 10, 12]},
    {'model__max_depth' : [6, 8, 10, 12], 'model__min_samples_leaf' : [3, 7, 10]},
    {'model__min_samples_split' : [2, 3, 5, 9], 'model__n_jobs' : [-1, 2, 4]}
]

# # [2] make_pipeline
# parameters=[
#     {'randomforestclassifier__n_estimators' : [100, 200], 'randomforestclassifier__max_depth' : [6, 8, 10, 12]},
#     {'randomforestclassifier__max_depth' : [6, 8, 10, 12], 'randomforestclassifier__min_samples_leaf' : [3, 7, 10]},
#     {'randomforestclassifier__min_samples_split' : [2, 3, 5, 9], 'randomforestclassifier__n_jobs' : [-1, 2, 4]}
# ]

scaler = [MinMaxScaler(), StandardScaler()]
search = [RandomizedSearchCV, GridSearchCV]

for scale in scaler :
    pipe = Pipeline([("scaler", scale), ('model', RandomForestClassifier())])
    # pipe = make_pipeline(scale, RandomForestClassifier())

    for CV in search :
        model = CV(pipe, parameters, cv=5)
        model.fit(x_train, y_train)
        results = model.score(x_test, y_test)
        print(str(scale),str(CV)+':'+str(results))

# MinMaxScaler() <class 'sklearn.model_selection._search.RandomizedSearchCV'>:0.9814814814814815
# MinMaxScaler() <class 'sklearn.model_selection._search.GridSearchCV'>:0.9814814814814815
# StandardScaler() <class 'sklearn.model_selection._search.RandomizedSearchCV'>:0.9629629629629629
# StandardScaler() <class 'sklearn.model_selection._search.GridSearchCV'>:0.9814814814814815