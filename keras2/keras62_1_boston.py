# DNN & ML
# from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import numpy as np
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Dropout, Input
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Data
boston = load_boston()
data = boston.data
target = boston.target

# Preprocessing
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3, random_state=42)
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
print(x_train.shape, x_test.shape)    # (404, 13) (102, 13)

# Modeling
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier, KerasRegressor
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

def build_model(drop=0.5, optimizer='adam', activation='relu') :
    inputs = Input(shape = (13,), name='input')
    x = Dense(32, activation=activation, name='hidden1')(inputs)
    x = Dense(32, activation=activation, name='hidden2')(x)
    x = Dense(64, activation=activation, name='hidden3')(x)
    x = Dense(64, activation=activation, name='hidden4')(x)
    x = Dense(128, activation=activation, name='hidden5')(x)
    x = Dropout(drop)(x)
    x = Dense(128, activation=activation, name='hidden6')(x)
    x = Dropout(drop)(x)
    outputs = Dense(1, activation='relu', name='outputs')(x)
    model = Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
    return model

def create_hyperparameters() :
    batches = [2, 4, 8, 16]
    optimizers = ['rmsprop', 'adam', 'adadelta']
    dropout = [0.1, 0.2, 0.3]
    activation =['relu','elu','prelu']
    return {"batch_size" : batches, "optimizer" : optimizers, "drop" : dropout, "activation" : activation}

# model2 = build_model()
model2 = KerasRegressor(build_fn=build_model, verbose=1, epochs=100)   

path = '../data/modelcheckpoint/k62_1_{epoch:02d}_{val_loss:.3f}.hdf5'
cp = ModelCheckpoint(path, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
es = EarlyStopping(monitor='val_loss', mode='min', patience=5, verbose=1)
lr = ReduceLROnPlateau(monitor='val_loss', mode='min', factor=0.4, patience=3, verbose=1)

hyperparameters = create_hyperparameters()

from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
# search = RandomizedSearchCV(model2, hyperparameters, cv=2)
search = GridSearchCV(model2, hyperparameters, cv=2)

search.fit(x_train, y_train, verbose=1, validation_split=0.2, callbacks=[es, lr, cp])

print("best_params : ", search.best_params_)         
# best_params :  {'activation': 'relu', 'batch_size': 4, 'drop': 0.1, 'optimizer': 'adam'}
print("best_estimator : ", search.best_estimator_)   
# best_estimator :  <tensorflow.python.keras.wrappers.scikit_learn.KerasClassifier object at 0x000001C0872F5DF0>
print("best_score : ", search.best_score_)           
# best_score :  -17.9723482131958

loss = search.score(x_test, y_test)
print("Score : ", loss)
# Score :  -16.297247123718262
