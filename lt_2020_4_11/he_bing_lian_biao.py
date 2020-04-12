"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

__all__ = 'Jax'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'{self.val}'
    # def nexts(self):
    #     return self.next


def solution(l1: ListNode, l2: ListNode):
    """都是升序"""
    p = rst = ListNode(None)  ## 新建节点和指针
    while True:
        try:
            while l1.val <= l2.val:  # 若l1更小，`p.next`就指向l1,同时更新l1，p节点
                p.next = l1
                l1, p = l1.next, p.next
            while l1.val > l2.val:  # 若l2更小，`p.next`就指向l2,同时更新l2，p节点
                p.next = l2
                l2, p = l2.next, p.next
        except:
            break  ## 发生异常时，一定l1/l2至少一个为None了
    p.next = l1 or l2  ## 接上不为None的节点
    return rst.next  ##返回新建指针


def solution_two(l1: ListNode, l2: ListNode):
    """
    todo 看不懂啊, 链表， 需要研究一下
    :param l1:
    :param l2:
    :return:
    """
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = solution_two(l1.next, l2)

    return l1 or l2


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n4.next = n5
    n5.next = n6
    ret = solution_two(n1, n4)
    while ret.next:
        print(ret)
        ret = ret.next
    # print(n1, n2)
    # print(n1 < n2)
    # n1.val, n2.val = n2.val, n1.val
    # print(n1.next)
