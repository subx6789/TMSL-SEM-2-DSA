class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue (Insert)
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    # Dequeue (Delete)
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        deleted = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return deleted

    # Peek Front Element
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None

        return self.front.data

    # Display Queue
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front

        print("Front -> ", end="")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print("<- Rear")


# Driver Code
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

print("Front Element:", q.peek())

print("Deleted:", q.dequeue())

print("After Dequeue:")
q.display()