'''
Step1: set two sum variables: cursum and maxsum, let them be nums[0]

Step2: loop the array from[1:], calculate the cursum, and get the maxsum 

Tips: 
if num < 0: 
    sum = sum 
if num > 0:
    sum += num
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        
        if not nums:
            return False
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)

            maxSum = max(maxSum, curSum)

        return maxSum
