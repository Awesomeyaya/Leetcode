def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if nums is False or len(nums) <= 0:
            return -1 
        
        start = 0 
        end = len(nums) - 1 
        
        while start +1 < end :
            mid = int((end + start)/2) 
            if nums[mid] == target: 
                return mid 
            elif nums[mid] < target: 
                start = mid + 1
            else:
                end = mid - 1 
                
        if nums[start] == target: 
            return start
        elif nums[end] == target:
            return end 
        else:
            return -1 
