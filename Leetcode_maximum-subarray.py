class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max1=nums[0]
        for i in range(len(nums)):
            sum=sum+nums[i]
            max1=max(sum,max1)
            if(sum<0):
                sum=0
        return max1
