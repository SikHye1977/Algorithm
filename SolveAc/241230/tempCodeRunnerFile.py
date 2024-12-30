N = int(input())
M = int(input())

arr = list(map(int,input().split()))
score = [0] * N

for i in range(M):
  ans = list(map(int,input().split()))
  count = 0
  check = arr[i] - 1
  for j in range(N):
    if(arr[i] == ans[j]):
      score[j] += 1
    else:
      count += 1
  score[check] += count
      

print(score)