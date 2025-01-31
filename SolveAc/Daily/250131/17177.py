# [BOJ] 내접사각형 만들기 / Bronze 1 / 1h
import math
a, b, c = map(int,input().split())

p = a
q = 2 * b * c
r = a * (c * c - a * a + b * b)

d = q * q - 4 * p * r

if(d < 0):
  print(-1)
elif(int((math.sqrt(d) - q) / (2 * p)) < 0):
  print(-1)
else:
  print(int((math.sqrt(d) - q) / (2 * p)))
  
# 참고 : https://velog.io/@youngjun_10/%EB%B0%B1%EC%A4%80-%EB%82%B4%EC%A0%91%EC%82%AC%EA%B0%81%ED%98%95-%EB%A7%8C%EB%93%A4%EA%B8%B0