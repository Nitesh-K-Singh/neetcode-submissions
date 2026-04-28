class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # this is basically dteceting inetrvals.. 
        # so ideally: detect intervals, merge intervals, insert and merge intervals, 
        # don't know why this is backwards

        n = len(intervals)
        # intervals = [[x] for x in intervals]
        intervals = sorted(intervals, key = lambda x: x.start)

        for i in range(n-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        
        return True
