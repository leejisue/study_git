# 나눌 열 지정하기
import numpy as np

a = np.floor(10*np.random.random((2, 12)))

print(a)
'''
[[8. 0. 7. 0. 0. 2. 7. 5. 6. 3. 2. 5.]
 [0. 3. 3. 8. 1. 2. 0. 4. 5. 7. 3. 7.]]
'''
print(np.hsplit(a, (3, 4)))
'''
[array([[8., 0., 7.],
       [0., 3., 3.]]), array([[0.],
       [8.]]), array([[0., 2., 7., 5., 6., 3., 2., 5.],
       [1., 2., 0., 4., 5., 7., 3., 7.]])]
'''