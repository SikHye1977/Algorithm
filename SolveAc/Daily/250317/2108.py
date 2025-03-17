# [BOJ] 통계학 / Silver 3 / 40m
import sys
N = int(sys.stdin.readline())

arr = []

for i in range(N):
  temp = int(sys.stdin.readline())
  arr.append(temp)

arr.sort()

print(round(sum(arr) / N))
print(arr[N//2])

dic = dict()
for i in arr:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
  
max_value = max(dic.values())
max_dic = []

for i in dic:
  if(max_value == dic[i]):
    max_dic.append(i)
  
if (len(max_dic) > 1):
  print(max_dic[1])
else:
  print(max_dic[0])

print(max(arr) - min(arr))

# 값을 입력받아 배열에 저장한다.
# 1번 산술 평균을 계산 할 때
# round(sum(arr) // N)
# 위와 같이 정수 나눗셈을해서 틀렸었다.
# 최빈값을 dic에 저장하고,
# 최댓값을 저장 할 배열을 하나 더 만들어서
# 최빈값의 key를 배열에 추가하고
# 최빈값이 여러개인지 아닌지에 따라 값을 다르게 출력한다.