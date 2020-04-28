"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

 

示例:

输入: "Hello World"
输出: 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/length-of-last-word
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(' ')
        print(s)
        l = s.split(' ')
        if not l:
            return 0

        return len(l[-1])

    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        sums = 0
        for num in digits[::-1]:
            print(num)
            sums += num * i
            i *= 10
        sums += 1

        return [int(i) for i in str(sums)]


if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3, 9]))
