# 나머지 / Bronze 2 / 25m
arr = []
N = int(input())
arr.append(N)

for i in range(9):
  N = int(input())
  check = N % 42
  count = 0
  for j in range(len(arr)):
    if(arr[j] % 42 != check):
      count += 1
  if(count == len(arr)):
    arr.append(N)
        
print(len(arr))

# 조금 생각한 문제
# 첫번째 입력값은 배열에 그대로 입력
# 두번째 입력값 부터 기존의 배열에 입력된 값과 비교
# 입력받은 값의 나머지가 기존 배열의 나머지와 다르다면 count를 1씩 증가
# count가 배열의 길이와 같다면 같은 값이 없다는 뜻이므로 배열에 추가
# 배열의 길이를 출력