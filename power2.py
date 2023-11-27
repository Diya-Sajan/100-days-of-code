def isPowerofTwo(n):
    
    while(n>1):
        if n%2!=0:
            return "NO"
        else:
            n=n//2
    return "yes" 
        
#print(isPowerofTwo(8))
print(isPowerofTwo(3))