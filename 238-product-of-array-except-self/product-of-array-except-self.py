class Solution(object):
    def productExceptSelf(self, nums):
        l=[]
        pro=1
        count=0
        for i in range (0,len(nums)):
            if (nums[i]!=0):
                pro = pro * nums[i]
            else: 
                count+=1

        for j in range(0,len(nums)):
            if (count==0):
                num = pro/nums[j]    
            
            elif (count==1):
                if(nums[j] == 0):
                    num = pro
                else: 
                    num = 0   
            elif(count>1):
                num = 0
            
            l.append(num)
        return l
