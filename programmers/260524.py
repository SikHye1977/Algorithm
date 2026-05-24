# [프로그래머스] 다음에 올 숫자 / Lv.0 / 30h
def solution(common):
    list = []
    end = len(common)
    for i in range(end - 1):
        diff = common[i + 1] - common[i]
        list.append(diff)
    
    check = True
    for i in range(len(list) - 1):
        if(list[i] != list[i + 1]):
            check = False
            break
    
    list_end = len(list)
    if(check == True):
        answer = common[end - 1] + list[list_end - 1]
    else:
        ratio = common[1] // common[0]
        answer = common[end - 1] * ratio

    return answer

# 등차/등비 수열 결정하는 방식이 처음에 좀 헷갈렸다
# 그리고 처음에 ratio 없이 
# common[end - 1] * list[list_end - 1]
# 위와 같이 등비수열 구해서 틀렸었다
# list[0]에 항상 공비가 저장되는게 아니기 때문
# 그래서 ratio를 따로 구해줬다.