# [BOJ] Four Squares / Silver 3 / 1H
import math
n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
  minimum = 1e9
  for j in range(1, int(math.sqrt(i)) + 1):
    minimum = min(minimum, dp[i - j ** 2])
  dp[i] = minimum + 1

print(dp[n])

# python3로 제출하면 시간 초과가 뜬다.
# 어떠한 자연수 n에 대해서 n보다 작은 제곱수를 빼면
# 그 수는 반드시 어떤 제곱수들의 합일 것이므로
# n-k^2을 구성하는 제곱수의 개수보다 한개 많은 제곱수로 이루어져 있다.
# n보다 작은 제곱수를 빼준 모든 경우의 최솟값을 구하고, 1을 더해서 해결