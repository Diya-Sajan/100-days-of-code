#User function Template for python3

def max_sum(a,n):
    inisum = sum(a)
    sumone = 0

    
    for i in range(n):
        sumone += i*a[i]
        
    maxi = sumone
    for i in range(1,n):
        cursum = sumone + inisum - n*a[n-i]
        sumone = cursum
        #print(sumone, inisum , cursum)
        if cursum > maxi:
            maxi = max ( maxi, cursum)

    
    return maxi
    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends