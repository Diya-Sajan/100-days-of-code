#User function Template for python3
class Solution:
    def longSubarrWthSumDivByK (self,arr,  n, K) :
        remainder_dict = {0: -1}
        max_length = 0
        current_sum = 0
 
        for i in range(n):
            current_sum += arr[i]
            remainder = current_sum % K
 
            # If the remainder is negative, add K to make it positive
            if remainder < 0:
                remainder += K
 
            if remainder in remainder_dict:
                # If the same remainder is found, update the maximum length
                max_length = max(max_length, i - remainder_dict[remainder])
            else:
                # If the remainder is not in the dictionary, add it with its current index
                remainder_dict[remainder] = i
 
        return max_length




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends