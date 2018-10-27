def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int , the length of the returned array
        """
        
        if not nums:
            return 0 
        
        pointer = 0
        for n in range(1,len(nums)) :
            if nums[n] != nums[pointer]:
                pointer = pointer + 1
                nums[pointer] = nums[n]
        return pointer + 1
