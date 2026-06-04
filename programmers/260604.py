# [프로그래머스] 중요한 단어를 스포 방지 / Lv.1 / 2h
def solution(message, spoiler_ranges):
    answer = 0
    
    token = []
    current = 0
    
    for word in message.split(" "):
        start = current
        end = current + len(word) - 1
        token.append((word, start, end))
        current += len(word) + 1
    
    spoiler = []
    non_spoiler = set()
    
    for word, start, end in token:
        is_spoiler = False
        
        for r_start, r_end in spoiler_ranges:
            if max(start, r_start) <= min(end, r_end):
                is_spoiler = True
                break
                
        if is_spoiler:
            spoiler.append(word)
        else:
            non_spoiler.add(word)
        
    important = set()
    
    for word in spoiler:
        if word not in non_spoiler and word not in important:
            important.add(word)
            answer += 1
            
    
    return answer

# 단어를 하나하나 분리하고, 시작 idx와 끝 idx도 같이 저장한다.
# 만들어진 token 리스트를 돌면서, 스포일러 방지 영역에 단어가 있는지 확인하고, 스포일러 방지 단어면 sopiler 리스트에 추가한다.
# 스포일러 방지 단어가 아니면 non_spoiler에 추가
# 스포일러 방지 단어를 돌면서, 아래 조건에 맞게 탐색한다.
# 현재 단어가 스포일러 방지 단어이면서, 이미 보인 단어가 아니면 answer + 1
# 이미 드러난 단어는 important에 추가

# extend 함수는 append와 다르게, 붙일거 각각을 분리해서 기능 적용이 가능하다.

# 처음에 아래와 같이 풀었다가 틀렸다(65점 나옴)
# 구간에서 단어를 찾는게 아니라, 단어가 구간에 속하는지 찾아야 한다.
# 한 단어에 스포일러 방지 영역이 두번 찍혀있을 수도 있기 때문.

# def solution(message, spoiler_ranges):
#     answer = 0
#     tokens = message.split(" ")
#     spoiler = []
    
#     for i in spoiler_ranges:
#         temp_start = i[0]
#         temp_end = i[1]
#         word = ""
#         for j in range(i[0],-1,-1):
#             if(message[j] == " "):
#                 break
#             temp_start = j
#         for l in range(i[1],len(message),1):
#             if(message[l] == " "):
#                 break   
#             else:
#                 temp_end += 1
#         word = message[temp_start:temp_end]
#         spoiler.extend(word.split())
    
#     print(spoiler)
    
#     unique_spoilers = set(spoiler)
    
#     for word in unique_spoilers:
#         total_count = tokens.count(word) 
        
#         hidden_count = spoiler.count(word)
        
#         if total_count == hidden_count:
#             answer += 1
    
    
#     return answer