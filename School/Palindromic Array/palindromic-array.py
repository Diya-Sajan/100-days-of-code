# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    for i in range (n):
        x = str(arr[i])
        if x == x[::-1]:
            continue
        else:
            return 0
    return 1



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends