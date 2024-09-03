
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        check_node = head
        lenght = 1
        
        while check_node.next:
            check_node = check_node.next
            lenght += 1
        
        if lenght == 1 and n == 1:
            head.val = ''
            return head
        
        if lenght == n:
            return head.next
        
        nodeChange = head
        for _ in range(lenght - n - 1):
            nodeChange = nodeChange.next
        nodeChange.next = nodeChange.next.next
        return head