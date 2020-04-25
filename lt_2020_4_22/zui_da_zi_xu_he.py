"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


def solution_sort(nums: List[int]) -> int:
    """动态规划"""
    sums = nums[0]
    max_sum = sums
    for num in nums[1:]:
        if sums > 0:
            sums += num
        else:
            sums = num

        if max_sum < sums:
            max_sum = sums

    return max_sum


def solution_sort1(nums: List[int]) -> int:
    """分治法， 递归"""
    # 结束条件是啥？ 当 nums 的长度为 1 的时候， 最大的就是它本身， 直接返回
    if len(nums) == 1:
        return nums[0]

    # 不等于 1， 开始计算 左边 右边 最大值
    l_nums = nums[: len(nums) // 2]
    r_nums = nums[len(nums) // 2:]

    # 在求这个子序列的左右最大值, 递归 todo 这样是选择了子列中最大的一个数 用来相加。 没有考虑 是不是连续的问题
    max_l = solution_sort1(l_nums)  # 左子列返回的最大值
    max_r = solution_sort1(r_nums)  # 又子列返回的最大值

    # 中间的最大子列呢？
    l_max = nums[len(nums) // 2 - 1]
    l_tem = 0
    r_max = nums[len(nums) // 2]
    r_tem = 0

    for i in nums[len(nums) // 2 - 1:: -1]:
        # print(i)
        l_tem += i
        l_max = max(l_max, l_tem)
    for j in nums[len(nums) // 2:]:
        r_tem += j
        r_max = max(r_max, r_tem)

    return max(max_l, max_r, l_max + r_max)  # 返回三个最大值


if __name__ == '__main__':
    print(solution_sort1([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]))
