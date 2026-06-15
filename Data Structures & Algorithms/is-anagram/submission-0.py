class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        if len(s) != len(t):
            return False
        else:
            for char in s:
                hm[char] = hm.get(char, 0) + 1
            for char in t:
                hm[char] = hm.get(char, 0) - 1
            for val in hm.values():
                if val !=   0:
                    return False
            return True