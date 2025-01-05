# OX퀴즈 / Bronze 2 / 5m
N = int(input())

for i in range(N):
  str = input()
  count = 0
  sum = 0
  for j in range(len(str)):
    if(str[j] == 'O'):
      sum += count + 1
      count += 1
    elif(str[j] == 'X'):
      count = 0
  print(sum)
  
# 간단한 몸풀기 문제
# 조건에 맞춰 더해주는 값을 조절해야함
# O가 들어왔을 때 이전의 count + 1을 합에 더해주고 count를 1 증가
# X일때는 count를 0으로 초기화