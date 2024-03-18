from math import pow
nums = [-4,-1,0,3,10]
for i in range(0,len(nums)-1):
    a = pow(nums[i],2)
    nums[i]=int(a)

print(sorted(nums))