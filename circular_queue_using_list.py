# Circular Queue implementation using a list in Python

MAX_SIZE = 100

class CircularQueue:
    def __init__(self):
        self.queue = [None] * MAX_SIZE
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % MAX_SIZE == self.front

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue overflow! Cannot enqueue item : {item}")
        else:
            if self.is_empty():
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % MAX_SIZE
            self.queue[self.rear] = item
            print(f"Item enqueued : {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! Cannot dequeue item from an empty queue.")
        else:
            item = self.queue[self.front]
            if self.front == self.rear:
                # Queue becomes empty
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % MAX_SIZE
            print(f"Item dequeued : {item}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty! Cannot peek item.")
        else:
            print(f"Front item : {self.queue[self.front]}")

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            i = self.front
            elements = []
            while True:
                elements.append(self.queue[i])
                if i == self.rear:
                    break
                i = (i + 1) % MAX_SIZE
            print("Current queue:", elements)


if __name__ == "__main__":
    
    q = CircularQueue()
    
    n = int(input("Enter the number of elements to enqueue (MAX_SIZE = 100): "))
    
    for _ in range(n):
        q.enqueue(int(input("Enter the element to enqueue: ")))
        
    q.display()
    
    q.peek()
    
    print("Dequeuing all elements from the queue :- ")
    
    for _ in range(n):
        q.dequeue()
        
    q.display()