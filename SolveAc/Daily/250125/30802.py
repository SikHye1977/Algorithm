# [BOJ] 웰컴 키트 / Bronze 3 / 30m
N = int(input())
arr = list(map(int,input().split()))
T, P = map(int,input().split())

count = 0
for i in arr:
    count += (i + T - 1) // T

print(count)
print(N // P, N % P)

# 간단한 수학 구현 문제
# 문제가 무슨 소리를 하는지 못알아 먹어서 푸는데 한참 걸렸다.