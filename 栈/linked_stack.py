"""
基于单链表实现链式栈

Author: Will
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, val: int)->bool:
        if not self.head:
            self.head = Node(val)
            return True
        node = Node(val)
        node.next = self.head
        self.head = node
        return True
    
    def pop(self)->int:
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def __repr__(self)->str:
        cur = self.head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return " ".join(f"{num}]" for num in nums)

if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(10):
        res = stack.push(i)
    print(stack)

    for i in range(10):
        val = stack.pop()
        print(val)

    print(stack.pop())