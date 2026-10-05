class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        maxV = 0

        for n in nums:
            if maxV < 0:
                maxV = 0
            maxV += n
            maxSub = max(maxSub, maxV)
        return maxSub
