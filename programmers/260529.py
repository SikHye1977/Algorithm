# [프로그래머스] 하노이의 탑 / Lv.2 / 1h
def solution(n):
    answer = []
    
    def hanoi(num, start, end, via):
        if(num == 1):
            answer.append([start,end])
            return
        
        hanoi(num - 1, start, via, end)
        answer.append([start,end])
        hanoi(num - 1, via, end, start)
        

    hanoi(n,1,3,2)
    return answer

# 역사와 전통의 재귀함수 문재
# 맨 밑에 있는 원통은 항상 start에서 end로 이동한다.
# 아래에서 부터 위로 역순으로 생각해야 함
#
# n-1번 원통은 항상 start에서 via로 옮겨져야 함
# 맨 밑의 원통은 항상 start에서 end로
# n-1개의 원통을 end 위에 쌓으면 끝