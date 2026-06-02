# [프로그래머스] 전력망을 둘로 나누기 / Lv.3 / 2h
from collections import deque

def solution(n, s, a, b, fares):
    INF = float("inf")
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for u,v,weight in fares:
        graph[u][v] = weight
        graph[v][u] = weight
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    min_fare = INF
    
    for x in range(1, n + 1):
        fare = graph[s][x] + graph[x][a] + graph[x][b]
        
        if fare < min_fare:
            min_fare = fare
    
    answer = min_fare
    return answer

# 간선에 가중치가 있는 트리를 그래프로 만드는게 헷갈렸다.
# 이후 각 구간별 최단거리를 찾기 위해
# 플로이드 워샬 알고리즘으로 각 간선을 업데이트 한다.
# 이후 합승거리 (S -> X)와 각자 집으로 가는 거리 (x -> A) (x -> B)의 최솟값을 구한다.
# 이때 X는 어느 위치가 될 지 모르므로 완전탐색을 사용한다.
# 각 노드를 합승목적지로 해서 최소가 되는 거리를 구한다.
