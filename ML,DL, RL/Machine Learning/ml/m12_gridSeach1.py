import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler  
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score

from sklearn.svm import LinearSVC, SVC
# from sklearn.neighbors import KNeighborsClassifier  # Classifier : 분류모델
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression # 회귀가 아닌 분류 모델임

import warnings
warnings.filterwarnings('ignore')

# Data
iris = load_iris()
data = iris.data 
target = iris.target
# print(x.shape)  # (150, 4)
# print(y.shape)  # (150, )

# preprocessing 
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=44)

kfold = KFold(n_splits=5, shuffle=True) # 데이터를 5등분

parameters = [
    {"C" : [1, 10, 100, 1000], "kernel" : ["linear"]},                              # 4번 계산
    {"C" : [1, 10, 100], "kernel" : ["rbf"], "gamma" : [0.001, 0.0001]},            # 6번 계산
    {"C" : [1, 10, 100, 1000], "kernel" : ["sogmoid"], "gamma" : [0.001, 0.0001]}   # 8번 계산
]   # 한 번 kfold를 돌 때마다 총 18번 파라미터 계산

# Modeling
# model = SVC()
model = GridSearchCV(SVC(), parameters, cv=kfold)
# 모델 : SVC 모델을 GridSearchCV로 쌓음
# parameters : SVC에 들어가 있는 파라미터 값들 (딕셔너리 형태)
# 총 90번 모델이 돌아감

# fitting
model.fit(x_train, y_train)

# evaluate
print("최적의 매개변수 : ", model.best_estimator_)
#  model.best_estimator_ : 어떤 파라미터가 가장 좋은 값인지 알려줌

# prediction
y_pred = model.predict(x_test)
print('최종정답률', accuracy_score(y_test, y_pred))

aaa = model.score(x_test, y_test)
print('aaa ', aaa)

# 최적의 매개변수 :  SVC(C=1, kernel='linear')
# 최종정답률 0.9666666666666667
# aaa  0.9666666666666667