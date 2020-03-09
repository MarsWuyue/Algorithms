"""
基于链表实现链式队列
Author：Will
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedQue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int):
        node = Node(val)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
    
    def pop(self)-> int:
        if not self.head:
            return None
        if self.head == self.tail:
            self.tail = None
        value = self.head.val
        self.head = self.head.next
        return value
    
    def peek(self):
        if not self.head:
            return None
        return self.head.val

    def __repr__(self) -> str:
        cur = self.head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return " ".join(f"{num}" for num in nums)

if __name__ == "__main__":
    queue = LinkedQue()

    for i in range(5):
        queue.push(i)

    print(queue)
    
    for i in range(5):
        val = queue.pop()
        print(val)

    print(queue.pop()) # None

    queue.push(99)
    queue.push(100)
    print(queue)
    print(queue.peek()) # 99


        