class Solution(object):
    def subarraySum(self, nums, k):
        freq={0:1}
        prefix_sum=0
        count=0
        for i in nums:
            prefix_sum+=i
            needed=prefix_sum-k
            if needed in freq:
                count+=freq[needed]
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count

