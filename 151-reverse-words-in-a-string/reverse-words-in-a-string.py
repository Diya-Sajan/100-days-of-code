class Solution:
    def reverseWords(self, s: str) -> str:
        a = [x for x in s.strip().split()]
        a[:] = a[::-1]
        st = ""
        for i in a:
            st = st+i+" "
        return st[:-1]

        