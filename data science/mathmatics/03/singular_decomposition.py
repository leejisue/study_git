import numpy as np
from numpy.linalg import svd

A = np.array([[3, -1], [1, 3], [1, 1]])
U, S, VT = svd(A)

print(U)
'''
[[-4.08248290e-01  8.94427191e-01 -1.82574186e-01]
 [-8.16496581e-01 -4.47213595e-01 -3.65148372e-01]
 [-4.08248290e-01 -2.06937879e-16  9.12870929e-01]]
'''

print("===========================================")
print(S)    # [3.46410162 3.16227766]

print("===========================================")
print(np.diag(S, 1)[:, 1:])
'''
[[3.46410162 0.        ]
 [0.         3.16227766]
 [0.         0.        ]]
'''

print("===========================================")
print(VT)
'''
[[-0.70710678 -0.70710678]
 [ 0.70710678 -0.70710678]]
'''

print("===========================================")
print(U @ np.diag(S, 1)[:, 1:] @ VT)
'''
[[ 3. -1.]
 [ 1.  3.]
 [ 1.  1.]]
'''

# 축소형을 구하려면 인수 full_matrices=False 로 지정한다.
U2, S2, VT2 = svd(A, full_matrices=False)

print("===========================================")
print(U2)
'''
[[-4.08248290e-01  8.94427191e-01]
 [-8.16496581e-01 -4.47213595e-01]
 [-4.08248290e-01 -2.06937879e-16]]
'''

print("===========================================")
print(S2)   # [3.46410162 3.16227766]

print("===========================================")
print(VT2)
'''
[[-0.70710678 -0.70710678]
 [ 0.70710678 -0.70710678]]
'''

print("===========================================")
print(U2 @ np.diag(S2) @ VT2)
'''
[[ 3. -1.]
 [ 1.  3.]
 [ 1.  1.]]
'''