# [프로그래머스] 서버 증설 횟수 / Lv.2 / 1h 30m
def solution(players, m, k):
    count = 0
    n = 1
    expansion = []
    
    for i in range(len(players)):
        new_expansion = [x - 1 for x in expansion if x - 1 > 0]
        n -= (len(expansion) - len(new_expansion))
        expansion = new_expansion
        while (players[i] >= n*m):
            n += 1
            count += 1
            expansion.append(k)
            print(i, n, count)
    
    print(count)
    answer = count
    return answer

# 입력된 배열만큼 반복
# 새로 증설된 서버는 k시간만큼 유지되고 철수 됨
# 증설된 서버 각각 타이머를 적용시키기 위해 배열 생성
# k를 새 인덱스에 삽입 한 뒤, 삽입된 때 부터 각 인덱스를 1씩 감소
# 이용자 수가 현재 서버 수 * 서버당 수용 인원보다 많으면
# n을 하나씩 증가 시켜서 총 서버 몇개가 필요한지 판단.

# 리스트 컴프리헨션이라는 걸 알게 됨
