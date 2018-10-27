class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return False
        dir1 = {}
        for i in range(len(nums)):
            if target - nums[i] in dir1:
                return [dir1[target - nums[i]] , i]
            else :
                dir1[nums[i]] =i
