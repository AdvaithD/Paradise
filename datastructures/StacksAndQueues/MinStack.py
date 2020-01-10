# Problem Statement: (#155)
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) - - Push element x onto stack.
# pop() - - Removes the element on top of the stack.
# top() - - Get the top element.
# getMin() - - Retrieve the minimum element in the stack.


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x) -> None:
        currentMinimum = self.getMin()
        if currentMinimum == None or x < currentMinimum:
            currentMinimum = x
        self.stack.append((x, currentMinimum))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push((5))
obj.push((6))
obj.push((7))
# obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3, param_4)
