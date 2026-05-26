# [프로그래머스] 문자열 밀기 / Lv.0 / 30m
def solution(A, B):
    answer = 0
    if (A == B):
        answer = 0
    else:
        A_ = []
        B_ = []
        for i in A:
            A_.append(i)
        for i in B:
            B_.append(i)
        
        count = 1
        iterate = len(A_) - 1
        for i in range(iterate):
            temp = []
            cur = A_.pop()
            temp.append(cur)
            for j in A_:
                temp.append(j)
            A_ = temp
            if (temp == B_):
                break
            else:
                count += 1
        if(count == len(A)):
            answer = -1
        else:
            answer = count
            
    return answer

# 문자열을 밀 필요가 없는 경우를 맨 마지막에 처리해줬다가 늦었다.
# str을 list로 바꿔서 풀었는데
# 슬라이싱이 내가 생각한대로 가능하면
# 굳이 이렇게 복잡하게 안풀어도 될 듯
# 슬라이싱을 공부하자...

# def solution(A, B):
#     A_ = []
#     B_ = []
    
#     for i in range(len(A)):
#         A_.append(A[i])
#         B_.append(B[i])
        
    
#     check = []
#     count = 1
#     for i in range(len(A_) - 1):
#         cur = A_.pop()
#         check.append(cur)
#         for i in A_:
#             check.append(i)
#         if(check == B_):
#             break
#         else:
#             cur = ""
#             count += 1
            
#     if(A == B):
#         answer = 0
#     elif count == len(B_):
#         answer = -1
#     else:
#         answer = count
        
#     return answer