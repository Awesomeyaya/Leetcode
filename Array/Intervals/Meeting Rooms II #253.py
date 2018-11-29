''' 
First sort the start and end time.
Then use available to represent the available room. And use numsroom to represent the meeting rooms needed.

If there is available room, then we don't have to add one more meeting room. And if there is a conflict meeting coming, we lose 
one available room. 
If there is no available room, then we have to add one more meeting room. 


'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        available = numsroom = 0
        s = e = 0 
        while s < len(start):
            if start[s] < end[e]:
                if available == 0: 
                    numsroom += 1
                else: 
                    available -= 1 
                s += 1 
            else: 
                available += 1 
                e += 1 
        return numsroom
