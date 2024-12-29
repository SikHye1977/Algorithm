arr = []
for i in range(5):
  N = int(input())
  arr.append(N)
  
arr.sort()
print(int(sum(arr)/5))
print(arr[2])

# 이것 또한 몸풀기 문제 