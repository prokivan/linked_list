class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
        print_data = self.head
        while print_data is not None:
            print(print_data.data)
            print_data = print_data.next

    def at_begining(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def at_between(self, middle_node, new_data):
        if middle_node is None:
            print('The mentioned node is absent')
            return
        new_node = Node(new_data)
        new_node.next = middle_node.next
        middle_node.next = new_node

    # def remove_node(self, remove_key):
    #     head_data = self.head
    #
    #     if head_data is not None:
    #         if head_data.data == remove_key:
    #             self.head = head_data.next
    #             head_data = None
    #             return
    #     while head_data is not None:
    #         if head_data == remove_key:
    #             break
    #         prev = head_data
    #         head_data = head_data.next
    #
    #     if head_data == None:
    #         return
    #     prev.next = head_data.next
    #     head_data = None
    def RemoveNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None


list1 = SLinkedList()
list1.head = Node('one')
e2 = Node('two')
e3 = Node('three')
list1.head.next = e2
e2.next = e3
list1.listprint()
print('\n')
list1.at_begining('fore')
list1.listprint()
print('\n')
list1.at_end('five')
list1.listprint()
print('\n')
list1.at_between(list1.head.next, 'six')
list1.listprint()
print('\n')
list1.RemoveNode('three')
list1.listprint()
