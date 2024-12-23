N = int(input())

arr = []
for i in range(1, N):
  sum = 0
  init = i
  while init > 0:
    sum = sum + (init % 10)
    init //= 10
  if(sum + i == N):
    arr.append(i)

if arr:
  print(arr[0])
else:
  print(0)
  
# while문 안에서 자연수의 각 자릿수를 쪼갬
# 임시변수 init을 이요해서 i값을 유지하고, 합을 계산해서 조건에 맞는지 판단
# indexerror 방지를 위해 arr가 비어있을 경우에 0을 출력

#map을 이용한 풀이도 있음
# N = int(input())

# # 가장 작은 생성자를 찾으면 바로 출력
# for i in range(1, N):
#     sum_digits = sum(map(int, str(i)))  # 각 자리수의 합 계산
#     if i + sum_digits == N:
#         print(i)
#         break
# else:
#     # 생성자가 없는 경우
#     print(0)
