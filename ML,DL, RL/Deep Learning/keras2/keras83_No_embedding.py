# 자연어 처리
# 긍정 / 부정 텍스트를 맞춰본다.
# embedding 레이러를 빼고 구성 / 성능비교

from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

docs = ['너무 재밌어요', '참 최고에요', '참 잘 만든 영화예요', '추천하고 싶은 영화입니다',
        '한 번 더 보고 싶네요','글쎄요','별로에요','생각보다 지루해요',
        '연기가 어색해요','재미없어요','너무 재미없다','참 재밌네요','규현이가 잘 생기긴 했어요']

# 긍정 1, 부정 0
labels = np.array([1,1,1,1,1,0,0,0,0,0,0,1,1])  # y : (13,)

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
# {'참': 1, '너무': 2, '잘': 3, '재밌어요': 4, '최고에요': 5, '만든': 6, '영화예요': 7, '추천하고': 8, '싶은': 9, '영화입니다': 10, '한': 11, '번': 12, '더': 13, '보고': 14, '싶네요': 15, '글쎄요': 16, '별로에요': 17, '
# 생각보다': 18, '지루해요': 19, '연기가': 20, '어색해요': 21, '재미없어요': 22, '재미없다': 23, '재밌네요': 24, '규현이가': 25, '생기긴': 26, '했어요': 27}

x = token.texts_to_sequences(docs)
print(x)
# [[2, 4], [1, 5], [1, 3, 6, 7], [8, 9, 10], [11, 12, 13, 14, 15], [16], [17], [18, 19], [20, 21], [22], [2, 23], [1, 24], [25, 3, 26, 27]]
# 문제점 : 문장의 길이가 다 다르다.
# 해결점 : 가장 긴 문장을 기준으로 문장의 길이를 맞춰준다. 나머지 공간은 0으로 채워준다. 
# 주의점 : 모델은 뒤로갈 수록 영향력이 크기 때문에 앞에서 0을 채운다.

from tensorflow.keras.preprocessing.sequence import pad_sequences
pad_x = pad_sequences(x, padding='pre', maxlen=5)  

print(pad_x)
print(pad_x.shape)  # (13, 5)

print(np.unique(pad_x))
print(len(np.unique(pad_x)))
# [ 0  1  2  3  4  5  6  7  8  9 10 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27] >>> 11이 maxlen 길이 초과로 인해 잘렸다.
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27] 
# 28


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Flatten, Conv1D, BatchNormalization

model = Sequential()

# 임베딩 없는 LSTM 
pad_x = pad_x.reshape(13,5,1)
model.add(LSTM(32, activation='relu', input_shape=(5,1)))

# 임베딩 없는 Dense
# model.add(Dense(32, activation='relu', input_shape=(5,)))

model.add(Dense(16))
model.add(Dense(8))
model.add(Dense(1, activation='sigmoid'))

model.summary()


model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(pad_x, labels, epochs=100)

acc = model.evaluate(pad_x, labels)[1]
print("accuracy : ", acc)

# Embedding 있을 때, =================
# LSTM
# accuracy :  1.0

# Embedding 없을 때, =================
# LSTM
# accuracy :  0.9230769276618958

# DNN
# accuracy :  0.9230769276618958
