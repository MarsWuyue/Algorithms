# [252. 会议室](https://leetcode-cn.com/problems/meeting-rooms/)

"""

给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

示例 1:

输入: [[0,30],[5,10],[15,20]]
输出: false
示例 2:

输入: [[7,10],[2,4]]
输出: true
"""
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n == 0:
            return False
        intervals.sort()
        for row in range(1, n):
            left = intervals[row - 1][0]
            right = intervals[row - 1][1]
            if intervals[row][0] <= right:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    param = [[0,30],[5,10],[15,20]]
    res = sol.canAttendMeetings(param) # False
    assert res == False
    param =[[7,10],[2,4]]
    res = sol.canAttendMeetings(param) # True
    assert res == True