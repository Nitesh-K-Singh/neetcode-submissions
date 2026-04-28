class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # first store the interval at correct place
        intervals_new = intervals.copy()
        intervals_new.append(newInterval)
        intervals_new = sorted(intervals_new, key = lambda x: x[0])

        # merge intervals: but i lose information fo where i added it and so have to do a complete pass?
        # so not able to exploit loacl structure: only possible overlapping will be for intervals just before and just after this stored new interval

        n = len(intervals_new)
        intervals_final = [intervals_new[0]]

        for i in range(1,n):
            if intervals_new[i][0] <= intervals_final[-1][1]:
                max_stop = max(intervals_new[i][1],intervals_final[-1][1] )
                intervals_final[-1][1] = max_stop

            else:
                intervals_final.append(intervals_new[i])



        return intervals_final
        

        