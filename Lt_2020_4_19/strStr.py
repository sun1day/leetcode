"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def solution(haystack: str, needle: str):
    # from collections import Counter
    # c = Counter()
    # todo 偷懒， 没达到练习算法的目的
    ret = haystack.find(needle)
    return ret


def solutions(haystack: str, needle: str):
    """Sunday 匹配机制"""
    # mapping = list(zip(enumerate(haystack)))
    # mapping = dict(zip(enumerate(haystack)))

    if len(haystack) < len(needle):
        return -1

    if (not haystack or not needle) or haystack == needle:
        return 0

    # 求出 字符串的长度
    length = len(haystack)

    # 偏移表
    mapping = {v: len(needle) - i for i, v in enumerate(needle)}
    mapping.update(other=len(needle) + 1)  # 添加其他情况偏移量

    # 指针
    index = 0

    # 如果 指针 + 模式串 的长度 必须小于主串的长度
    print(length)
    while index + len(needle) <= length:
        if haystack[index: index + len(needle)] == needle:
            return index

        # 此处不相同， 算偏移量
        off = mapping.get(haystack[index + len(needle)])  # 没有在模式串中
        if not off:
            index += mapping.get('other')
            continue

        index += off
    print(index)
    return -1


if __name__ == '__main__':
    print(solutions("mississippi", "pi"))

    # [1, 2, 3, 6,4 ,5]
    # [1, 2 ,3]
