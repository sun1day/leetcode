"""
1309. 解码字母到整数映射
给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

字符（'a' - 'i'）分别用（'1' - '9'）表示。
字符（'j' - 'z'）分别用（'10#' - '26#'）表示。
返回映射之后形成的新字符串。

题目数据保证映射始终唯一。

示例 1：

输入：s = "10#11#12"
输出："jkab"
解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
示例 2：

输入：s = "1326#"
输出："acz"


提示：
1 <= s.length <= 1000
s[i] 只包含数字（'0'-'9'）和 '#' 字符。
s 是映射始终存在的有效字符串。
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        """
        1-9
        10-26
        """

        def str_number_2_string(string_num) -> str:
            return chr(int(string_num) + 96)

        # 循环
        length = len(s)
        _string = ''

        i = 0
        while 1:
            if i >= length:
                return _string

            flag_idx = i + 2
            if flag_idx >= length:
                _string += str_number_2_string(s[i])
                i += 1
                continue

            if s[flag_idx] == '#':
                _string += str_number_2_string(s[i]+s[i + 1])
                i += 3
                continue

            _string += str_number_2_string(s[i])
            i += 1





        # _string = ''
        # ret = ''
        # for idx in range(length):
        #     if s[idx] == '#':
        #         ret += str_number_2_string(_string)
        #         _string = ''
        #         continue
        #
        #     flag_idx = idx + 2
        #
        #     if s[flag_idx] == '#':
        #         _string = s[idx] + s[idx + 1]
        #     # ret += str_number_2_string(s[idx])
        #
        # return ret


if __name__ == '__main__':
    print(Solution().freqAlphabets('11'))
