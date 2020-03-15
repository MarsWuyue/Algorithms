"""
快速排序

思想：
    找个标兵，然后把小于他的都放左边，大于它的都放右边
    然后类似于二分法，对于标兵的两端继续执行第一步
    递归执行上述两步操作

本模板注意：
    1. 标兵设置为当前要排序的数组片段的最右侧
    2. 利用一个count计数
    3. 遇到比标兵小的，就把他跟count所在位置交换，然后count后移一位
    4. 在做完全部交换后，此时count指向的就是第一个比标兵大的位置
    5. 最后记得把标兵位置和count位置交换
    6. 返回count位置
    7. 注意terminator，应该是end <= begin
"""

from typing import List
class Solution():
    def sort(self, nums: List[int]):
        self.quickSort(nums, 0, len(nums) - 1)

    def quickSort(self, nums, begin, end):
        if end <= begin:
            return
        pivot = self.partition(nums, begin, end)
        self.quickSort(nums, begin, pivot - 1)
        self.quickSort(nums, pivot + 1, end)

    def partition(self, nums, begin, end):
        count, pivot = begin, end
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        nums[count], nums[pivot] = nums[pivot], nums[count]
        return count

if __name__ == "__main__":
    sol = Solution()
    param = [3, 5, 2, 1, 6, 4]
    sol.sort(param)
    assert param == [1, 2, 3, 4, 5, 6]
