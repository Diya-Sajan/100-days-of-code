#User function Template for python3

class Solution:    
    def merge(self,arr,l,h,mid):
        i,j,k=0,0,l
        left=arr[l:mid+1]
        right=arr[mid+1:h+1]
        count=0
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                arr[k]=right[j]
                count+=(len(left)-i)
                j+=1
                k+=1
            else:
                arr[k]=left[i]
                i+=1
                k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return count

    def mergeSort(self,arr,l,h):
        val=0
        if l<h:
            mid=(l+h)//2
            val+=self.mergeSort(arr,l,mid)
            val+=self.mergeSort(arr,mid+1,h)
            val+=self.merge(arr,l,h,mid)
        return val
    
    def countPairs(self,arr, n): 
        for i in range(n):
            arr[i]*=i
        return self.mergeSort(arr,0,n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends