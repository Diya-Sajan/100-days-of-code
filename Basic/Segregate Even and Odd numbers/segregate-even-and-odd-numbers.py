#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
		ar2 = sorted(arr)
		arr.clear()
		for i in ar2:
		    if i%2 == 0:
		        arr.append(i)
		for i in ar2:
		    if i%2!=0:
		        arr.append(i)
		
		return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends