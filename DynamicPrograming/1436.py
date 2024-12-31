# 1로 만들기
X = int(input())

dp = [0] * 1000001

for i in range(2, X+1):
  dp[i] = dp[i - 1] + 1
  if(i % 2 == 0):
    dp[i] = min(dp[i], dp[i//2] + 1)
  if(i % 3 == 0):
    dp[i] = min(dp[i], dp[i//3] + 1)
    
print(dp[X])
# https://velog.io/@qtly_u/DP-%EB%B0%B1%EC%A4%80-1463%EB%B2%88-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0