# [프로그래머스] 다음에 올 숫자 / Lv.1 / 30m
def solution(wallpaper):
    answer = []
    
    lux_arr = []
    luy_arr = []
    rdx_arr = []
    rdy_arr = []
    
    lux = 0
    luy = 0
    rdx = 1
    rdy = 1
    
    for i in wallpaper:
        for j in i:
            if(j == "#"):
                lux_arr.append(lux)
                luy_arr.append(luy)
                rdx_arr.append(rdx)
                rdy_arr.append(rdy)
            lux += 1
            rdx += 1
        lux = 0
        luy += 1
        rdx = 1
        rdy += 1
    
    
    answer.append(min(luy_arr))
    answer.append(min(lux_arr))
    answer.append(max(rdy_arr))
    answer.append(max(rdx_arr))
    
        
    return answer

# 파일을 하나하나씩 찾아서
# 각 파일의 왼쪽 위, 오른쪽 아래 좌표를 저장
# 저장된 좌표들에서
# 왼쪽 위 값은 최소로
# 오른쪽 아래 값은 최대가 되는 값을 찾아서
# 정답 배열에 저장