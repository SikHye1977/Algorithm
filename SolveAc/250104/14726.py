N = int(input())

arr = []

for i in range(N):
  num = int(input())
  arr.append(num)
  
ans = []
count = 1

for i in range(N):
  sum = 0
  target = arr[i]
  while target > 0:
    check = target % 10
    if(count % 2 != 0):
      sum += check
    else:
      check = check * 2
      if(check < 10):
        sum += check
      else:
        while check > 0:
          sum += check % 10
          check = check // 10
    count += 1
    target = target // 10
  ans.append(sum)
      
    
for i in range(N):
  if(ans[i] % 10 == 0):
    print('T')
  else:
    print('F')
    
# 그냥 구현 문제인데
# 인덱스 잘못 생각해서 푸는데 좀 걸렸다.
# 50분 걸림