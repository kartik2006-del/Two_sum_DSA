class Solution(object):
    def pivotIndex(self, nums):
        total=0
        for i in nums:
            total+=i
        left_sum=0
        for j in range(len(nums)):
            if left_sum==total-left_sum-nums[j]:
                return j
            left_sum+=nums[j]
        return -1