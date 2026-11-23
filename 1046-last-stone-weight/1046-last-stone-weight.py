
class Solution(object):
    def lastStoneWeight(self, stones):
        import heapq
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                diff = first - second
                heapq.heappush(stones, -diff)
        if stones:
            return -stones[0]
        return 0
