"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        points = sorted(set([val for  x in intervals for val in (x.start, x.end) ]))
        segments = [(points[i], points[i+1]) for i in range(len(points)-1)]

        count = {}
        for x in segments:
            count[x] = count.get(x,0)
        # relation between any segment and iany nterval.. segment is either contained completely in ointerval or disjoinyt
        # there is no partial overlap

        for interval in intervals:
            increment = [x for x in count.keys() if x[0] >= interval.start  and x[1] <= interval.end ] # all contained segments
            for x in increment:
                count[x] = count[x] + 1

        return max(count.values(), default=0)





        