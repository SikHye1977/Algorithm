#알파벳 찾기 / Bronze 2 / 5m
S = input().strip()

arr = [-1] * 26

str = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(S)):
  for j in range(len(str)):
    if(S[i] == str[j] and arr[j] == -1):
      arr[j] = i

print(*arr)

# 바보같이 중간에 체크용으로 놔뒀던 print문을 놔둬서 틀렸었다.
# 몸풀기 문제