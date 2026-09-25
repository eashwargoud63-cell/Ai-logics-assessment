class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_two_numbers(l1, l2):
    carry = 0
    dummy = ListNode()
    cur = dummy
    while l1 or l2 or carry:
        s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        cur.next = ListNode(s % 10)
        cur = cur.next
        carry = s // 10
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next
def build(vals):
    head = cur = ListNode(vals[0])
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head
def to_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return " ".join(res)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

print(to_list(add_two_numbers(build(a), build(b))))