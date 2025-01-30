# 바이러스 / Silver 3 / 50m
N = int(input())

M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
  node, edge = map(int, input().split())
  graph[node].append(edge)
  graph[edge].append(node)

visited=[0]*(N+1)

def dfs(v):
  visited[v]=1
  for i in graph[v]:
    if(visited[i] == 0):
      dfs(i)

dfs(1)
print(sum(visited) - 1)

# 그래프 탐색 알고리즘
# 인접리스트를 생성해서 DFS, 혹은 BFS로 그래프를 탐색한다.
# 재귀 함수를 이용하여, v번째 컴퓨터에 연결된 컴퓨터를 확인한다.
# visitied 배열을 통해 방문한 컴퓨터인지 아닌지 검사한다.
# 방문하지 않은 컴퓨터이면 재귀로 해당 컴퓨터를 방문하고, 반복한다.
# 참고 자료 : https://bio-info.tistory.com/152