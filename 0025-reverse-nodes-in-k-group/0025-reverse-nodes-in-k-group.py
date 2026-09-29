class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        count = 0

      
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        
        prev = None
        curr = head

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        head.next = self.reverseKGroup(curr, k)

        return prev