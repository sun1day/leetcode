"""
# 9. 回文数

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。
 

示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
 

提示：

-2**31 <= x <= 2**31 - 1
 

进阶：你能不将整数转为字符串来解决这个问题吗？
"""


class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     """转化为 字符串 方法"""
    #     _x = str(x)
    #     if len(_x) == 1:
    #         return True
    #
    #     if x < 0:
    #         return False
    #
    #     mid = (len(_x) - 1) / 2
    #
    #     i = 0
    #     while i < mid:
    #
    #         j = -i - 1
    #         if _x[i] != _x[j]:
    #             return False
    #         i += 1
    #
    #     return True
    def isPalindrome(self, x: int) -> bool:
        """不转化为 字符串 方法"""
        if (x < 0) or ((x != 0) and (x % 10 == 0)):
            # 负数 肯定不为会文. x 不为 0 而且 各位为 0 肯定也不是回文.
            return False

        # 考虑起码得情况
        _x = 0
        while x > _x:
            _x = _x * 10 + x % 10
            x //= 10
        return (_x == x) or (_x // 10 == x)


if __name__ == '__main__':
    print(Solution().isPalindrome(121))

