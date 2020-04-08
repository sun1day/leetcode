"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
"""

__author__ = "Sun"


class Solution:
    @classmethod
    def is_palindrome(cls, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True
        res, y = 0, x
        while y != 0:
            res = res * 10 + y % 10
            y //= 10

        if res == x:
            return True
        return False

    @classmethod
    def is_palindrome2(cls, x: int) -> bool:
        y = str(x)
        if y[::-1] == y:
            return True
        return False

    @classmethod
    def is_palindrome3(cls, x: int) -> bool:
        ##########################
        #     todo 错误的思路
        ############################
        y = str(x)
        if y.startswith('10') and y.endswith('10'):
            return True
        return False

    ##################################大佬的写法################################

    # 方法一: 将int转化成str类型: 双向队列
    # 复杂度: O(n^2) [每次pop(0)都是O(n)..比较费时]
    def isPalindrome4(x: int) -> bool:
        lst = list(str(x))
        while len(lst) > 1:
            if lst.pop(0) != lst.pop():
                return False
        return True

    # 方法二: 将int转化成str类型: 双指针 (指针的性能一直都挺高的)
    # 复杂度: O(n)
    def isPalindrome5(x: int) -> bool:
        lst = str(x)
        L, R = 0, len(lst) - 1
        while L < R:
            if lst[L] != lst[R]:
                return False
            L += 1
            R -= 1
        return True

    ######### todo 3-5 都不咋地
    # 方法三: 进阶:不将整数转为字符串来解决: 使用log来计算x的位数
    # 复杂度: O(n)
    def isPalindrome6(self, x: int) -> bool:
        """
        模仿上面字符串的方法:分别取'第一位的数'与'第二位的数'对比
                        (弊端是:频繁计算,导致速度变慢)(下面的方法三只反转一半数字,可以提高性能)
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            import math
            length = int(math.log(x, 10)) + 1
            L = length - 1
            print("l = ", L)
            for i in range(length // 2):
                if x // 10 ** L != x % 10:
                    return False
                x = (x % 10 ** L) // 10
                L -= 2
            return True

    # 方法四: 进阶:不将整数转为字符串来解决: 使用log来计算x的位数
    # 复杂度: O(n)
    def isPalindrome7(self, x: int) -> bool:
        """
        只反转后面一半的数字!!(节省一半的时间)
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            import math
            length = int(math.log(x, 10)) + 1
            reverse_x = 0
            for i in range(length // 2):
                remainder = x % 10
                x = x // 10
                reverse_x = reverse_x * 10 + remainder
            # 当x为奇数时, 只要满足 reverse_x == x//10 即可
            if reverse_x == x or reverse_x == x // 10:
                return True
            else:
                return False

    # 方法五: 进阶:不将整数转为字符串来解决: 不使用log函数
    # 复杂度: O(n)
    def isPalindrome8(self, x: int) -> bool:
        """
        只反转后面一半的数字!!(节省一半的时间)
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True
        else:
            reverse_x = 0
            while x > reverse_x:
                remainder = x % 10
                reverse_x = reverse_x * 10 + remainder
                x = x // 10
            # 当x为奇数时, 只要满足 reverse_x//10 == x 即可
            if reverse_x == x or reverse_x // 10 == x:
                return True
            else:
                return False



if __name__ == '__main__':
    # print(Solution.is_palindrome3(121))
    # print(Solution.is_palindrome3(10))
    # print(Solution.is_palindrome3(-121))
    x1 = '10'
    print(x1.startswith('10'))
    print(x1.endswith('10'))
