# [프로그래머스] 유연근무제 / Lv.1 / 1h
def solution(schedules, timelogs, startday):
    admit = []
    
    for i in schedules:
        hour = i // 100
        minute = i % 100
        minute += 10
        
        if (minute >= 60):
            hour += 1
            minute -= 60
        
        temp = hour * 100 + minute
        admit.append(temp)
    
    row = 0
    count = 0
    for i in admit:
        start = startday
        gift = True
        for j in timelogs[row]:
            current = (start - 1) % 7 + 1
            if (current == 6 or current == 7):
                start += 1
                continue
                # print("holiday")
            else:
                if (i < j):
                    gift = False
                    break
            start += 1
        # print()
        if(gift == True):
            count += 1
        row += 1
    answer = count
    return answer

# 먼저 시간을 1000자리수로 구해준다.
# 이후 루프를 돌면서
# 직원이 출근 희망하는 시각이 실제 출근시간보다 작으면 넘어가고
# 실제 출근시간이 희망시간보다 늦었으면 flag를 False로 바꾼다.
# 처음에 Conitnue를 잘못써서 틀렸었다.
# 1000자리 숫자로 시간 변경하는것도 잘못 처리했었다.