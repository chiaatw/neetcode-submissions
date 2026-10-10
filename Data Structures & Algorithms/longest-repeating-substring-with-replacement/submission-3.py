class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0

        hm = {}
        maxf = 0

        for c in range(len(s)):
            hm[s[c]] = 1 + hm.get(s[c], 0)
            maxf = max(maxf, hm[s[c]])

            while (c - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, c - l + 1)
        return res