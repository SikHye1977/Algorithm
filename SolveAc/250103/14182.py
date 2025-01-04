arr = []
while True:
  num = int(input())
  if(num == 0):
    break
  arr.append(num)

for i in range(len(arr)):
  if(arr[i] <= 1000000):
    print(arr[i])
  elif(arr[i] > 1000000 and arr[i] <= 5000000):
    print(arr[i] - int(arr[i] * 0.1))
  else:
    print(arr[i] - int(arr[i] * 0.2))
    
# 문제가 영어로 적혀있어서 뭔가 했는데
# 아무것도 아니었다.
