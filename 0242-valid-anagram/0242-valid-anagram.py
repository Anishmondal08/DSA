class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t = list(t)

        for i in range(len(s)):
            if s[i] in t:
                index = t.index(s[i])
                t.pop(index)
            else:
                return False

        return True