from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if new interval's start time <= current observed interval's end time, update its end time, otherwise append the new interval
        # and update the current observed intervals
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x[0])
        current_interval = intervals[0]
        merge = []
        for i in intervals[1:]:
            if i[0] <= current_interval[1]:
                current_interval[1] = max(i[1], current_interval[1])
            else:
                merge.append(current_interval)
                current_interval = i
        merge.append(current_interval)
        return merge


class ConciseSolution:
    # If new internal's start time > last element's end time, append the interval to the merge list
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merge = []
        for interval in intervals:
            if not merge or interval[0] > merge[-1][1]:
                merge.append(interval)
            else:
                merge[-1][1] = max(interval[1],  merge[-1][1])
        return merge
