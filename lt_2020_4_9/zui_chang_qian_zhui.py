# _*_ coding = utf-8 _*_
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z
"""
from typing import List

__author__ = 'Jax'


def my_answer(lists: List[str]):
    if not lists:
        return ''
    start_str = lists[0]
    string = ''
    for s in start_str:
        string += s
        for item in lists[1:]:
            if item.startswith(string):
                continue
            return string[:-1]
    return string


def da_lao_dai_ma(lists):
    ret = zip(*lists)
    string = ''
    for i in ret:
        if len(set(i)) != 1:
            break
        string += i[0]

    return string


# print(my_answer(["flower", "flow", "flight"]))
# print(my_answer(["dog", "racecar", "car"]))

if __name__ == '__main__':
    # print(ord('f'))
    # print(ord('l'))
    # print(ord('o'))
    # print(ord('w'))
    # print('------------------')
    # print(ord('f'))
    # print(ord('l'))
    # print(ord('o'))
    # print(ord('w'))
    # print(ord('e'))
    # print(ord('r'))
    # print(list(zip(*['abc', 'qwe', 'qwert'])))
    print(da_lao_dai_ma(["flower", "flow", "flight"]))
