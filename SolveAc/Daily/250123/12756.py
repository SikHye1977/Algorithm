#[BOJ] 고급 여관 / Bronze 3 / 10m
A, h1 = map(int, input().split())
B, h2 = map(int, input().split())

x, y = h1//B + (1 if h1%B else 0), h2//A + (1 if h2%A else 0)

if x == y:
    print("DRAW")
elif x > y:
    print("PLAYER A")
else:
    print("PLAYER B")
    
# 간단한 몸풀기 문제