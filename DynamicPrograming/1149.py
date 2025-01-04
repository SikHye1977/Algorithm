N = int(input())

arr = []
dp = [[0]*3 for _ in range(N)]

for i in range(N):
  num = list(map(int, input().split()))
  arr.append(num)

dp[0] = arr[0]

for i in range(1,N):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
  
print(min(dp[N-1]))


# https://velog.io/@monam2/Python-RGB%EA%B1%B0%EB%A6%AC-%EB%B0%B1%EC%A4%80-1149%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC