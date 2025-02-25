# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val: int = 0, next: ListNode = None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0)
        result_tail = result

        node1 = l1
        node2 = l2

        carry = 0

        has_next = True 

        while has_next: 
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            
            val = val1 + val2 + carry 
            carry = val // 10
            
            node = ListNode(val = val % 10)
            print("new node: ", node)

            print("result_tail: ", result_tail)
            print("result ", result)

            result_tail.next = node

            print("result_tail 2: ", result_tail)
            print("result ", result)

            result_tail = result_tail.next

            print("result_tail 3: ", result_tail)
            print("result: ", result)

            if (node1 is not None and node1.next): 
                node1 = node1.next 
            else:
                node1 = None 

            if (node2 is not None and node2.next):
                node2 = node2.next
            else: 
                node2 = None 

            if (node1) or (node2) or (carry > 0): 
                has_next = True 
            else: 
                has_next = False

            print("=========")

        return result.next

