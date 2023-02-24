import linked_list

class Stack():
    '''
    LIFO structure
    '''
    def __init__(self, max_size=None):
        self.link_list = linked_list.LinkedList()
        self.max_size = max_size

    def push(self, value):
        if self.max_size and self.link_list.get_len() >= self.max_size:
            raise Exception('Stack is already full.')
        else:
            self.link_list.append_node(value)

    def pop(self):
        if self.link_list.is_empty():
            raise Exception('Cannot pop from an empty stack.')
        else:
            return self.link_list.pop_head()
        
    def count(self):
        return self.link_list.get_len()
    
    def isEmpty(self):
        return self.link_list.is_empty()
    
    def isFull(self):
        if self.max_size:
            return self.count >= self.max_size
        else:
            return False
        
    def peek(self, index):
        return self.link_list.get_value(index)
    
    def change(self, value, index):
        self.link_list.delete_node(index)
        self.link_list.add_node(value, index)

    def display(self):
            prev_node = None
            current_node = self.link_list.head
            for i in range(self.link_list.get_len()):
                print(current_node)
                prev_node = current_node
                current_node = prev_node.next_node



if __name__ == '__main__':

    my_stack = Stack()

    for i in range(10):
        my_stack.push(i)
    
    my_stack.display()

    length = my_stack.count()
    print('Length: ', length)

    for _ in range(length):
        print('Popped value: ', my_stack.pop())

    print('Is empty: ', my_stack.isEmpty())

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    print('Peek on index 1: ', my_stack.peek(1))

    my_stack.change(40, 2)
    print('Peek on index 2: ', my_stack.peek(2))