class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'Node value: {self.data}'


class LinkedList:
    '''
    Linear data structure which stores data in nodes.
    Attributes: head (first node)
    '''

    def __init__(self):
        self.head = None
        # podtržítko: 1. nemám na to sahat, 2. count je častý slovo, nechci, aby se mlátilo s jinou proměnnou, protected and private proměnná
        self.count = 0

    def is_empty(self):
        return self.head is None
    
    def get_len(self):
        return self.count
    
    def append_node(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.count += 1

    def get_index(self, value):
        prev_node = None
        current_node = self.head
        for i in range(self.count):
            if current_node.data == value:
                return i
            else:
                prev_node = current_node
                current_node = prev_node.next_node
        return 'Value not in linked list'

    def get_value(self, index):
        if index >= self.count:
            raise IndexError('Index not in linked list')
        elif index == 0:
            return self.head.data
        else:
            prev_node = None
            current_node = self.head
            for _ in range(index):
                prev_node = current_node
                current_node = prev_node.next_node
            return current_node.data
        
    def add_node(self, value, index):
        if index == 0:
            self.append_node(value)
        elif index > self.count:
            raise IndexError('Index not in linked list')
        else:
            prev_node = None
            current_node = self.head
            for _ in range(index):
                prev_node = current_node
                current_node = prev_node.next_node
            current_node = Node(value, current_node)
            prev_node.next_node = current_node
            self.count += 1

    def pop_head(self):
        if self.is_empty():
            raise Exception('Cannot remove head from an empty linked list')
        else:
            old_head = self.head.data
            self.head = self.head.next_node
            self.count -= 1
            return old_head

    def delete_node(self, index):
        if index >= self.count:
            raise IndexError('Index not in linked list')
        elif index == 0:
            self.delete_head()
        else:
            prev_node = None
            current_node = self.head
            for _ in range(index):
                prev_node = current_node
                current_node = prev_node.next_node
            if current_node.next_node == None:
                current_node = None
                prev_node.next_node = None
            else:
                prev_node.next_node = current_node.next_node
                current_node = None
            self.count -= 1

    def into_array(self):
        if self.is_empty():
            return []
        else:
            array = []
            prev_node = None
            current_node = self.head
            for _ in range(self.count):
                array.append(current_node.data)
                prev_node = current_node
                current_node = prev_node.next_node
            return array
        

    def clear(self):
        self.head = None
        self.count = 0
    


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.append_node(10)
    linked_list.append_node(20)
    linked_list.append_node(30)

    print('Length: ', linked_list.get_len())

    val1 = linked_list.get_value(0)
    val2 = linked_list.get_value(1)
    val3 = linked_list.get_value(2)
    print('Get values: ', val1, val2, val3)

    ind1 = linked_list.get_index(10)
    ind2 = linked_list.get_index(20)
    ind3 = linked_list.get_index(30)
    ind4 = linked_list.get_index(40)
    print('Get indices: ', ind1, ind2, ind3, ind4)

    linked_list.add_node(40, 2)
    print('Values of index 2 and 3: ', linked_list.get_value(2), linked_list.get_value(3))

    popped = linked_list.pop_head()
    print('Popped value, value of index 0: ', popped ,linked_list.get_value(0))

    linked_list.delete_node(2)
    print('Length: ', linked_list.get_len())

    print('Array: ', linked_list.into_array())

    linked_list.clear()
    print('Is empty: ', linked_list.is_empty())