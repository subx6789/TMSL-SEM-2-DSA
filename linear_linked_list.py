class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node contains key
        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Element not found")
            return

        prev.next = temp.next

    # Print list
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")


# Driver Code
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked List:")
ll.display()

ll.delete(20)

print("After Deletion:")
ll.display()