# [프로그래머스] 요격 시스템 / Lv.2 / 1h 30m
def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    
    missile = -1
    
    for s, e in targets:
        if s >= missile:
            answer += 1
            missile = e
    
    return answer

# 그리디 알고리즘으로 푸는 문제
# 막상 풀고 나니까 간단했던 문제
# target을 끝 점을 기준으로 오름차순으로 정렬
# 배열을 순회 하면서 시작점이 현재 미사일 발사 위치보다 크다면 요격 불가능한 것으로 판단
# answer을 +1 한다

# 이전에는 시작점과 끝점 차이를 기준으로 배열 정렬하고, 문제를 풀었다가 틀렸음