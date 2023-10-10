class Solution(object):
    def isAnagram(self, s, t):
        ls = []
        lt = []
        for i in s:
            ls.append(i)
        for j in t:
            lt.append(j)
        ls.sort()
        lt.sort()
        if (ls==lt):
            return True
        else:
            return False




        """
        :type s: str
        :type t: str
        :rtype: bool
        """
         