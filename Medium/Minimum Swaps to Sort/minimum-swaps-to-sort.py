

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
        numIndx = [[nums[i],i] for i in range(len(nums))]
        numIndx.sort()
        i=0
        count = 0
        while i<len(nums):
            j = numIndx[i][1]
            if j==i:
                i+=1
                continue
            numIndx[i], numIndx[j] = numIndx[j], numIndx[i]
            count+=1
        return count


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends