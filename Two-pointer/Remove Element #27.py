def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        """
        zero = 0 
        for n in range(len(nums)):
            if nums[n] != val:
                nums[zero] = nums[n]
                zero = zero + 1
        return zero
