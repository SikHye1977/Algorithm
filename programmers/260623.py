# [프로그래머스] 선인장 숨기기 / Lv.2 / 3h
def solution(m, n, h, w, drops):
    answer = []
    def check(k):
        grid = [[0] * n for _ in range(m)]
        for i in range(k):
            row, col = drops[i]
            grid[row][col] = 1
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = grid[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        for r in range(m - h + 1):
            for c in range(n - w + 1):
                area = prefix[r+h][c+w] - prefix[r][c+w] - prefix[r+h][c] + prefix[r][c]
                
                if area == 0:
                    return [r,c]
        return None
    
    left = 0
    right = len(drops)
    
    while left <= right:
        mid = (left + right) // 2
        
        result = check(mid)
        
        if result is not None:
            answer = result
            left = mid + 1
        else:
            right = mid - 1
    
    return answer

# 누적합과 이분탐색을 이용하는 문제
# 이분탐색을 통해 drops 범위의 중간부터 탐색해간다.
# 가장 많은 비가 떨어져도 가장 안전한 구역을 찾기 위해서임.
# 내부에서는 구간합 연산을 이용한다.
# 먼저 비가 떨어지는 위치를 grid로 구하고
# prefix로 해당 구간의 구간합을 구한다.
# 가장 적은 값이 나오는 r,c가 정답이 된다

# 누적합 공부를 더 해야 할 듯