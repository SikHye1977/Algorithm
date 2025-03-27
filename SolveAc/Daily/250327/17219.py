# [BOJ] 비밀번호 찾기 / Silver 4 / 15m
import sys

N,M = map(int,sys.stdin.readline().split())

arr = dict()

for i in range(N):
  admin, password = map(str, sys.stdin.readline().split())
  arr[admin] = password

for i in range(M):
  temp = input()
  if temp in arr:
    print(arr[temp])