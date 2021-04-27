# 시간 복잡도 구하요
# 1부터 n까지의 합을 구하는 알고리즘1
    # 입력 n에 따라 덧셈을 n번 해야 함 (반복문!)
    # 시간 복잡도 : n, Big O Notation으로는 O(n)

# 알고리즘 2 : 1부터 n까지의 합을 구하는 알고리즘
    # n * (n + 1) / 2

def sum_all(n):
    return int(n * (n + 1) / 2)

print(sum_all(3))   # 6
print(sum_all(100)) # 5050

# 시간 복잡도 구하기
# 1부터 n까지의 합을 구하는 알고리즘
    # 입력 n이 어떻든 간에, 곱셈 / 덧셈 / 나눗셈 하면 됨 (반복문이 없음!)
    # 시간 복잡도 : 1, Big O Notation으로는 O(1)

# 어느 알고리즘 성능이 좋은가요?
# 알고리즘 1 vs 알고리즘 2
    # O(n) vs O(1)
    # 위와 같이, 동일한 문제를 푸는 알고리즘은 다양할 수 있음.
    # 어느 알고리즘이 보다 좋은지를 객관적으로 비교하기 위해, 빅 오 표기법등의 시간복잡도 계산법을 사용함
    