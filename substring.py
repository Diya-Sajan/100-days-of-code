def UncommonChars(s, x):
    a = [*s]
    b = [*x]

    for i in range(0,len(a)):
        if a[i] == b[0]:
            for j in range(1,len(b)):
                if a[i+j]==b[j]:
                    if j==len(b)-1:
                        return i
                    continue
                else:
                    break

        
    if i==len(a)-1:return -1


print(UncommonChars("charaacacters" , "ac"))
