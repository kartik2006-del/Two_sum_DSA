class Solution(object):
    def runningSum(self, nums):
        total=0
        arr=[]
        for i in range(len(nums)):
            total+=nums[i]
            arr.append(total)
        return arr
            
