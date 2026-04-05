# Queue implementation using a list in Python

MAX_SIZE = 100

class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == MAX_SIZE
    
    def enqueue(self, item):
        if self.is_full():
            print(f"Queue overflow! Cannot enqueue item : {item}")
        else:
            self.queue.append(item)
            print(f"Item enqueued : {item}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! Cannot dequeue item from an empty queue.")
        else:
            item = self.queue.pop(0)
            print(f"Item dequeued : {item}")
            
    def peek(self):
        if self.is_empty():
            print("Queue is empty! Cannot peek item.")
        else:
            item = self.queue[0]
            print(f"Front item : {item}")
            

if __name__ == "__main__":
    
    s = Queue()
    
    n = int(input("Enter the number of elements to enqueue (MAX_SIZE = 100) : "))
    
    for _ in range(n):
        s.enqueue(int(input("Enter the element to enqueue: ")))
        
    print(f"Current queue: {s.queue}")
    
    s.peek()
    
    print("Dequeuing all elements from the queue :- ")
    
    for _ in range(n):
        s.dequeue()
        
    print(f"Current queue now : {s.queue}")