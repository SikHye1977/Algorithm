# [프로그래머스] 택배 상자 꺼내기 / Lv.1 / 2h
def solution(n, w, num):
    row = (num - 1) // w
    if (row % 2 == 0):
        col = (num - 1) % w
    else:
        col = w - 1 - ((num - 1) % w)
        
    top_row = (n - 1) // w
    if (top_row % 2 == 0):
        top_col = (n - 1) % w
    else:
        top_col = w - 1 - ((n - 1) % w)
    
    height = top_row
    
    if (top_row % 2 == 0):
        if (col > top_col):
            height = top_row - 1
    else:
        if (col < top_col):
            height = top_row - 1
            
    answer = height - row + 1
    return answer

# 배열을 만드는게 아니라 수학적 규칙을 이용해서 풀어야 함
# 찾고자 하는 상자의 인덱스를 먼저 구함 
# 높이(row)는 (상자 - 1) // w로 구할 수 있음 (몇층인지)
# 홀수 층이면 역순으로 정렬되어있기 때문에 조건문으로 분기
# 가장 위에 있는 박스의 인덱스도 위와 같은 방법으로 찾음
# 마지막으로 찾고자 하는 상자가 있는 열의 최대 높이를 구함
# 정답 = 최대 높이 - 상자 층 + 1 (목표 상자도 빼야 하므로)

# 처음에 아래와 같이 풀었었다
# 테스트 케이스는 통과했는데 채점에서 30점 나옴
# def solution(n, w, num):
#     box = []
    
#     for i in range(1,n+1,w):
#         temp = []
#         for j in range(i,i + w):
#             if (j > n):
#                 break
#             temp.append(j)
#         box.append(temp)
    
#     height = len(box)
    
#     for i in range(1,height,2):
#         box[i].sort(reverse=True)
    
#     idx_a = 0
#     idx_b = 0
    
#     first_idx = 0
#     for width in box:
#         second_idx = 0
#         for item in width:
#             if(item == num):
#                 idx_a = first_idx
#                 idx_b = second_idx
#                 break
#             second_idx += 1
#         first_idx += 1
    
#     print(idx_a,idx_b)
    
#     answer = height - idx_a
    
#     return answer
