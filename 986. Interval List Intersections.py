# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Time: O(n) Space: O(1)

"""

class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i = j = 0 
        ans = []
        
        while i < len(A) and j < len(B):
            lower = max(A[i].start, B[j].start) 
            upper = min(A[i].end, B[j].end) 
            
            if lower <= upper:
                ans.append([lower, upper])
            
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1 
        return ans
        
