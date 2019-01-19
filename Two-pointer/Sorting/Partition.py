'''
Partition tempelet: O(n)
pivot 左边 <pivot 
pivot 右边 >= pivot
'''

def Partition(self,nums,start,end):
if start >= end:
    return 
mid = (start+end)//2 
left, right, pivot = start, end, nums[mid]
while left <= right:
    while left <= right and nums[left] < pivot:
            left += 1 
        while left <= right and nums[right] >= pivot:
            right -= 1 
        if left <= right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1 
            right -=1 
            
'''
应用1: Find kth largest element 
等于 find (length -k)th smallesr element 
依旧是partition, 每次partition的right如果比k小，说明nums[k] < nums[left], 在nums[start,left]继续partition. 
直到start == end 时 return nums[k]，说明找到了。

'''
    
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return 0 
        length = len(nums)-1
        return self.partition(nums,0,length,len(nums)-n)
        
        
    def partition(self,nums,start,end,k):
        if start == end:
            return nums[k]
        mid = (start+end)//2
        left, right, pivot = start, end, nums[mid]
        while left <= right and nums[left] < pivot:
            left += 1 
        while left <= right and nums[right] > pivot:
            right -= 1 
        if left <= right:
            nums[left],nums[right] = nums[right],nums[left]
            left, right = left+1, right-1
        if k <= right:
            return self.partition(nums,start,right,k)
        if k >= left:
            return self.partition(nums,left,end,k)
            
        return nums[k]
