# 최댓값 / Bronze 3 / 3m
arr = []
for i in range(9):
  num = int(input())
  arr.append(num)
  
count = 0
check = max(arr)
for i in range(9):
  if(arr[i] != check):
    count += 1
  else:
    break
  
print(check)
print(count + 1)

# 몸풀기 문제
# 근데 출력 조건 제대로 안읽어서 한번 틀렸다.