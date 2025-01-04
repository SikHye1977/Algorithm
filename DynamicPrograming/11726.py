n = int(input())

dp = [0] * 1000001

dp[0] = 1
dp[1] = 2

for i in range(2,n):
  dp[i] = (dp[i-1] + dp[i-2]) % 10007
  
print(dp[n-1])

# 10007은 왜 나눠주라는건지 모르겠다. 조건 확인때문에 시간을 날려 먹었다.
# 마찬가지로 규칙을 찾는 문제. i번째 경우의 수는 i-1번재와 i-2번째의 합과 같다.
# 10분 걸림