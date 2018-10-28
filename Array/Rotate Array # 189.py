def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if k is None or k <= 0: 
            return 
        k = k % (len(nums))
        end = len(nums)- 1
        self.swap(nums,0,end-k)
        self.swap(nums,end-k+1,end)
        self.swap(nums,0,end)

    def swap(self, nums, start,end):
        while start < end : 
            nums[start], nums[end] = nums[end], nums[start]
            start = start + 1
            end = end - 1
