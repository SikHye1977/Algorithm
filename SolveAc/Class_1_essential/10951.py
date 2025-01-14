# A+B - 4 / Bronze 5 / 1m
ans = []

while True:
  try:
    A, B = map(int,input().split())
    ans.append(A + B)
  except:
    break
  
for i in range(len(ans)):
  print(ans[i])
  
# 문제에 입력 제한이 없어서 뭔 개소린가 했는데
# try, except 구문을 활용하라는 뜻이었다.