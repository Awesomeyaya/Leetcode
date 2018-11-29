# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == [] or len(intervals) == 0:
            return intervals
        
        intervals = sorted(intervals, key = lambda r:r.start)
        result = []
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i].end < result[-1].end:
                continue
            elif intervals[i].start > result[-1].end: 
                result.append(intervals[i])
            else:
                result[-1].end = intervals[i].end 
        return result
