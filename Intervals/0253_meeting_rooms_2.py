"""
Meeting Rooms II

Medium

Link:
1. NeetCode 150: https://neetcode.io/problems/meeting-rooms-ii
2. LeetCode: https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2

Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1


"""
import heapq
from typing import List


class OutofTimeSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = [set(range(*intervals[0]))]
        for i in range(1, len(intervals)):
            avail = False
            request = set(range(*intervals[i]))
            for j in range(len(rooms)):
                reserve = rooms[j]
                intersect = reserve & request
                if len(intersect) == 0:
                    reserve.update(request)
                    avail = True
            if not avail:
                rooms.append(request)
        return len(rooms)


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            avail = False
            for j, reserved_e in enumerate(rooms):
                if start >= reserved_e:
                    rooms[j] = end
                    avail = True
                    break
            if not avail:
                rooms.append(end)
        return len(rooms)


class MinHeapSolution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Use min-heap to track the end time of meetings in rooms.
        For each new meeting, check if it can reuse the room with the earliest end time.
        If yes, update the end time of that room. If not, allocate a new room.
        Finally, the size of the heap represents the minimum number of rooms required.
        
        Time Complexity: O(N log N) due to sorting and heap operations.
        Space Complexity: O(N) for the heap in the worst case.
        
        Recommended solution.
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        return len(rooms)


if __name__ == '__main__':
    test_cases = [
        ([], 0, "Empty input"),
        ([[4, 9]], 1, "Single meeting"),
        ([[0, 8], [8, 10]], 1, "Adjacent meetings (no conflict at 8)"),
        ([[0, 40], [5, 10], [15, 20]], 2, "Example 1: overlapping meetings"),
        ([[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]], 2, "Multiple overlaps"),
        ([[9, 10], [4, 9], [4, 17]], 2, "Unsorted input"),
        ([[1, 13], [13, 15]], 1, "Back-to-back meetings"),
        ([[7, 10], [2, 4]], 1, "Non-overlapping meetings"),
        ([[1, 5], [8, 9], [8, 9]], 2, "Duplicate intervals"),
        ([[0, 30], [5, 10], [15, 20]], 2, "One long meeting with shorter ones"),
        ([[1, 3], [3, 6], [6, 8], [8, 10]], 1, "Chain of adjacent meetings"),
        # Large dataset test (truncated display)
        ([[64738, 614406], [211748, 780229], [208641, 307338], [499908, 869489], [218907, 889449], [177201, 481150],
          [123679, 384415], [120440, 404695], [191810, 491295], [800783, 826206], [165175, 221995], [420412, 799259],
          [484168, 617671], [746410, 886281], [765198, 792311], [493853, 971285], [194579, 313372], [119757, 766274],
          [101315, 917883], [557309, 599256], [167729, 723580], [731216, 988021], [225883, 752657], [588461, 854166],
          [231328, 285640], [772811, 869625], [892212, 973218], [143535, 306402], [336799, 998119], [65892, 767719],
          [380440, 518918], [321447, 558462], [54489, 234291], [43934, 44986], [11260, 968186], [248987, 707178],
          [355162, 798511], [661962, 781083], [149228, 412762], [71084, 953153], [44890, 655659], [708781, 956341],
          [251847, 707658], [650743, 932826], [561965, 814428], [697026, 932724], [583473, 919161], [463638, 951519],
          [769086, 785893], [17912, 923570], [423089, 653531], [317269, 395886], [412117, 701471], [465312, 520002],
          [168739, 770178], [624091, 814316], [143729, 249836], [699196, 879379], [585322, 989087], [501009, 949840],
          [424092, 580498], [282845, 345477], [453883, 926476], [392148, 878695], [471772, 771547], [339375, 590100],
          [110499, 619323], [8713, 291093], [268241, 283247], [160815, 621452], [168922, 810532], [355051, 377247],
          [10461, 488835], [220598, 261326], [403537, 438947], [221492, 640708], [114702, 926457], [166567, 477230],
          [856127, 882961], [218411, 256327], [184364, 909088], [130802, 828793], [312028, 811716], [294638, 839683],
          [269329, 343517], [167968, 391811], [25351, 369583], [210660, 454598], [166834, 576380], [296440, 873280],
          [660142, 822072], [33441, 778393], [456500, 955635], [59220, 954158], [306295, 429913], [110402, 448322],
          [44523, 88192], [231386, 353197], [120940, 902781], [348758, 597599], [329467, 664450], [208411, 890114],
          [230238, 516885], [434113, 602358], [349759, 419831], [10689, 308144], [94526, 180723], [435280, 986655],
          [611999, 690154], [75208, 395348], [403243, 489260], [498884, 611075], [487209, 863242], [13900, 873774],
          [656706, 782943], [53478, 586952], [226216, 723114], [554799, 922759], [467777, 689913], [80630, 147482],
          [277803, 506346], [532240, 976029], [206622, 761192], [148277, 985819], [10879, 807349], [952227, 971268],
          [172074, 919866], [239230, 384499], [607687, 984661], [4405, 264532], [41071, 437502], [432603, 661142],
          [144398, 907360], [139605, 360037], [943191, 997317], [12894, 171584], [382477, 800157], [452077, 518175],
          [208007, 398880], [375250, 489928], [384503, 726837], [278181, 628759], [114470, 635575], [382297, 733713],
          [156559, 874172], [507016, 815520], [164461, 532215], [17332, 536971], [418721, 911117], [11497, 14032]], 
         77, "Large dataset (140 intervals)")
    ]
    
    print("Meeting Rooms II Test Results:")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for i, (intervals, expected, description) in enumerate(test_cases, 1):
        result = MinHeapSolution().minMeetingRooms(intervals)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        # Format intervals display
        if len(intervals) <= 5:
            intervals_str = str(intervals)
        else:
            intervals_str = f"[{intervals[0]}, {intervals[1]}, ..., {intervals[-1]}] ({len(intervals)} intervals)"
        
        print(f"Test {i}: {description}")
        print(f"Input: {intervals_str}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print("-" * 60)
        
        if result == expected:
            passed += 1
        else:
            failed += 1
    
    print(f"\nSummary: {passed} passed, {failed} failed out of {len(test_cases)} tests")
