# 숫자 카드 2 / Silver 4 / 1h"
N = int(input())
card = list(map(int,input().split()))
card.sort()

M = int(input())
find = list(map(int,input().split()))

dic = {}

for i in card:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

for i in find:
  if i in dic:
    print(dic[i], end=' ')
  else:
    print(0, end=' ')

# 아래처럼 이진 탐색으로 풀려 했는데 중복되는 수를 처리하기가 어려워서 포기했다
# https://dev-sungjun.tistory.com/37
# 블로그를 참고해서 파이썬 자료형인 dictionary로 풀었다.


# for i in range(len(find)):
#   start = 0
#   end = len(find)
#   while start <= end:
#     mid = (start + end) // 2
#     if(find[i] == card[mid]):
#       ans[i] += 1
#       break
#     elif(find[i] > card[mid]):
#       start = mid + 1
#     else:
#       end = mid - 1
  
      
# print(*ans)
