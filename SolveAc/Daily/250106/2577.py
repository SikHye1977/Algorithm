# 숫자의 개수 / Bronze 2 / 5분 걸림
target = 1
for i in range(3):
  num = int(input())
  target = target * num

target = str(target)

ans = [0] * 10

for i in range(len(target)):
  check = int(target[i])
  ans[check] += 1
  
for i in range(len(ans)):
  print(ans[i])
  
# 타입 변경만 생각해주면 간단한 문제