class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

        print(data, "pushed")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        popped = self.top.data
        self.top = self.top.next

        return popped

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None

        return self.top.data

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top

        print("Top -> ", end="")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Driver Code
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top Element:", s.peek())

print("Popped:", s.pop())

s.display()