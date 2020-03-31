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
        count = 1
        for i in range(length):
            for j in range(0, length - i - 1):
                count += 1
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        print(count)

        return a

    def maopaopaixuyouhua1(self, nums: List[int]):
        """
        此种优化属于不稳定优化, 当一定的情况下有排序好的时候, 这中方法会比较好. 当一个循环中标记没变的时候, 说明已经是好的排序了
        :param nums:
        :return:
        """
        count = 1
        for i in range(len(nums)):
            stamp = False
            for j in range(len(nums) - i - 1):
                count += 1
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    stamp = True

            if not stamp:
                print(count)
                return nums
        print(count)


Solution().maopaopaixuyouhua1([1, 2, 3, 4, 5])
print("------------------------------")
Solution().maopao([1, 2, 3, 4, 5])
