"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
示例 1：

输入: n = 5, m = 3
输出: 3
示例 2：

输入: n = 10, m = 17
输出: 2
"""
__author__ = 'Jax'


class Solution:
    def last_remaining(self, n: int, m: int) -> int:
        """圆圈问题"""
        # 构建列表

        r_list = [num for num in range(n)]  # type: list

        # 如果列表的长度为 1, 直接返回

        if len(r_list) == 1:
            return n
        begin_index = 0

        while len(r_list) > 1:
            begin_index = (begin_index + m % len(r_list) - 1) % len(r_list)  # 最开始删除的位置
            # begin_index = (begin_index + m -1 ) % len(r_list)  # todo 看别人的计算,

            r_list.pop(begin_index)
            # print(r_list)

        print(r_list[0])


Solution().last_remaining(n=10, m=17)


#############################
# 约瑟夫环解体思路, 比上边的时间节省了 很多倍数  todo 暂时还没看懂

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (m + x) % i
        return x

