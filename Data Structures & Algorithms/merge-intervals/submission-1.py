class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)
        intervals = sorted(intervals, key = lambda x: x[0])
        new = [intervals[0]]

        for i in range(1,n):
            if intervals[i][0] <= new[-1][1]:   # left to right merging , take care of last case
                max_stop = max(intervals[i][1], new[-1][1])
                new[-1][1] =  max_stop

            else:
                new.append(intervals[i])
        return new
            

