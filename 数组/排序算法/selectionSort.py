"""
选择排序

时间复杂度：O(n^2)

思想：
    第一层循环用于指定元素
    第二层循环用于找到指定元素之后的最小元素，并与指定元素交换

实现效果：
    每经历一次第一层循环，就会将数组中最小元素排到前面
"""
from typing import List
class Solution():
    def sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            if min_idx != i:
                nums[i], nums[min_idx] = nums[min_idx], nums[i]

if __name__ == "__main__":
    sol = Solution()
    param = [3, 5, 2, 1, 6, 4]
    sol.sort(param)
    assert param == [1, 2, 3, 4, 5, 6]