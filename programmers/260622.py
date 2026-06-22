# [프로그래머스] [PCCP 기출문제] 1번 / 붕대 감기 / Lv.1 / 45m
def solution(bandage, health, attacks):
    length = len(attacks)
    last = attacks[length - 1][0]
    
    HP = health
    sequence = 0
    count = 0
    for i in range(1, last + 1):
        
        if(i == attacks[count][0]):
            HP -= attacks[count][1]
            count += 1
            sequence = 0
        else:
            HP += bandage[1]
            HP = min(health, HP)
            sequence += 1
        
        if (HP <= 0):
            HP = -1
            break
        
        if(sequence == bandage[0]):
            HP += bandage[2]
            HP = min(health, HP)
            sequence = 0
    
    answer = HP
    return answer

# 조건에 맞춰 작성하면 됨
# 1초부터 MAX까지 반복하면서
# 공격 받는 타이밍에 HP 감소
# 회복 시에는 최대 체력을 넘지 않게 HP = min(health, HP) 연산으로 조정