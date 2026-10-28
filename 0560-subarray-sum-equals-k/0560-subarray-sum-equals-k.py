class Solution(object):
    def subarraySum(self, nums, k):
        freq={0:1}
        count=0
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            needed=prefix-k
            if needed in freq:
                count+=freq[needed]
            freq[prefix]=freq.get(prefix,0)+1
        return count