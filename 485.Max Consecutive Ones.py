nums =[1,1,0,1,1,1]
token = 0
result = 0
for i in range(0,len(nums)):
    if(nums[i]==1):
        token+=1
        if(token>result):
            result = token
    else:
        if(token>result):
            result = token
        token = 0
print(result)