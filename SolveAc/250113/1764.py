# 듣보잡 / silver 4 / 30m
N, M = map(int, input().split())

dutbo =[]

for i in range(N):
  str = input()
  dutbo.append(str)
  
dutbo.sort()
  
dut = []

for j in range(M):
  str = input()
  dut.append(str)
  
ans = []
count = 0

for i in range(len(dut)):
  start = 0
  end = len(dutbo) - 1
  while start <= end:
    mid = (start + end) // 2
    if(dut[i] == dutbo[mid]):
      ans.append(dut[i])
      count += 1
      break
    elif(dut[i] < dutbo[mid]):
      end = mid - 1
    else:
      start = mid +  1
      
ans.sort()

print(count)
for i in range(len(ans)):
  print(ans[i])
  
# 알고리즘 분류는 해시를 사용한 집합과 맵이지만
# 그냥 이진 탐색으로 풀었다.
# 시간초과는 안뜨지만 조금 느리긴 했다.