class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        arr = []
        for i in range(len(nums)):
            heapq.heappush(arr, nums[i])
            while len(arr) > k:
                heapq.heappop(arr)
        return arr[0]