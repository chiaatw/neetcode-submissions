class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for n in range(len(nums)):

            res[n] = prefix
            prefix *= nums[n]

        postfix = 1
        for j in range(len(nums) -1, -1, -1):

            res[j] *= postfix
            postfix *= nums[j]

        return res