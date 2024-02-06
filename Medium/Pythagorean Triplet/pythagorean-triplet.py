#User function Template for python3
class Solution:
    def checkTriplet(self, arr, n):
        square_map = {i * i: i for i in arr}

        for square1 in square_map:
            for square2 in square_map:
                sum_of_squares = square1 + square2

                if sum_of_squares in square_map:
                    return True
                    
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.checkTriplet(arr, n)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends