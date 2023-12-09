#User function Template for python3

class Solution:
    def sortIt(self, arr, n):
        arr[:] = sorted(arr)
        ar2=[]
        for i in range(n-1,-1,-1):
            if arr[i] %2!=0:
                ar2.append(arr[i])
        for i in range(0,n):
            if arr[i] %2==0:
                ar2.append(arr[i])
            
        arr[:]=ar2
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortIt(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends