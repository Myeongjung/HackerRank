class MyQueue(object):
    def __init__(self):
        self.l = []
    
    def peek(self):
        return(self.l[0])
        
    def pop(self):
        self.l.pop(0)
        return(self.l)
        
    def put(self, value):
        self.l.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())