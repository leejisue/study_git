import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 8], [7, 6]])

print(A @ B)
'''
[[19 22]
 [43 50]]
'''
print(B @ A)
'''
[[23 34]
 [31 46]]
'''
print(A @ (B + C))
'''
[[42 42]
 [98 98]]
'''
print(A @ B + A @ C)
'''
[[42 42]
 [98 98]]
'''
print((A + B) @ C)
'''
[[110  96]
 [174 152]]
'''
print(A @ C + B @ C)
'''
[[110  96]
 [174 152]]
'''

# Transpose연산에도 분배 법칙이 성립합니다.
print((A + B).T)
'''
[[ 6 10]
 [ 8 12]]
'''
print(A.T + B.T)
'''
[[ 6 10]
 [ 8 12]]
'''
print((A @ B).T)
'''
[[19 43]
 [22 50]]
'''
print(B.T @ A.T)
'''
[[19 43]
 [22 50]]
'''