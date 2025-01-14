# 좌표 압축 / Silver 2 / 30m
N = int(input())

arr = list(map(int,input().split()))
set_arr = set(arr)
set_arr = sorted(set_arr)

dic = {set_arr[i]:i for i in range(len(set_arr))}

for i in arr:
  print(dic[i], end=" ")

# 아래와 같이 그냥 이중 반복문이나 이진탐색으로 풀면 시간 초과가 뜬다
# for i in range(len(arr)):
#   target = arr[i]
#   for j in range(len(set_arr)):
#     if(target == set_arr[j]):
#       ans.append(j)
#       break

# for i in range(len(arr)):
#   target = arr[i]
#   start = 0
#   end = len(set_arr) - 1
#   while start <= end:
#     mid = (start + end) // 2
#     if(target == set_arr[mid]):
#       ans.append(mid)
#       break
#     elif(target < set_arr[mid]):
#       end = mid - 1
#     else:
#       start = mid + 1

# 딕셔너리 자료형을 이용해서 풀었다.
# 딕셔너리 참고자료 : https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-18870-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95%ED%8C%8C%EC%9D%B4%EC%8D%AC