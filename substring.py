def strstr(s, x):
    a = [*s]
    b = [*x]

    for i in range(0,len(a)):
        if a[i] == b[0] and i!= len(a)-1:
            for j in range(1,len(b)):
                if not (i+j>=len(a)):
                    if a[i+j]==b[j]:
                        if j==len(b)-1:
                            return i
                        continue
                    else:
                        break        
    if i==len(a)-1:return -1
'''def strstr(s,x):
    
    if x in s :
        i=s.index(x)
        return i
    return -1'''


print(strstr("bafeecbbceeeeaefeffccabfbbdfdacefccdcbec", "ecaaaeffddfddbacabbdcefb"))
#print(len("bafeecbbceeeeaefeffccabfbbdfdacefccdcbec"))