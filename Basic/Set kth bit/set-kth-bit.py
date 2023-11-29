#User function Template for python3
class Solution:
	def setKthBit(self, N, K):
        num = bin(N)[2:]
        k=len(num)-(K+1)
        res = num[:k]+'1'+num[k+1:]
        return int(res,2)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = input().split()
		N = int(N)
		K = int(K)
		ob = Solution()
		ans = ob.setKthBit(N,K)
		print(ans)




# } Driver Code Ends