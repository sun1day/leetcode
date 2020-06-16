"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def square_root(x: int) -> int:
    # todo pass 太耗时
    # if x == 0:
    #     return 0
    # for i in range(1, x + 1):
    #     if i ** 2 == 0:
    #         return i
    #     if i ** 2 < x < (i + 1) ** 2:
    #         return i
    def inner(header, end, ident):
        middle = (header + end) // 2
        if middle == header or middle ** 2 == ident:
            return middle

        if middle ** 2 > ident:
            return inner(header, middle, ident)

        return inner(middle, end, ident)
    if x in [0, 1]:
        return x
    return inner(0, x, x)


if __name__ == '__main__':
    print(square_root(100))
