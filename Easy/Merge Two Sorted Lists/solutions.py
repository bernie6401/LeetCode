# from typing import Optional

# # Definition for singly-linked list.
# max_length = 50
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if self.get_length(list1) > max_length or self.get_length(list2) > max_length:
#             exit()
#         else:
#             main_list = list1 if self.get_length(list1) > self.get_length(list2) else list2
#             sub_list = list2 if main_list == list1 else list1

#         if not list1 or not list2:
#             return list1 or list2
        
#         if self.is_out_of_bounds(list1) or self.is_out_of_bounds(list2):
#             exit()
        
#         list1 = self.get_element(list1)
#         list2 = self.get_element(list2)
#         return self.list_2_ListNode(list(sorted(list1 + list2)))

    
#     def is_out_of_bounds(self, node: Optional[ListNode]) -> bool:
#         return node and (node.val < -100 or node.val > 100)
    
#     def get_length(self, node: Optional[ListNode]) -> int:
#         length = 0
#         while node:
#             length += 1
#             node = node.next
#         return length

#     def get_element(self, node: Optional[ListNode]) -> list:
#         list_all_element = []
#         while node:
#             list_all_element.append(node.val)
#             node = node.next
#         return list_all_element

#     def list_2_ListNode(self, node: list) -> Optional[ListNode]:
#         if not node:
#             return None
#         node.reverse()
#         result = ListNode(node[0])
#         for val in node[1:]:
#             tmp = ListNode(val)
#             tmp.next = result
#             result = tmp
#         return result

# if __name__ == "__main__":

#     # Example usage:
#     list1 = ListNode(1, ListNode(2, ListNode(4)))
#     list2 = ListNode(1, ListNode(3, ListNode(4)))
    
#     solution = Solution()
#     merged_list = solution.mergeTwoLists(list1, list2)
    
#     # Print merged list
#     while merged_list:
#         print(merged_list.val, end=" -> ")
#         merged_list = merged_list.next
#     print("None")

# from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 cur.next = list1
#                 list1 = list1.next
#             else:
#                 cur.next = list2
#                 list2 = list2.next
#             cur = cur.next
        
#         cur.next = list1 if list1 else list2
#         return dummy.next

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        while list1 and list2:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            
        return list1 if list1 else list2

if __name__ == "__main__":

    # Example usage:
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # Print merged list
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("None")