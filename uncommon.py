
def UncommonChars(A, B):
    a = [*A]
    b = [*B]
    c = sorted(list(set(a+b)))
    newc = []
    for i in c:
        if not ((i in a) and (i in b)):
            newc.append(i)
    res = "".join(newc)
    if res == '': return -1
    else: return res

print(UncommonChars("characters" , "alphabets"))


