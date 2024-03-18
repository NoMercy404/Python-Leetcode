class Solution(object):
    def myPow(self, x, n):
        a=x
        if (n==0):
            return 1
        elif (n<0):
            x=1/x
            n*=-1
            for i in range(1,n):
                x*=x
        elif (n>0):
            for i in range(1,n+1):
                x*=a
        return x

print(Solution.myPow((),34.00515,-3))