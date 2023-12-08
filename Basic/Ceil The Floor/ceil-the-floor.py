#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # code here
    a=[]
    if x in arr:
        a.append(x)
    elif x<min(arr):
        a.append(-1)
    else:
        res=[]
        for i in arr:
            if i<x:
                res.append(i)
        a.append(max(res))
    if x in arr:
        a.append(x)
    elif x>max(arr):
        a.append(-1)
    else:
        res=[]
        for i in arr:
            if i>x:
                res.append(i)
        a.append(min(res))
    return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends