class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        newStr = ''.join(chars)
        return newStr == newStr [::-1]