# 과제 및 실습 / LSTM
# EarlyStopping, preprocessing all in
# 데이터 1 ~ 100 
#    x               y
# 1 2,3,4,5          6
# ...
# 95,96,97,98,99    100
# predict를 만들 것
# 96,97,98,99,100 -> 101
# ...
# 100,101,102,103,104 -> 105
# 예상 predict는  (101,102,103,104,105)
import numpy  as np

a = np.array(range(1, 101))
size = 6

# LSTM 모델을 구성하시오

def split_x(seq, size) :
    aaa = []  
    for i in range(len(seq) - size + 1) :       # range(len(seq) - size + 1) : 반복횟수(= 행의 개수), # size : 열의 개수
        subset = seq[i : (i+size)]
        aaa.append(subset)
    # print(type(aaa))
    return np.array(aaa)

dataset = split_x(a, size)  # (6, 5)
# print(dataset)

#1. Data
x = dataset[:,:5] 
# print(x) 
# print(x.shape)      # (95, 5) -> (95, 5, 1) -> (5, 1)

y = dataset[:,-1:]  
# print(y)
# print(y.shape)      # (95, 1)

pred = np.array(range(96, 106))
size_pred = 6
dataset_pred = split_x(pred, size_pred)  # (6, 5)

x_pred = dataset_pred[:,:5] 
# print(x_pred)
# print(x_pred.shape) # (5, 5)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, shuffle=True, random_state=44)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
x_pred = scaler.transform(x_pred)

# print(x_train.shape)    # (76, 5)
# print(x_test.shape)     # (19, 5)
# print(x_pred.shape)     # (5, 5)

x_train = x_train.reshape(76, 5, 1)
x_test = x_test.reshape(19, 5, 1)
x_pred = x_pred.reshape(5, 5, 1)

#2. Modeling
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, LSTM,Input

input1 = Input(shape = (5,1))
dense1 = LSTM(300,activation = 'relu')(input1)
dense1 = Dense(150)(dense1)
dense1 = Dense(74)(dense1)
dense1 = Dense(36)(dense1)
dense1 = Dense(1)(dense1)
model = Model(inputs=input1, outputs = dense1)

# model.summary()

#3. Compile, Train
model.compile(loss='mse', optimizer='adam', metrics=['mae'])

from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='loss',patience=10, mode='min')
model.fit(x_train, y_train, epochs=2000, batch_size=5, validation_split=0.2, callbacks=[early_stopping])

#4. Evaluate, Predcit
loss, mae = model.evaluate(x_test, y_test, batch_size=5)
print("loss : ", loss)
print("mae : ", mae)

y_pred = model.predict(x_pred)
print("y_pred : \n", y_pred)

# LSTM
# mae :  0.09569147974252701
# y_pred : 
#  [[101.63942]
#  [102.7319 ]
#  [103.83015]
#  [104.93419]
#  [106.04402]]