# 문자열 반복 / Bronze 2 / 20m
N = int(input())

ans = []

for i in range(N):
  data = input().split()
  num = int(data[0])
  str = data[1]
  arr = []
  for j in range(len(str)):
    arr.append(str[j] * num)
  ans.append(arr)

for i in range(len(ans)):
  for j in range(len(ans[i])):
    print(ans[i][j], end='')
  print()
  
# 입력값 분할때문에 참고자료를 찾아봤다.
# 나머지 로직은 구현하는데 어려움은 없었다.