"""
基于数组实现有限顺序栈

Author: Will
"""

class ArrayStack:
    def __init__(self, capacity: int):
        self.data = [float('inf')] * capacity
        self.size = 0
        self.capacity = capacity

    def push(self, val: int)->bool:
        if self._full():
            return False

        self.data[self.size] = val
        self.size += 1
        return True

    def pop(self)->int:
        if self._empty():
            return None
        self.size -= 1
        return self.data[self.size]
    
    def _full(self)->bool:
        return self.size == self.capacity

    def _empty(self)->bool:
        return self.size == 0

if __name__ == "__main__":
    stack = ArrayStack(10)
    for i in range(10):
        res = stack.push(i)
        print(res)

    print(stack.push(11))

    for i in range(10):
        val = stack.pop()
        print(val)
    
    print(stack.pop())