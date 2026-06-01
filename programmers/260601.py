# [프로그래머스] 전력망을 둘로 나누기 / Lv.2 / 1h
from collections import deque

def bfs(node, graph, n):
    visited = [False] * (n + 1)
    visited[node] = True
    
    queue = deque([node])
    count = 1
    
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count
    
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = float("inf")
    cnt = []
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        cnt_first = bfs(a, graph, n)
        cnt_second = n - cnt_first
        
        diff = abs(cnt_first - cnt_second)
        distance = min(diff, distance)
        
        graph[a].append(b)
        graph[b].append(a)
    
    answer = distance
    return answer

# 트리를 탐색하는 문제
# 늘 하던것 처럼 트리를 인접행렬형태로 만들고
# 탐색(BFS)를 구현, 경로 갯수를 count 해서 반환한다.
# 노드를 잘랐을 때 차이가 최소가 되어야 하므로
# 간선을 하나씩 잘라가며 차이가 최소인 경우의 count수를 반환한다.