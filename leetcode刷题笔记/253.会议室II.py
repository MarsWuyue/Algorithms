# [253. 会议室 II](https://leetcode-cn.com/problems/meeting-rooms-ii/)

"""
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1

"""
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2:
            return n
        intervals.sort()
        res = 1
        for row in range(1, n):
            left = intervals[row - 1][0]
            right = intervals[row - 1][1]
            if intervals[row][0] < right:
                res += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    param = [[0, 30],[5, 10],[15, 20]]
    val = sol.minMeetingRooms(param) # 2
    assert val == 2
    param = [[7,10],[2,4]]
    val = sol.minMeetingRooms(param) # 1
    assert val == 1
