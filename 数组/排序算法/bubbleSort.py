"""
冒泡排序

时间复杂度：O(n^2)

思想：
    每一次循环都将数组中最大的数放置到最后

第一层循环：次数循环，循环n次
第二层循环：每次从第一个元素，两两比较
第二层循环的次数为： n - 1 - i
"""

from typing import List
class Solution():
    def sort(self, nums: List[int]):
        n = len(nums)
        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

if __name__ == "__main__":
    sol = Solution()
    param = [3, 5, 2, 1, 6, 4]
    sol.sort(param)
    assert param == [1, 2, 3, 4, 5, 6]