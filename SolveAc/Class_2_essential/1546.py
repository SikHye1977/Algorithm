# [BOJ] 평균 / Bronze 1 / 10m
N = int(input())
arr = list(map(int,input().split()))
MAX = max(arr)

ans = []
for i in range(N):
  ans.append(arr[i]/MAX*100)
  
print(sum(ans)/N)

# 처음에 나눗셈을 바보같이 상수로 집어넣어서 틀렸다.
# 아주 간단한 문제.
# 식을 문제에서 제공해준다.