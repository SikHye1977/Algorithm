# 좌표 정렬하기 / Silver 5 / 3m
N = int(input())

arr = []

for i in range(N):
  x, y = map(int,input().split())
  arr.append((x,y))
  
arr.sort(key=lambda x : (x[0], x[1]))

for i in range(len(arr)):
  print(*arr[i])
  
# 10814번이랑 비슷한 문제
# lambda로 조건만 잘 주면 된다.