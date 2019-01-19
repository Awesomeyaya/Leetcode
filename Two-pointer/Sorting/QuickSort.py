'''
1. left <= right 一定正确
2. while 套 while ，用于移动left & right
3. 结束时，right 在 left 左边，然后再继续分别partition左边和右边
4. pivot 是一个值，而不是index 
5. start >= end: 就return A


'''
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None 
        self.quicksort(A,0,len(A)-1)
            
    def quicksort(self,A,start,end):
        if start >= end:
            return A
        left,right,pivot = start,end,A[(start+end)//2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1 
            while left <= right and A[right] > pivot:
                right -=1 
            if left <= right:
                A[left],A[right] = A[right],A[left]
                left += 1 
                right -=1
        self.quicksort(A,start,right)
        self.quicksort(A,left,end)
