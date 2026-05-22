# [프로그래머스] 가장먼노드 / Lv.3 / 1h
from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    distances = [-1] * (n + 1)
    distances[1] = 0
    
    queue = deque([1])
    while queue:
        current = queue.popleft()
        
        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    max_distance = max(distances)
    answer = distances.count(max_distance)
    
    return answer

# BFS로 거리 카운트 한 후
# 가장 거리가 먼 노드의 개수를 count