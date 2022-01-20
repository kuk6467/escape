'''내장 함수 확인 https://docs.python.org/ko/3.7/library/functions.html
내장 함수 확인 https://docs.python.org/ko/3.8/py-modindex.html
https://python.flowdas.com/library/random.html
'''

# # 가능한 함수 출력
import random
# print(dir())
# print(dir(random))

# # 절대 값
# print(abs('-3'))

# # 모든 요소 참 True 출력
# print(all(lst))

# # 한개라도 참 True 출력
# print(any(lst))

# # 2진 숫자로 출력
# print(bin(3))

# # random 함수
# print(random.random())  # random 실수 0.0 ~ 1.0 사이
# print(random.uniform(10, 20))  # random 실수 10.0 ~ 20.0 사이
# print(random.randint(10, 20))  # random 정수 0.0 ~ 1.0 사이
# print(random.randrange(7, 10))  # random b를 포함하지 않는 정수
# print(random.expovariate(1/5))
# Single random element from a sequence
print(random.choice(['win', 'lose', 'draw']))
