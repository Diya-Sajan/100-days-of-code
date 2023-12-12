#User function Template for python3
class Solution:

	def maxRepeating(self,arr, n, k):
		f = {}
		max = 0
		for i in arr:
		    if i not in f:
		        f[i] = 1
		    else:
		        f[i] +=1
		for i in f:
		    if f[i] > max:
		        max = f[i]
		        val = i
		    elif f[i] == max:
		        if i<val:
		            val = i
		return val


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxRepeating(arr, n, k)
        print(ans)
        tc -= 1


# } Driver Code Ends