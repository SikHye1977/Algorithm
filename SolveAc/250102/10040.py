N, M = map(int,input().split())

game = []
judge = []
ans = [0] * N

for i in range(N):
  x = int(input())
  game.append(x)
for i in range(M):
  x = int(input())
  judge.append(x)

for i in range(M):
  for j in range(N):
    if(game[j] <= judge[i]):
      ans[j] += 1
      break

print(ans.index(max(ans)) + 1)

# 각 게임과 심사위원의 비용을 배열에 저장
# 정답 배열은 게임수만큼으로 초기화
# 2중 반복문을 돌면서 기준을 만족하는 인덱스에 1씩 더함
# 가장 큰 값이 나온 index + 1을 해서 해당 게임의 위치를 알아냄
# 순서 정렬때문에 고민했는데 그럴 필요가 없었음
# 45분 걸림

# https://woody0808.tistory.com/367