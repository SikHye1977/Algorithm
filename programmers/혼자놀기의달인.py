# [프로그래머스] 혼자놀기의달인 / Lv.1 / 40m
def solution(cards):
    list = []
    
    i = 0
    while i < len(cards):
        if(cards[i] == 0):
            i += 1
            continue

        count = 0
        current = i
        while True:
            if(cards[current] == 0):
                break
            next_idx = cards[current] - 1
            count += 1
            cards[current] = 0
            current = next_idx
        list.append(count)
        i += 1
    
    list.sort(reverse = True)
    
    if len(list) < 2:
        return 0

    answer = list[0] * list[1]
    return answer

# 중첩 while로 풀었다
# 마지막에 list를 내림차순으로 정렬해서
# 가장 큰 두 점수를 곱해서 answer를 냈다.
# continue를 까먹지 말자!
# 처음엔 아래처럼 풀어서 틀렸었다.
# 그룹이 3개 이상 나올수 있다는걸 생각하지 않았음
# def solution(cards):
#     list1 = []
#     list2 = []
#     i = 0
#     while True:
#         if(cards[i] == 0):
#             break
#         next_idx = cards[i] - 1
#         list1.append(next_idx + 1)
#         cards[i] = 0
#         i = next_idx
    
#     j = 0
#     for i in cards:
#         if(i == 0):
#             j += 1
#         else:
#             break
    
#     while True:
#         if(cards[j] == 0):
#             break
#         next_idx = cards[j] - 1
#         list2.append(next_idx + 1)
#         cards[j] = 0
#         j = next_idx
        
        
#     print(list1)   
#     print(list2)
    
    
#     answer = len(list1) * len(list2)
#     return answer