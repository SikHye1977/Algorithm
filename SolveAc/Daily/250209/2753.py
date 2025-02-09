# [BOJ] 윤년 / Bronze 5 / 3m
year = int(input())
if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
  print(1)
else:
  print(0)

# 스트릭 유지용