# 음계 / Bronze 2 / 10m
arr = list(map(int, input().split()))

if(arr == sorted(arr)):
  print('ascending')
elif(arr == sorted(arr, reverse=True)):
  print('descending')
else:
  print('mixed')
  
# 처음에 배열 체크해서 풀었는데
# 그냥 정렬해서 풀면 되는 문제였음
# 정렬방법은 구글링 함