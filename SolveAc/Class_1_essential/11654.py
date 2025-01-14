# 아스키 코드 / Bronze 5 / 5m
char = input()

arr = [0,1,2,3,4,5,6,7,8,9]

if(char in arr):
  print(chr(char))
else:
  print(ord(char))
  
# 파이썬에서 
# 문자->아스키코드 = ord
# 숫자->아스키코드 = chr