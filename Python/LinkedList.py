class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_at_start(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def append_at_end(self, data):
        if self.head is None:
            self.append_at_start(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> '
            itr = itr.next
        llstr += 'Null'
        return llstr

ll = LinkedList()
print(ll.print_list())
ll.append_at_start(1)
ll.append_at_end(2)
print(ll.print_list())