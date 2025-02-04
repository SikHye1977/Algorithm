# [BOJ] 검증수 / Bronze 5 / 2m
arr = list(map(int,input().split()))

sum = 0
for i in range(len(arr)):
  temp = arr[i] * arr[i]
  sum += temp
print(sum % 10)

# 스트릭 유지용 문제