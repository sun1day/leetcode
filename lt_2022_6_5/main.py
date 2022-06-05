"""
606. 根据二叉树创建字符串
给你二叉树的根节点 root ，请你采用前序遍历的方式，将二叉树转化为一个由括号和整数组成的字符串，返回构造出的字符串。

空节点使用一对空括号对 "()" 表示，转化后需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。



示例 1：


输入：root = [1,2,3,4]
输出："1(2(4))(3)"
解释：初步转化后得到 "1(2(4)())(3()())" ，但省略所有不必要的空括号对后，字符串应该是"1(2(4))(3)" 。
示例 2：


输入：root = [1,2,3,null,4]
输出："1(2()(4))(3)"
解释：和第一个示例类似，但是无法省略第一个空括号对，否则会破坏输入与输出一一映射的关系。


提示：

树中节点的数目范围是 [1, 104]
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        1(2(4)())(3()())
        1(2(4()())())(3()())
        """
        # 1(2(4)())(3()())
        # 1(2(4()())())(3()())
        # 前序遍历
        s = ''
        if not root:
            return s

        s += f'{root.val}'
        if root.left:
            s += f'({self.tree2str(root.left)})'

        if root.right:
            if not root.left:
                s += '()'
            s += f'({self.tree2str(root.right)})'
        return s


if __name__ == '__main__':
    tns = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            right=TreeNode(val=4)
        ),
        right=TreeNode(
            val=3
        )

    )
    tns2 = TreeNode(
        val=1,
        left=TreeNode(
            val=2,
            right=TreeNode(val=4)
        ),
        right=TreeNode(
            val=3
        )

    )
    print(Solution().tree2str(tns2))
