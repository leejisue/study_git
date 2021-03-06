import numpy as np

# exercise 2.2.1
# A, B, C 세 회사의 주식은 각각 100만원, 80만원, 50만원이다. 이 주식을 각각 3주, 4주, 5주를 매수할 때 필요한 금액을 구하고자 한다.
# (1) 주식의 가격과 수량을 각각 p 벡터, n 벡터로 표시하고 넘파이로 코딩한다.
# (2) 주식을 매수할 때 필요한 금액을 곱셈으로 표시하고 넘파이 연산으로 그 값을 계산한다.

p = np.array([[1000000],[800000],[500000]])
n = np.array([[3],[4],[5]])

print(p.T @ n)  # [[8700000]]