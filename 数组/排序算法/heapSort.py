"""
堆排序
"""

from typing import List
from collections import deque
class Solution():
    def sort(self, nums):
        self.heapSort(nums)

    def heapSort(self, nums):
        queue = deque(nums)
        queue.appendleft(0)
        L = len(queue) - 1
        fatherCount = L // 2
        for i in range(fatherCount):
            self.heapAdjust(queue, fatherCount - i, L)
        print(queue)
        for i in range(L - 1):
            self.swap(queue, 1, L - i)
            self.heapAdjust(queue, 1, L - 1 - i)
        nums[:] = [queue[i] for i in range(1, L + 1)]

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def heapAdjust(self, nums, fatherIndex, length):
        son = fatherIndex * 2
        while son <= length:
            if son < length and nums[son] < nums[son + 1]:
                son = son + 1
            if nums[fatherIndex] >= nums[son]:
                break
            else:
                nums[fatherIndex], nums[son] = nums[son], nums[fatherIndex]
                fatherIndex = son
                son = 2 * fatherIndex

if __name__ == "__main__":
    sol = Solution()
    param = [50, 16, 30, 10, 60, 66, 2, 80, 70]
    sol.sort(param)
    assert param == [2, 10, 16, 30, 50, 60, 70, 80, 66]
