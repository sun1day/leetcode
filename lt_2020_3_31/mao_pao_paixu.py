"""
最好时间复杂度: O(n)  # 优化之后的方法
最坏时间复杂度: O(n**2)

"""
import time
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

        todo 大佬的说法:
            假设我们现在排序ar[]={1,2,3,4,5,6,7,8,10,9}这组数据，按照上面的排序方式，第一趟排序后将10和9交换已经有序，接下来的8趟排序就是多余的，什么也没做。所以我们可以在交换的地方加一个标记，如果那一趟排序没有交换元素，说明这组数据已经有序，不用再继续下去。
        :param nums:
        :return:
        """
        count = 1
        stamp = False
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                count += 1
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    stamp = True

            if not stamp:
                print(count)
                return nums
        print(count)
        return nums

    def mao_pao_you_hua_2(self, nums):
        """
        第二种优化
        优化一仅仅适用于连片有序而整体无序的数据(例如：1， 2，3 ，4 ，7，6，5)。
        但是对于前面大部分是无序而后边小半部分有序的数据(1，2，5，7，4，3，6，8，9，10)排序效率也不可观，
        对于种类型数据，我们可以继续优化。
        既我们可以记下最后一次交换的位置，
        后边没有交换，必然是有序的，
        然后下一次排序从第一个比较到上次记录的位置结束即可。

        """
        count = 1  # 计数器
        stamp = False  # 标记
        pos = len(nums) - 1  # 这个是记录最后位置的下表
        s = 0  # 第三个变量
        for i in range(len(nums)):
            for j in range(pos):
                count += 1
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    stamp = True
                    s = j
            pos = s - 1

            if not stamp:
                print(count)
                return nums
        print(count)
        return nums

    def mao_pao_you_hua_3(self, nums):
        # def mp(nums: List[int]) -> List[int]:
        """冒泡排序最终版本"""
        length = len(nums)

        s = 0  # 标记最小的变动的位置
        b = length - 1  # 标记最大变动的位置
        swapb = 0
        swaps = length - 1
        for i in range(length):
            flag = False
            for j in range(s, b):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    flag = True
                    swapb = j

            b = swapb
            if not flag:
                return nums
            for k in range(b, s, -1):
                if nums[k] < nums[k - 1]:
                    nums[k], nums[k - 1] = nums[k - 1], nums[k]
                    flag = True
                    swaps = k

            s = swaps
            if not flag:
                return nums

        # print(mp([95, 85, 12, 52, 64, 74, 105, 502, 4, 7, 6, 1, 74, 60, 141, 19, 34, 45, 59]))


start_t = time.time()
print(Solution().maopaopaixuyouhua1([1, 2, 5, 7, 4, 3, 6, 8, 9, 10]))
end_t1 = time.time()
print("------------------------------")
print(Solution().maopao([1, 2, 5, 7, 4, 3, 6, 8, 9, 10]))
end_t2 = time.time()
print("------------------------------")
print(Solution().mao_pao_you_hua_2([1, 2, 5, 7, 4, 3, 6, 8, 9, 10]))
end_t3 = time.time()
print("****************")
print(Solution().mao_pao_you_hua_3([1, 2, 5, 7, 4, 3, 6, 8, 9, 10]))
end_t4 = time.time()
print(11111111111111111111111111111111111111)

t1 = end_t1 - start_t
t2 = end_t2 - start_t - t1
t3 = end_t3 - start_t - t2 - t1
t4 = end_t4 - start_t - t3 - t2 - t1
print(t1, t2, t3, t4)
# [1 ,3, 2]
