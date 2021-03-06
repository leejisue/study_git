# 알고리즘 작성 연습하기
# 알고리즘을 잘 작성하기 위해서는 잘 작성된 알고리즘을 이해하고, 스스로 만들어 봐야 함
    # 모사! 그림을 잘 그리기 위해서는 잘 그린 그림을 모방하는 것부터 시작

# 알고리즘 연습 방법
    # 1. 연습장과 펜을 준비하지.
    # 2. 알고리즘 문제를 읽고 분석한 후에, 
    # 3. 간단하게 테스트용으로 매우 간단한 경우부터 복잡한 경우 순서대로 생각해보면서, 연습장과 펜을 이용하여 알고리즘을 생각해본다.
    # 4. 가능한 알고리즘이 보인다면, 구현할 알고리즘을 세부 항목으로 나누고, 문장으로 세부 항목을 나누어서 적어본다.
    # 5. 코드화하기 위해, 데이터 구조 또는 사용할 변수를 정리하고,
    # 6. 각 문장을 코드 레벨로 적는다.
    # 7. 데이터 구조 또는 사용할 변수가 코드에 따라 어떻게 변하는지를 손으로 적으면서, 임의 데이터로 코드가 정상 동작하는지를 연습장과 펜으로 검증한다.

# 예 : 팩토리얼 구하기
    # 팩토리얼 n! = n(n-1) (n-2) ... 1

# 간단한 경우부터 생각해보기
    # 2! = 1 x 2
    # 3! = 1 x 2 x 3
    # 4! = 1 x 2 x 3 x 4

# 2.1.2 규칙이 보임 : n! = n x (n-1)!
    # 함수를 하나 만든다.
    # 함수(n)은 1부터 n까지 곱하면 됨
    # 반복문 range(1, n + 1)

# 검증 (코드로 검증하지 않고, 직접 간단한 경우부터 대입해서 검증해야 함)
# 반복문 range(1, n+1) 이라고 생각하면
    # 1. 먼저 2! 부터
        # 함수(2) 이면, 1 x 2 [2(n)]
    # 2. 먼저 3! 부터
        # 함수(3) 이면, 1 x 2 x 3 [3(n)]
    # 3. 먼저 4! 부터
        # 함수 (4) 이면, 1 x 2 x 3 x 4 [4(n)]

# 코드 레벨로 적어보기
# 2.1.2 항목에서 적어놓은 문장을 코드로 옮긴다. 필기에서는 좀더 코드레벨로 연습장에 적은 후에 작성
def factorial(n):
    factorial_value = 1
    for factorial_item in range(1, n + 1):
        factorial_value = factorial_value * factorial_item
    return factorial_value

print(factorial(5)) # 120
print(1 * 2 * 3 * 4 * 5)