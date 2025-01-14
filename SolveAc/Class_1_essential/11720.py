# 숫자의 합 / Bronze 4 / 8m
N = int(input())
num = input()

sum = 0

for i in range(N):
  sum += int(num[i])
  
print(sum)

# 이거 어렵게 낼려면 더 어렵게 낼 수 있을거 같은데
# 브론즈 4 문제라 그런지 트릭키하진 않았다
# 단순하게 품