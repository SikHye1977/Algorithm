# 알람시계 / Bronze 3 / 5m
H, M = map(int,input().split())

if(M < 45):
  M = M + 60
  H = H - 1
  #0일 때
  if(H < 0):
    H = 23

print(H, M-45)

# 간단한 수학 구현
# 분 값이 45보다 작으면 60을 더해준 후 빼면 된다.
# 시간 값이 0보다 작으면 23부터 시작하게 만들면 된다.