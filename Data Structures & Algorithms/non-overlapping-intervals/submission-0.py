class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[1])

        prevEnd = intervals[0][1]
        rem = 0

        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                rem += 1
            else:
                prevEnd = intervals[i][1]
        return rem

