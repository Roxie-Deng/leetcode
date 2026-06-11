class MinStack:
    def __init__(self):
        self.stack = [(0,float('inf'))] # (data_stack, min_stack)

    def push(self, val: int) -> None:
        self.stack.append((val, min(val,self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
    # O(n);O(1)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()