"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

"""

__author__ = 'Sun'


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            mark = '+'
        elif x == 0:
            return 0
        else:
            mark = '-'
            x = 0 - x
        str_x = str(x)

        if mark == '-':
            new_x = str_x[-1::-1].lstrip('0')
            new_x = int(new_x)
            new_x = 0 - new_x
            if new_x < -2 ** 31:
                return 0
            return new_x

        new_x = str_x[-1::-1].lstrip('0')
        new_x = int(new_x)
        if new_x > 2 ** 31-1:
            return 0
        return new_x

        # x = str(x)
        # mark = '-'
        # if x.startswith('-'):
        #     x.replace('-', '')
        # elif x.startswith('+'):
        #     x.replace('+', '')
        # else:
        #     pass
        # new_x = mark + x[-1:0].replace('0', '')
        # if int(new_x) > 2 ** 31 - 1 or int(new_x) < -2 ** 31:
        #     return 0
        # return int(new_x)

# ------------------------- 优化解
    def reverse_better(
            self,
            x: int) -> int:

        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res


print(Solution().reverse_better(-50100001))
# x = 1
# boundry = (1<<31) -1 if x>0 else 1<<31
# print(boundry)