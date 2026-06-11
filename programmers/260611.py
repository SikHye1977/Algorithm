# [프로그래머스] 동영상 재생기 / Lv.1 / 1h
def solution(video_len, pos, op_start, op_end, commands):
    temp = pos.split(":") + video_len.split(":") + op_start.split(":") + op_end.split(":")
    current = int(temp[0] + temp[1])
    length = int(temp[2] + temp[3])
    start = int(temp[4] + temp[5])
    end = int(temp[6] + temp[7])
    
    for i in commands:
        if(current >= start and current <= end):
                current = end
        if(i == "next"):
            minute = current // 100
            second = current % 100
            second += 10
            
            if(second >= 60):
                minute += 1
                second -= 60
            
            current = minute * 100 + second
            if(current >= length):
                current = length
            print(current)
        else:
            minute = current // 100
            second = current % 100
            second -= 10
            
            if(second < 0):
                minute -= 1
                second += 60
                
            current = minute * 100 + second
            if(current <= 0):
                current = 0
            
            print(current)
            
        if(current >= start and current <= end):
                current = end
    
    final_pos = current
    answer = f"{final_pos // 100:02d}:{final_pos % 100:02d}"
    return answer

# 로직 자체는 이전에 풀었던 유연 근무제와 큰 차이 없음
# 마지막 출력값을 양식에 맞게 맞추는게 힘들었음
# F-string으로 손쉽게 해결 가능