# 1 : 다 mlp 함수형
# keras10_mlp6.py 를 함수형으로 바꾸시오
import numpy as np

# DATA
x = np.array( range(100) )
y = np.array( [range(711, 811), range(1, 101), range(201, 301)] )  

print(x.shape)          #(100, )
print(y.shape)          #(3, 100)
x = np.transpose(x)     
# print(x)
print(x.shape)          #(100, )
y = np.transpose(y)     
print(y.shape)          #(100, 3)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, shuffle=True, random_state=66) 
print(x_train.shape)     #(80,) 
print(y_train.shape)     #(80,3)
print(x_test.shape)      #(20,)

x_pred2 = np.array([100])
x_pred2 = x_pred2.reshape(1,1) 
print("x_pred2.shape_transpose : ", x_pred2.shape)  #(1, 1) 2차원


#2. Modeling
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input

# 함수혇
input1 = Input(shape=(1,))
dense1 = Dense(100, activation='relu')(input1)
dense2 = Dense(100)(dense1)
dense3 = Dense(10)(dense2)
dense4 = Dense(10)(dense3)
output = Dense(3)(dense4)
model = Model(inputs = input1, outputs = output)
model.summary()

# Sequential
# model = Sequential()
# model.add(Dense(100, input_dim = 1)) #input 1개
# model.add(Dense(100))
# model.add(Dense(10))
# model.add(Dense(10))
# model.add(Dense(5))
# model.add(Dense(3)) # output= 3 

#3. Compile, Train
model.compile(loss='mse', optimizer='adam', metrics=['mae'])
model.fit(x_train, y_train, epochs=100, batch_size=1, validation_split=0.6) 

#4. Predict, Evaluate
loss, mae = model.evaluate(x_test, y_test)
print('loss : ', loss)
print('mae : : ', mae)

y_predict = model.predict(x_test)
print(y_predict) 

from sklearn.metrics import mean_squared_error 
def RMSE (y_test, y_predict) :                 # y_test, y_predict의 shpae 를 맞춰야 함 (20,3)
      return np.sqrt(mean_squared_error(y_test, y_predict)) 
print("RMSE :", RMSE(y_test, y_predict))

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_predict)
print("R2 : ", r2)

# loss :  1.6617516251926645e-08
# mae : :  0.00010577440116321668
# RMSE : 0.00012890894099203807
# R2 :  0.9999999999789738

y_predict2 = model.predict(x_pred2)
print(y_predict2) 
print(y_predict2.shape) #(1,3)