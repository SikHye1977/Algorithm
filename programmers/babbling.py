# [프로그래머스] 옹알이 / Lv.0 / 20m
def solution(babbling):
    check = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for i in babbling:
        flag = False
        bab = ""
        for j in i:
            bab += j
            if(bab in check):
                print(bab)
                flag = True
                bab = ""
            else:
                flag = False
        if(flag == True):
            count += 1

    return count

# 처음에 각 옹알이를 어떻게 잘라서 비교할지 고민했다
# 그냥 char하나하나 잘라서 붙이다가 check에 있는 단어가 나오면 count + 1해주는 식으로 풀었다
# 코딩테스트 입문 문제라 그런지 어렵진 않았음