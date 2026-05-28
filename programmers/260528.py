# [프로그래머스] 게임 맵 최단거리 / Lv.2 / 1h

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                queue.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
            
    answer = maps[n-1][m-1]
    
    if answer == 1:
        return -1
    else:
        return answer
    
# 이전에 풀었던 그래프 문제를 생각하고
# 인접행렬부터 만들려고 했으나, 그래프가 아닌 2차원 배열 형태여서 접근법을 바꿨다.
# 캐릭터가 움직일 수 있는 방향은 상하좌우 4방향이다
# 그래서 dx, dy 배열을 만든다. (좌우하상)
# 2차원 배열을 왼쪽 위(문제에서 고정됨)에서 부터 4방향으로 한 칸 씩 이동시켜 본다.
# 맵을 넘어가거나, 벽(0)으로 표시된 부분은 continue로 넘어간다
# 갈 수 있는 경우 해당 위치의 값을 +1 하면서 나아간다
# 아직 안 갔지만 갈 수 있는 (1인 경우) 경우에만 갈 수 있으므로 최단거리가 보장된다.
# 탐색이 끝난후 상대진영의 값을 체크해서 출력한다.
# 만약 벽으로 가로막혀있으면 1이기 때문에, -1을 출력한다.