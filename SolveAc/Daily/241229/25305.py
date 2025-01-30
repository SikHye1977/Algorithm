N, K = list(map(int,input().split()))

arr = []
arr = list(map(int,input().split()))
arr.sort(reverse=True)

print(arr[K-1])

#몸풀기