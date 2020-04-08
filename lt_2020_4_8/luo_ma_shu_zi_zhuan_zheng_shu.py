"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

__author__ = 'Sun'


class Solution:
    @classmethod
    def roman_to_int(cls, s: str) -> int:
        """
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        IV             4
        IX             9
        XL             40
        XC             90
        CM             900
        CD             400
        :param s:
        :return:
        """
        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CM": 900,
            "CD": 400
        }
        import re
        # ret = re.findall(r'IV|IX|XL|XC|CM|CD', s)
        ret = re.findall(r'IV|IX|XL|XC|CM|CD', s)
        new_s = s
        sums = 0
        for item in ret:
            new_s = new_s.replace(item, '', 1)
            sums += dict_roman.get(item)
        for i in new_s:
            sums += dict_roman.get(i)
        return sums

    ##############看一下大佬的代码#################
    def one(self, s):
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CM": 900,
            "CD": 400
        }
        # todo 找到了规律 但是看起来太吃力了
        return sum(d.get(    s[ max(i - 1, 0) : i + 1 ],    d[n]    )     for i, n in enumerate(s))

    ###################################todo 另外一个大佬写的#######################################

    def two(self, s):

        # todo 这个 是真的好， 在左边的话 减去这个值， 右边的话加上这个值！！！！！！！！！！！！！！！！
        Roman2Int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Int = 0

        for index in range(len(s) - 1):
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]
            else:
                Int += Roman2Int[s[index]]

        return Int + Roman2Int[s[-1]]


if __name__ == '__main__':
    Solution.roman_to_int('MCMXCIV')
