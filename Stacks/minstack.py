class MinStack:

    def __init__(self):
        self.stack = [] #this is org stack
        self.min_stack=[] # min values stack 

    def push(self, val: int) -> None:
        self.stack.append(val) # pushes val into org stack
        #if there is no element in min_stack or else the val is less than min push it to min stack
        if not self.min_stack or val <= self.min_stack[-1] :
            self.min_stack.append(val) 

    def pop(self) -> None:
        val = self.stack.pop()
        #if now val is less than current min pop from min_stack too
        if val == self.min_stack[-1] :
            val = self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
       return self.min_stack[-1] 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()