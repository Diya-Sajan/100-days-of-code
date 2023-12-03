#User function Template for python3

class Solution:
    def lastIndex(self, s):
        x = s[::-1]
        for i in range(0,len(x)):
            if x[i] =="1":
                return len(s)-i-1
        return -1    
            
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends