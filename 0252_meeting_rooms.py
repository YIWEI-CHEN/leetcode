from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        end_time = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end_time:
                return False
            else:
                end_time = interval[1]
        return True

# condition: if two meeting overlaps, he cannot attend all meetings
# sort the start time
# [[0,30],[5,10],[15,20]]
# check end time of previous meeting and start time of current meeting