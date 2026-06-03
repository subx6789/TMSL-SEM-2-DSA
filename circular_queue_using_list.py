# Circular Queue implementation using a list in Python

MAX_SIZE = 5

class CircularQueue:
    def __init__(self):
        self.queue = [None] * MAX_SIZE
        self.front = -1
        self.rear = -1
        
    def is_full(self):
        return (self.rear + 1) % MAX_SIZE == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full! Cannot enqueue data.")
            return
        
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % MAX_SIZE
            
        self.queue[self.rear] = data
        print(f"Enqueued: {data}")
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue data.")
            return -1
        
        temp = self.queue[self.front]
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % MAX_SIZE
            
        print(f"Dequeued: {temp}")
        

if __name__ == "__main__":
    cq = CircularQueue()

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)

    # Attempt to insert when full
    cq.enqueue(60) 

    cq.dequeue()
    cq.dequeue()

    # Insert again to prove circular behavior
    cq.enqueue(70)
    cq.enqueue(80)

    cq.dequeue()