# [BOJ] 직각삼각형 / Bronze 3 / 10m
while True:
  arr = list(map(int,input().split()))
  if(arr[0] == 0 and arr[1] == 0 and arr[2] == 0):
    break
  arr.sort()
  
  if(arr[2] ** 2 == arr[0] ** 2 + arr[1] **2):
    print('right')
  else:
    print('wrong')

# 반복문 탈출 조건을 이상하게 적어놔서 틀렸었다.
# 피타고라스 정리를 쓰는 간단한 문제