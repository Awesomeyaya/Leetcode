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
            
      
    
