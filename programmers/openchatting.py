# [프로그래머스] 오픈채팅방 / ? / 1h
def solution(record):
    answer = []
    changed = {}
    
    for i in record[::-1]:
        msg = i.split(" ")
        if msg[0] in ["Enter", "Change"]:
            if msg[1] not in changed:
                changed[msg[1]] = msg[2]
    
    for i in record:
        msg = i.split()
        if msg[0] == "Enter":
            if msg[1] in changed:
                final_msg = changed[msg[1]] + "님이 들어왔습니다."
                answer.append(final_msg)
        elif msg[0] == "Leave":
            if msg[1] in changed:
                final_msg = changed[msg[1]] + "님이 나갔습니다."
                answer.append(final_msg)
            
        
    return answer

# 처음에 배열만 이용해서 아래처럼 풀었더니 시간초과 나고, 75점 나왔다
# Dictionary를 활용하자!
# 입력 레코드를 역순으로 돌면서, 가장 마지막의 상태값을 uuid를 key로 dictionary에 저장
# record를 처음부터 돌면서, dictionary key 값(uuid)와 record에 있는 id를 비교
# 변경 내역이 있으면 이름을 덮어 씌움

# def solution(record):
#     answer = []
#     changed = []
    
#     for i in record[::-1]:
#         flag = True
#         msg = i.split(" ")
#         if msg[0] != "Leave":
#             for j in changed:
#                 if j[0] == msg[1]:
#                     flag = False
#             if (flag == True):
#                 change_rec = [msg[1], msg[2]]
#                 changed.append(change_rec)
    
#     print(changed)
    
#     for i in record:
#         msg = i.split(" ")
#         if msg[0] == "Enter":
#             for i in changed:
#                 if(i[0] == msg[1]):
#                     msg[2] = i[1]
#             final_msg = msg[2] + "님이 들어왔습니다." 
#             answer.append(final_msg)
#         elif msg[0] == "Leave":
#             name = ""
#             for j in changed:
#                 if j[0] == msg[1]:
#                     name = j[1]
#             final_msg = name + "님이 나갔습니다."
#             answer.append(final_msg)
        
#     return answer