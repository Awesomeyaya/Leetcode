'''
1. 用递归去解决mergesort，每次把数组对半分
2. 先mergesort再merge
3. merge: 用leftstart和rightstart分别指向左边数组和右边数组的起始位置。然后把比较小的放进result数组里。result数组的position由index控制。
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
        temp = [0 for _ in range(len(A))]
        self.mergesort(A,0,len(A)-1,temp)
    
    def mergesort(self,A,start,end,temp):
        if start >= end:
            return 
        mid = (start+end)//2
        self.mergesort(A,start,mid,temp)
        self.mergesort(A,mid+1,end,temp)
        self.merge(A,start,mid,end,temp)
    
    def merge(self,A,start,mid,end,temp):
        leftstart = start 
        rightstart = 1 + mid
        index = start
        while leftstart <= mid and rightstart <= end:
            if A[leftstart] < A[rightstart]:
                temp[index] = A[leftstart]
                index += 1
                leftstart += 1 
            else:
                temp[index] = A[rightstart]
                index += 1 
                rightstart += 1 
        while leftstart <= mid:
            temp[index] = A[leftstart]
            index += 1
            leftstart += 1 
        while rightstart <= end:
            temp[index] = A[rightstart]
            index += 1 
            rightstart += 1 
        for index in range(start,end+1):
            A[index] = temp[index]
