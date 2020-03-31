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

    def maopao(self, a):
        """
        冒泡排序

        1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
        2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        3. 针对所有的元素重复以上的步骤，除了最后一个；
        4. 重复步骤1~3，直到排序完成。
        todo: 此冒泡排序还可以优化
        :param a:
        :return:
        """
        length = len(a)
        for i in range(length):
            for j in range(1, length - i):
                if a[j - 1] > a[j]:
                    a[j], a[j - 1] = a[j - 1], a[j]
        print(a)

        return a


Solution().maopao([5, 1, 1, 2, 0, 0])
