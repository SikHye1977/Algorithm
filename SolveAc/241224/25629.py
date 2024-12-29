N = int(input())
arr = list(map(int, input().split()))

odd = 0
even = 0
for i in range(N):
  if arr[i] % 2 == 1:
    odd += 1
  else:
    even += 1
    
if odd == even or odd == even + 1:
  print(1)
else:
  print(0)
  
# 다시 공부할 필요가 있다.