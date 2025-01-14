# A+B - 5 / Bronze 5 / 1m
ans = []

while True:
  A, B = map(int,input().split())
  if(A == 0 and B == 0):
    break
  else:
    ans.append(A + B)
  
for i in range(len(ans)):
  print(ans[i])