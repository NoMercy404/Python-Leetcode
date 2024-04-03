class Solution(object):
    def duplicateZeros(self, arr):
        IsZero=1
        for a in arr:
            if(a==0):
                IsZero+=1
        if(IsZero==1):
            return False
        else:
            arr2 =[]
            for i in range(0,len(arr)-1):
                if(arr[i] == 0):
                    arr2.append(arr[i])
                    arr2.append(0)
                else:
                    arr2.append(arr[i])
            del arr2[len(arr):]
            del arr[:]
        for i in arr2:
            arr.append(i)
        return arr
