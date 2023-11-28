import sys
def findMaxLength(nums):
    x = sorted(nums)
    zerol = [element for element in x if element == '0']
    onel = [element for element in x if element == '1']
    
    a = len(zerol)
    b = len(onel)
    print(zerol,a,onel,b)

    if a>b:
        return (b)*2
    else:
        return a*2

numstring = input()
nums = numstring.split(" ")

print(nums)
print(findMaxLength(nums))