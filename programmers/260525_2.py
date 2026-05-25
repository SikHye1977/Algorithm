# [프로그래머스] 종이 자르기 / Lv.0 / 1m
def solution(M, N):
    area = M * N
    if (area == 1):
        answer = 0
    else:
        answer = area - 1
    return answer

# 진짜 1분만에 풀었다
# 가로 세로를 곱해서 전체 면적을 구하고 -1 해주면 된다.