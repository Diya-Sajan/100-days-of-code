#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		if k not in arr:
		    return -1
		return arr.index(k)
		


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends