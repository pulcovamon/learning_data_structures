import doubly_linked_list

class MyQueue():

    def __init__(self) -> None:
        self.link_list = doubly_linked_list.DoublyLinkList()

    def enqueue(self, value):
        self.link_list.add_head(value)

    def dequeue(self):
        return self.link_list.pop_tail()
    
    def access(self, index):
        return self.link_list.get_value(index)
    
    def search(self, value):
        return self.link_list.get_index(value)

    def count(self):
        return self.link_list.get_len()
    
    def isEmpty(self):
        return self.link_list.is_empty()
    
    def display(self):
            prev_node = None
            current_node = self.link_list.head
            for i in range(self.link_list.get_len()):
                print(current_node)
                prev_node = current_node
                current_node = prev_node.next_node



if __name__ == '__main__':

    my_queue = MyQueue()

    for i in range(10):
        my_queue.enqueue(i)

    my_queue.display()

    length = my_queue.count()
    print('Length: ', length)

    for _ in range(length):
        print('Dequeued: ', my_queue.dequeue())

    print('Is empty: ', my_queue.isEmpty())

    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    print('Searched index: ', my_queue.search(30))
    print('Accessed value: ', my_queue.access(0))