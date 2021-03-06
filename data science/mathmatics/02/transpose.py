import numpy as np

A = np.array([[11,12,13],[21,22,23]])

print(A)
'''
[[11 12 13]
 [21 22 23]]
'''
# ==============================================================
# Transpose 수행

B = A.T
print(B)
'''
[[11 21]
 [12 22]
 [13 23]]
'''

# ==============================================================
x1 = np.array([5.1,3.5,1.4,0.2])
x2 = x1.T
print(x1)
print(x2)

# 1차원 데이터의 경우에 Transpose를 시켜도 변화가 없음


