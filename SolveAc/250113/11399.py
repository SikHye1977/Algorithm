# ATM / Silver 4 / 10m
N = int(input())

arr = list(map(int,input().split()))

arr.sort()

ans = []
sum = 0

for i in range(N):
  sum += arr[i]
  ans.append(sum)
  
sum_ans = 0 

for i in range(N):
  sum_ans += ans[i]
  
print(sum_ans)

# 그리디 알고리즘으로 분류된 문제
# 그냥 정렬 한 0~N의 합으로 배열을 만들고
# 그 합으로 반들어진 배열의 전체 합을 구해서 풀었다.