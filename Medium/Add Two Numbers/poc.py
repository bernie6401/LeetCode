# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        result = []
        a = 0
        b = 0
        for i in range(len(l1)):
            a += l1[i] * (10 ** i)
        for i in range(len(l2)):
            b += l2[i] * (10 ** i)
        a += b
        a = str(a)
        for i in range(len(a)):
            result.append(int(a[len(a) - i - 1]))
        return result


init = Solution()
print(init.addTwoNumbers([2,4,3], [5,6,4]))
print(init.addTwoNumbers([0], [0]))
print(init.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))