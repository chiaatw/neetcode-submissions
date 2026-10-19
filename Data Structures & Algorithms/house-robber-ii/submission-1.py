class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(res):
            prev1, prev2 = 0, 0

            for n in res:
                prev2, prev1 = prev1, max(prev1, n + prev2)
            return prev1

        if len(nums) == 1:
            return nums[0]
        
        return max(robbing(nums[1:]), robbing(nums[:-1]))
        