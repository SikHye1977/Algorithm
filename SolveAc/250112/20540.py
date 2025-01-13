# 연길이의 이상형 /Bronze 3 /5m
s = input()
li = ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']
for c in s:
    li.remove(c)
res = ''.join(li)
print(res)

# 간단한 문제