# Stack implementation using a list in Python

MAX_SIZE = 100

class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == MAX_SIZE
    
    def push(self, item):
        if self.is_full():
            print(f"Stack overflow! Cannot push item : {item}")
        else:
            self.stack.append(item)
            print(f"Item pushed : {item}")
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop item from an empty stack.")
        else:
            item = self.stack.pop()
            print(f"Item popped : {item}")
            
    def peek(self):
        if self.is_empty():
            print("Stack is empty! Cannot peek item.")
        else:
            item = self.stack[-1]
            print(f"Top item : {item}")
            

if __name__ == "__main__":
    
    s = Stack()
    
    n = int(input("Enter the number of elements to push (MAX_SIZE = 100) : "))
    
    for _ in range(n):
        s.push(int(input("Enter the element to push: ")))
        
    print(f"Current stack: {s.stack}")
    
    s.peek()
    
    print("Popping all elements from the stack :- ")
    
    for _ in range(n):
        s.pop()
        
    print(f"Current stack now : {s.stack}")