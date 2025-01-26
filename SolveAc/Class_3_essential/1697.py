# [BOJ] 숨바꼭질 / Silver 1 /
import sys
from collections import deque

def bfs(v):
  queue = deque([v])
  while queue:
    v = queue.popleft()
    if(v == K):
      return visited[v]
    for i in (v - 1, v + 1, v * 2):
      if(0 <= i < max and not visited[i]):
        visited[i] = visited[v] + 1
        queue.append(i)

N, K = map(int,sys.stdin.readline().split())
max = 100001
visited = [False] * (max)
print(bfs(N))
