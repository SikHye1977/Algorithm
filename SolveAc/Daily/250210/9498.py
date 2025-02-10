# [BOJ] 시험 성적 / Bronze 5 / 1m
N = int(input())
if(N >= 90 and N <=100):
  print('A')
elif(N >= 80 and N <= 89):
  print('B')
elif(N >= 70 and N <= 79):
  print('C')
elif(N >= 60 and N <= 69):
  print('D')
else:
  print('F')
  
# 스트릭 유지용 문제