#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/26 14:42
# @Author  : Jax
# @File    : main.py
# @Software: PyCharm

"""
## 905. 按奇偶排序数组

### 相关标签
1. 数组
2. 双指针
3. 排序

给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

返回满足此条件的 任意一个数组 作为答案。

 

示例 1：

输入：nums = [3,1,2,4]
输出：[2,4,3,1]
解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
示例 2：

输入：nums = [0]
输出：[0]
 

提示：

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
                continue

            # i 是奇数
            # j 偶数
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                continue

            # i 奇数, j 奇数
            j -= 1

        return nums


if __name__ == '__main__':
    print(Solution().sortArrayByParity([1, 3]))
