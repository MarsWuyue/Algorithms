"""
归并排序

思想：
    找到mid，然后左边归并，右边归并，之后进行merge
    最后一步的merge相当于两个有序数组进行merge的操作

注意：
    merge的时候需要注意两边数组长短不等，存在有一个数组没有merge完的情况
    此时将这个数组剩下的元素直接拼接到tmp即可
"""

from typing import List
class Solution():
    def sort(self, nums:List[int]):
        self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, left, right):
        if right <= left:
            return
        mid = (left + right) >> 1
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i, j = left, mid + 1
        tmp = [0] * (right - left + 1)
        count = 0
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp[count] = nums[i]
                i += 1
            else:
                tmp[count] = nums[j]
                j += 1
            count += 1
        if i <= mid:
            tmp[count:] = nums[i:mid + 1]
        if j <= right:
            tmp[count:] = nums[j:right + 1]
        nums[left:right + 1] = tmp[:]

if __name__ == "__main__":
    sol = Solution()
    param = [3, 5, 2, 1, 6, 4]
    sol.sort(param)
    assert param == [1, 2, 3, 4, 5, 6]