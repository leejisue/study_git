# eval_set : validation0, 1을 볼 수 있음
# eval_metric : 메트릭스를 지정
# evals_result : eval_metric 에 지정했던 rmse가 줄어드는 걸 볼 수 있음
from xgboost import XGBClassifier, XGBRegressor
from sklearn.datasets import load_boston, load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import r2_score, accuracy_score

# Data
# data, target = load_boston(return_X_y=True)
boston = load_boston()
data = boston.data
target = boston.target

x_train, x_test, y_train, y_test = train_test_split(\
    data, target, test_size=0.2, shuffle=True, random_state=66)

# Modeling
model = XGBRegressor(n_estimators=100, learning_rate=0.01, n_jobs=8)

# Fitting
# model.fit(x_train, y_train, verbose=1, eval_metric='rmse', eval_set=[(x_train, y_train), (x_test, y_test)])

model.fit(x_train, y_train, verbose=1, eval_metric=['rmse','logloss','mae'], eval_set=[(x_train, y_train), (x_test, y_test)])
# [99]    validation_0-rmse:9.42809       validation_0-logloss:-791.72455 validation_0-mae:8.32016        validation_1-rmse:9.45347       validation_1-logloss:-799.52972 validation_1-mae:8.35589

# Evaluate
aaa = model.score(x_test, y_test)
print("aaa : ", aaa)    # r2 score = score

# Prediction
y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)
print("r2 :", r2)

# aaa :  -4.690504661286998
# r2 : -4.690504661286998

print("================")
result = model.evals_result()
print(result)  
# {'validation_0': OrderedDict([('rmse', [23.611168, 23.387598, 23.166225, 22.947048, 22.730053, 22.515182, 22.302441, 22.091829, 21.883278, 21.676794])]), 'validation_1': OrderedDict([('rmse', [23.777716, 23.54969, 23.323978, 23.100504, 22.87919, 22.660995, 22.444965, 22.23027, 22.018494, 21.808922])])}
