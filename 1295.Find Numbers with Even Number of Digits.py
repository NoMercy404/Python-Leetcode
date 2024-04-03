class Solution(object):
    def findNumbers(self, nums):
        even = 0
        for i in nums:
            digits = 0
            while (i >= 1):
                digits += 1
                i = i / 10
            if (digits % 2 == 0):
                even += 1
        return even