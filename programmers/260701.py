# [프로그래머스] 연속된 부분 수열의 합 / Lv.2 / 30m
def solution(sequence, k):
    prefix = [0] * 1000001
    start, end = 1, 1
    prefix_range = []
    
    for i in range(len(sequence)):
        prefix[i + 1] = prefix[i] + sequence[i]
    
    while end <= len(sequence):
        prefix_sum = prefix[end] - prefix[start - 1]
        
        if(prefix_sum == k):
            prefix_range.append([start - 1,end - 1])
            start += 1
            
        elif(prefix_sum < k):
            end += 1
            
        else:
            start += 1
        
    prefix_range.sort(key = lambda x: x[1] - x[0])
    
    answer = prefix_range[0]
    return answer

# 누적합 개념을 사용하는 문제
# 먼저 누적합 배열을 만들고
# prefix[end] - prefix[start - 1]로 구간합을 구한다

# 반복문을 돌면서 (탈출 조건은 end 포인터가 sequence 배열을 벗어났을 때)
# 구간합을 구하고, k와 같으면 list에 추가한다

# 구간합이 k보다 작으면 end 포인터를 증가시키고
# k보다 작으면 start 포인터를 증가시킨다

# start가 end값 보다 커지더라도, 다음 루프에서 같은 위치로 맞춰짐