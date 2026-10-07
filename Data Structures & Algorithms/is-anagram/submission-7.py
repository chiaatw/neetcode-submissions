class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm1, hm2 = {}, {}
            
        for c in range(len(s)):
            hm1[s[c]] = 1 + hm1.get(s[c], 0)
            hm2[t[c]] = 1 + hm2.get(t[c], 0)
        return hm1 == hm2