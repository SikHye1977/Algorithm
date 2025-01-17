# 유기농 배추 / Silver 2 / 1h
T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
  queue = [(x,y)]
  graph[x][y] = 0
  
  while queue:
    x,y = queue.pop(0)
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if(nx < 0) or (nx >= M) or (ny < 0) or (ny >= N):
        continue
      if graph[nx][ny] == 1:
        queue.append((nx,ny))
        graph[nx][ny] = 0

for i in range(T):
  M, N, K = map(int,input().split())
  graph = [[0] * N for _ in range(M)]
  count = 0
  
  for j in range(K):
    X,Y = map(int,input().split())
    graph[X][Y] = 1
    
  for a in range(M):
    for b in range(N):
      if(graph[a][b] == 1):
        BFS(a,b)
        count += 1
  print(count)
  
# 그래프와 너비우선 탐색을 이용하는 문제
# 아이디어는 다음과 같다
# 1. 너비우선 탐색으로 인접한 1을 0으로 바꾼다
# 2. 그래프(행렬)을 만들어 graph[x][y]=1인 경우 BFS로 실행하고, 한번 실행할 때 마다 count를 1씩 증가시킨다
# 3. BFS 함수가 인접한 모든 1을 0으로 바꾸므로 연결된 하나의 블럭 개수를 구할 수 있다.
# 참고 https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1012%EB%B2%88-%EC%9C%A0%EA%B8%B0%EB%86%8D-%EB%B0%B0%EC%B6%94