"""
插入排序

时间复杂度：O(n^2)

思想：
    数组的前面会慢慢变得有序
    第一层循环用于选取在非有序队列的第一个
    然后与前面的有序队列进行逐一比较 - 比较顺序是：后 -> 前
    由于前面是有序的，因此只要先比较当前元素和有序队列的最后一个，
    遇到不符合比较规则的，说明当前元素找到了相应位置，直接break
注意：
    每做一次交换，需要 i--
"""
from typing import List
class Solution():
    def sort(self, nums: List[int]):
        n = len(nums)
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] >= nums[j]:
                    break
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1

if __name__ == "__main__":
    sol = Solution()
    param = [3, 5, 2, 1, 6, 4]
    sol.sort(param)
    assert param == [1, 2, 3, 4, 5, 6]