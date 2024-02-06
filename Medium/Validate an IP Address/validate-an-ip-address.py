#User function Template for python3

def isValid(s):
    l = s.split('.')
    if len(l)!=4:
        return 0
        
    for i in l:
        if len(i)==0 or len(i)>3 or (len(i)>1 and i[0]=='0') or i.isdigit()==False or int(i)<0 or int(i)>255:
            return 0

    return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends