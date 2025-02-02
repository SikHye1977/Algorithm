# [BOJ] 성택이의 은밀한 비밀번호 / Bronze 5 / 2m
N = int(input())

for i in range(N):
  str = input()
  if(len(str) >= 6 and len(str) <= 9):
    print('yes')
  else:
    print('no')
    
# 시간 없어서
# 스트릭 안깨질려고 푸는 문제