class Solution:
    def maxProduct(self, nums):
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])

            max_product = max(max_product, curr_max)

        return max_product