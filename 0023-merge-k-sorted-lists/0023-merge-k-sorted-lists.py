class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        result = None

        for i in range(len(lists)):
            result = self.mergeTwoLists(result, lists[i])

        return result

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next