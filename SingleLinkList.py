from asyncio.windows_events import NULL
from contextlib import nullcontext
from email import header


class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkList:
    def __init__(self):
        self.head=None

    def push_front(self,val):
        list_node=ListNode(val,next=self.head)
        self.head=list_node

    def push_back(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        out,cur=[],self.head
        while cur:
            out.append(cur.val)
            cur=cur.next
        return out

ll = LinkList()

    # Test pushing to the back
ll.push_back(10)
ll.push_back(20)
print(ll.to_list())  # Expected Output: [10, 20]

    # Test pushing to the front
ll.push_front(5)
print(ll.to_list())









