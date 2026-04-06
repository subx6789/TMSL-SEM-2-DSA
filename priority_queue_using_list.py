# Priority Queue implementation using a list in Python

MAX_SIZE = 100

class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == MAX_SIZE
    
    def enqueue(self, item, priority):
        if self.is_full():
            print(f"Queue overflow! Cannot enqueue item : {item}")
        else:
            self.queue.append((item, priority))
            print(f"Item enqueued : {item} with priority {priority}")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow! Cannot dequeue item from an empty queue.")
        else:
            # find highest priority (smallest number)
            min_index = 0
            for i in range(1, len(self.queue)):
                if self.queue[i][1] < self.queue[min_index][1]:
                    min_index = i
            
            item = self.queue.pop(min_index)
            print(f"Item dequeued : {item[0]} with priority {item[1]}")
            
    def peek(self):
        if self.is_empty():
            print("Queue is empty! Cannot peek item.")
        else:
            min_index = 0
            for i in range(1, len(self.queue)):
                if self.queue[i][1] < self.queue[min_index][1]:
                    min_index = i
            
            item = self.queue[min_index]
            print(f"Front item : {item[0]} with priority {item[1]}")


if __name__ == "__main__":
    
    pq = PriorityQueue()
    
    n = int(input("Enter number of elements: "))
    
    for _ in range(n):
        val = int(input("Enter element: "))
        pr = int(input("Enter priority (smaller = higher priority): "))
        pq.enqueue(val, pr)
        
    print(f"Current queue: {pq.queue}")
    
    pq.peek()
    
    print("Dequeuing all elements from the priority queue :- ")
    
    for _ in range(n):
        pq.dequeue()
        
    print(f"Current queue now : {pq.queue}")