nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
newArray=[]
for a in range(0,m):
    newArray.append(nums1[a])
for b in range(0,n):
    newArray.append(nums2[b])
newArray.sort()
del nums1[:]
for i in newArray:
    nums1.append(i)
print(nums1)