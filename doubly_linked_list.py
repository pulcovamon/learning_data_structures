import linked_list

class Node(linked_list.Node):
    
    def __init__(self, data, next_node=None, prev_node=None):
        super().__init__(data, next_node)
        self.prev_node = prev_node
        self.tail = None

class DoublyLinkList(linked_list.LinkedList):
    '''
    Object for doubly linked list
    '''

    def __init__(self):
        super().__init__()
        self.count = 0

    def add_head(self, value):
        old_head = self.head
        super().append_node(value)
        if super().get_len() > 1:
            old_head.prev_node = self.head
        else:
            self.tail = self.head

    def add_tail(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new = Node(value, prev_node=self.tail)
            self.tail.next_node = new
            self.tail = new

    def pop_head(self):
        old_head = super().pop_head()
        self.head.prev_node = None
    
    def pop_tail(self):
        if self.is_empty():
            raise Exception('cannot pop from an empty list')
        else:
            old_tail = self.tail.data
            if super().get_len() > 1:
                self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.count -= 1
            return old_tail
        
    def clear(self):
        self.tail = None
        return super().clear()
            



if __name__ == '__main__':
    my_doubly_linked_list = DoublyLinkList()

    my_doubly_linked_list.add_head(10)
    my_doubly_linked_list.add_head(20)

    print('Head: ', my_doubly_linked_list.head)
    print('Tail: ', my_doubly_linked_list.tail)

    my_doubly_linked_list.add_tail(30)
    print('Get value of index 1: ', my_doubly_linked_list.get_value(1))

    print('Popped value from tail: ', my_doubly_linked_list.pop_tail())
    print('Length: ', my_doubly_linked_list.get_len())
    
    my_doubly_linked_list.clear()
    print('Length: ', my_doubly_linked_list.get_len())