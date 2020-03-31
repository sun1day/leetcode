from typing import List


class Solution:
    """冒泡排序, 时间超出"""
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # min_num = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums


Solution().sortArray([5, 1, 1, 2, 0, 0])
