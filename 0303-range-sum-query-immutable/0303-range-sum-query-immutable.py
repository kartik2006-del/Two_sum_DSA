class NumArray(object):

    def __init__(self, nums):
        self.nums=nums
        total=0
        self.prefix=[]
        for i in nums:
            total+=i
            self.prefix.append(total)

        

    def sumRange(self, left, right):
        if left!=0:
            return self.prefix[right]-self.prefix[left-1]
        else:
            return self.prefix[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)