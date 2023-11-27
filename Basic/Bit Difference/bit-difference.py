#User function Template for python3

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        
        A = [*bin(a)][2:]
        B = [*bin(b)][2:]
    
        if len(A)> len(B):
            x = len(A) - len(B)
            B = ['0']*x + B
        elif len(A)< len(B):
            x = len(B) - len(A)
            A = ['0']*x + A
        count = 0
        for i in range(0,len(A)):
            if A[i]!=B[i]:
                count+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        ab=[int(x) for x in input().strip().split()]
        a=ab[0]
        b=ab[1]
        ob=Solution()
        print(ob.countBitsFlip(a,b))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends