# [프로그래머스] 약수의 합 / Lv.1 / 5m
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            answer += i
    
    return answer

# 약수의 개수와 덧셈 문제랑 비슷한 문제
# 약수 계산의 기본