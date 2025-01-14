# A+B - 3 / Bronze 5 / 1m
T = int(input())

ans = []

for i in range(T):
  A, B = map(int,input().split())
  ans.append(A + B)
  
for i in range(len(ans)):
  print(ans[i])