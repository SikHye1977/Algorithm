N, K = map(int,input().split())

arr = list(map(int,input().split(',')))
ans = [0] * len(arr)

if(K == 0):
  print(*arr, sep=',')
else:
  for i in range(K):
    for i in range(len(ans) - 1):
      ans[i] = arr[i+1]-arr[i]
    ans.pop(len(ans)-1)
    arr = ans
  print(*ans, sep=',')
  
# 문제 조건을 제대로 읽어보자
# 출력값 형식을 제대로 지정하자
# 25분 걸림