# [프로그래머스] 약수의 개수와 덧셈 / Lv.1 / 20m
def solution(left, right):
    answer = 0
    for i in range(left,right + 1,1):
        count = 0
        for j in range(1, i + 1):
            if(i % j == 0):
                count += 1
        if (count % 2 == 0):
            answer += i
        else:
            answer -= i
    
    return answer

# 중첩 반복문으로 푸는 간단한 문제
# 주어진 숫자마다 약수의 개수를 구함
# 약수의 갯수가 짝수면 정답에 더하고
# 아니면 뺌
# 시간복잡도 때문에 틀릴줄 알았는데 조건이 널널했나봄
# 다음에는 좀 더 줄일 수 있는 방법을 찾아봐야 할 것 같음