# [프로그래머스] 연속된 수의 합 / Lv.0 / 50m
def solution(num, total):
    mid = total // num
    
    start = mid - ((num - 1) // 2)
    
    answer = []
    
    for i in range(num):
        answer.append(start)
        start += 1
        
    return answer


# 처음에 아래와 같이 풀어서 70점이 나왔다.
# 양수 범위는 단순 중첩 반복문으로 해결 가능하나
# 음수까지 같이 나오는 문제는 해결이 불가능
# 그래서 주어진 total의 중앙값을 기준으로
# 양 방향으로 찾아나가기로 했다

# def solution(num, total):
#     count = 1
#     while True:
#         answer = []
#         check = 0
#         current = count
#         if (num == total):
#             check = (num // 2) + 1
#             print(check)
#             for i in range(num):
#                 answer.append(check)
#                 check -= 1
#             answer.sort()
#             return answer
#         for i in range(num):
#             check += current
#             answer.append(current)
#             current += 1
    
#         if sum(answer) == total:
#             return answer
#         else:
#             count += 1