# 10250 / Bronze 3 / 20m
N = int(input())

ans = []

for i in range(N):
  arr = list(map(int, input().split()))
  H = 0
  # 층 수 구하기
  if(arr[0] > arr[2]):
    H = arr[2]
  elif(arr[2] % arr[0] == 0):
    H = arr[0]
  else:
    H = arr[2] % arr[0]
  
  # 호실 구하기
  W = 0
  if(arr[2] <= arr[0]):
    W = 1
  elif(arr[2] % arr[0] == 0):
    W = arr[2] // arr[0]
  else: 
    W = (arr[2] // arr[0]) + 1
  
  #호실 적기
  arr = []
  arr.append(H)
  if(W < 10):
    arr.append(0)
    arr.append(W)
  else:
    arr.append(W)
  ans.append(arr)
  
for i in range(len(ans)):
  for j in range(len(ans[i])):
    print(ans[i][j], end='')
  print()
  
# 처음부터 하나하나 경우의수를 증가시켜가며 조건을 추가했다.
# 그래서 오래 걸렸다.