# 나이순 정렬 / Silver 5 / 30m
N = int(input())

arr = []

for i in range(N):
  age, name = map(str, input().split())
  temp = []
  temp.append(int(age))
  temp.append(name)
  arr.append(temp)
  
arr.sort(key = lambda x: x[0])

for i in range(N):
  print(*arr[i])

# 그냥 sort 때리면 안된다.
# 나이로만 비교했다. 나이가 같으면 먼저 기입한 사람이 앞에 와야하기 때문
# 이 조건이 헷갈려서 시간을 좀 잡아먹었다.