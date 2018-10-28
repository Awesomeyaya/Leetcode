def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = len(set(nums))
        l = len(nums)
        if l - s > 0 :
            return True 
        else:
            return False
