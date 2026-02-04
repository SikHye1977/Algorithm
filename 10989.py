# 수 정렬하기 3 / Bronze 1 / 20m
import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(N):
  num = int(sys.stdin.readline())
  count[num] += 1

for i in range(10001):
  if count[i] != 0:
    for _ in range(count[i]):
      sys.stdout.write(str(i) + '\n')

# 그냥 리스트에 입력값을 저장하니 메모리 초과가 떴음
# 문제 조건중 입력값의 범위는 0 ~ 10000 까지임
# 10000개의 0이 있는 리스트 count 생성
# 등장 횟수만 체크
# 등장 횟수만큼 출력