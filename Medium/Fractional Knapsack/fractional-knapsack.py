#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    def fractionalknapsack(self, W,arr,n):
        c=0
        k=0
        arr.sort(key=lambda x:x.value / x.weight, reverse = True)       
        for i in arr:
            if c==W:
                break
            if (c+i.weight)<=W:
                c+=i.weight
                k+=i.value          
            else:
                k += i.value * ((W - c) / i.weight)
                #k+=c
                break
        return k


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends