# 쉽게 푸는 문제 / Bronze 1 / 20m
A, B = map(int,input().split())

arr = []

for i in range(1, B + 1):
  for j in range(i):
    arr.append(i)
  
sum = 0 
  
for i in range(A - 1, B):
  sum += arr[i]
  
print(sum)

# 쉽게 푸는 문제인데
# 인덱스 때문에 별로 쉽게 풀리지 않았다.
# 처음에 배열 생성을 for i in range(B)로 했었는데
# for i in range(1, B + 1)로 설정해야한다.