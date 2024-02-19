# file: ds24_forfactorial.py
# desc: 반복문으로 팩토리얼 구하기

n = 20
factValue = 1
for i in range(n, 0, -1): # 10부터 1까지 역순으로
    factValue *= i

print(f'{n}! = {factValue}')

# 재귀호출 factorial

def factorial(num):
    if num <=1: return 1
    return num * factorial(num-1)

print(f'10! = : {factorial(10)}')
# 재귀호출 1000을 하면 recursionError: maximum recursion depth exceeded 재귀호출 최고 깊이를 초과