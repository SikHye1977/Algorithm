# 친구 / Bronze 2 / 10m
N, M = map(int, input().split())

arr = []

for i in range(M):
  A, B = map(int,input().split())
  arr.append((A,B))
  
ans = [0] * N

for i in range(len(arr)):
  target1 = arr[i][1] - 1
  ans[target1] += 1
  target2 = arr[i][0] - 1
  ans[target2] += 1
  
for i in range(len(ans)):
  print(ans[i])
  
# 양방향 친구관계를 고려하지 않고, 초기 배열을 1로 초기화 해서 들렸다
# 초기 배열을 0으로 초기화 하고, A의 친구에 +1, A에게 +1 하는 방식으로 해결했다.