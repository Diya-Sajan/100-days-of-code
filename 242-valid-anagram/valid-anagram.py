class Solution(object):
    def isAnagram(self, s, t):
        ls = sorted(s)
        lt = sorted(t)
        if (ls==lt):
            return True
        else:
            return False
         