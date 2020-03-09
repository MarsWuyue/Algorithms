"""
基于数组实现队列

Author: Will
"""

class ArrayQue:
    def __init__(self, capacity: int):
        self.data = [float('inf')] * capacity
        self.head = self.tail = 0
        self.capacity = capacity

    def push(self, val)->bool:
        if self.head != 0:
            self._move_to_head()

        if self._full():
            return False
        self.data[self.tail] = val
        self.tail += 1
        return True
    
    def pop(self)->int:
        if self._empty():
            return None
        val = self.data[self.head]
        self.head += 1
        return val

    def peek(self)->int:
        if self._empty():
            return None
        return self.data[self.head]

    def _full(self)->bool:
        return self.tail - self.head == self.capacity

    def _empty(self)->bool:
        return self.head == self.tail

    def _move_to_head(self):
        n = self.tail - self.head
        self.data[: n] = self.data[self.head : self.tail]
        self.tail -= self.head
        self.head = 0

if __name__ == "__main__":
    queue = ArrayQue(5)
    for j in range(2): # 两次为了验证 move_to_head
        for i in range(5):
            queue.push(i)
        
        for i in range(5):
            val = queue.pop()
            print(val)

    print(queue.pop()) # None

    queue.push(99)
    queue.push(100)
    print(queue.peek()) # 99


    
