for i in range(len(arr)):
  target = arr[i]
  for j in range(len(set_arr)):
    if(target == set_arr[i]):
      ans.append(i)
      break

print(ans)