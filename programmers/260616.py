# [프로그래머스] 지폐접기/ Lv.1 / 30m
def solution(wallet, bill):
    count = 0

    while True:
        if wallet[0] >= bill[0] and wallet[1] >= bill[1] :
            break
        elif wallet[1] >= bill[0] and wallet[0] >= bill[1]:
            break
        else:
            fold = max(bill[0], bill[1])
            if fold == bill[0]:
                bill[0] = bill[0] // 2
            else:
                bill[1] = bill[1] // 2
            count += 1
    
    answer = count
    return answer

# 그냥 문제에 적혀있는데로 풀면 되는 문제
# 어려울건 없었다.