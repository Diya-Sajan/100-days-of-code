#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		s = set(nuts)
		new = []
		f = {1:'!',2:'#',3:'$',4:'%',5:'&',6:'*',7:'?',8:'@',9:'^' } 
		#f = { '!','#','$','%','&','*','?','@','^' }
		for i in f:
		    if f[i] in s:
		        new.append(f[i])
		        
		nuts[:] = new[:]
		bolts[:] = new[:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends