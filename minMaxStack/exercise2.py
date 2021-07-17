class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.size = 0

    def push(self, x):
        if self.size ==0:
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)

        self.stack.append(x)
        self.size +=1
    
    def pop(self):
        temp = self.stack.pop()
        self.size -= 1
        if temp == self.min[-1]:
            self.min.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]
    
    def getAll(self):
        return self.stack
    
    def getMa


obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
