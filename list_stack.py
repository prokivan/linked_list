class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push_(self, new_data):
        new_node = Node(new_data)
        if not new_node:
            return
        new_node.next = self.head
        self.head = new_node

    def pop_(self):
        if self.is_empty():
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def peek(self):
        if not self.is_empty():
            return self.head.data
        return


stack = Stack()
stack.push_(11)
stack.push_(22)
stack.push_(33)
stack.push_(44)
print(stack.peek())
stack.pop_()
stack.pop_()
print(stack.peek())
