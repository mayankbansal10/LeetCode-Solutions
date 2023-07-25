class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new = []
        for i in lists:
            while (i):
                new.append(i.val)
                i = i.next

        a = sorted(new, reverse=True)

        final = None
        for i in a:
            final = ListNode(i, final)

        return final
