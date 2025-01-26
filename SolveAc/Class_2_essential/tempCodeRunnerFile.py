N = int(input())
arr = list(map(int,input().split()))
MAX = max(arr)

ans = []
for i in range(N):
  ans.append(arr[i]/MAX*100)
  
print(sum(ans)/3)