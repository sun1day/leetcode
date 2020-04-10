"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""

__author__ = 'Jax'


def solution(string: str) -> bool:
    # todo 栈思想， 先进后出， 与括号的排列顺序是一样的.
    str_l = ('{', '[', '(')
    str_r = ('}', ']', ')')
    d = {
        '{': '}',
        '[': ']',
        '(': ')'
    }
    if len(string) == 0:
        return True
    if len(string) % 2 != 0:
        return False
    if string.startswith(str_r) or string.endswith(str_l):
        return False
    stack = [0]
    for s in string:
        if s in str_l:
            stack.append(s)
            continue
        ls = stack.pop()
        if d[ls] != s:
            return False
    return True


if __name__ == '__main__':
    print(solution('{[]}'))
    print(solution('()[]{}'))
    print(solution('([)]'))
    print(solution('{[]}'))
