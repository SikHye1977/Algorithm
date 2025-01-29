# [BOJ] 2023은 무엇이 특별할까? / Bronze 4 / 3m
T = int(input())

for i in range(T):
  test = int(input())
  if((test + 1) % (test % 100) == 0):
    print('Good')
  else:
    print('Bye')
    
# 간단한 몸풀기 문제
# N + 1이 N의 끝 두자리로 나누어 떨어지면 Good을, 아니면 Bye를 출력