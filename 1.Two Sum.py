class Solution(object):
    def twoSum(nums, target):
        for i in range(0,len(nums)-1):
            for j in range(1,len(nums)):
                if(nums[i]+nums[j]==target and i!=j):
                    return(i,j)
nums =[2,5,5,11]
target = 10
print(Solution.twoSum(nums,target))