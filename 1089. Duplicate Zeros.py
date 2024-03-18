arr = [1,0,2,3,0,4,5,0]
arr2 =[]
for i in range(0,len(arr)-1):
    if(arr[i] == 0):
        arr2.append(arr[i])
        arr2.append(0)
    else:
        arr2.append(arr[i])
del arr2[len(arr):]
arr.clear()
for i in arr2:
    arr.append(i)
print(arr)