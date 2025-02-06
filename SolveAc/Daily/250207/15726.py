# [BOJ] 이칙연산 / Bronze 4 / 10m
arr = list(map(int,input().split()))

print(arr[0] * max(arr[1], arr[2]) // min(arr[1], arr[2]))

# 최대값을 곱하고 최솟값을 나눠줘야 함