from random import randint

class BinaryHeap():

    def __init__(self, capacity=1):
        self.heap_size = 0
        self.heap_capacity = capacity
        self.heap = [None] * capacity
        self.map = {}

    def __repr__(self) -> str:
        pass

    def getParentIndex(self, index):
        return (index - 1) // 2
        
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.heap_size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.heap_size
    
    def isFull(self):
        return self.heap_capacity <= self.heap_size
    
    def swap(self, index1, index2):
        val1 = self.heap[index1]
        val2 = self.heap[index2]
        self.heap[index1] = val2
        self.heap[index2] = val1

    def insert(self, value):
        if self.isFull():
            raise Exception('Heap is alreafy full.')
        else:
            index = self.heap_size
            self.heap[index] = value
            self.bubbleUp(index)
            self.heap_size += 1

    def bubbleUp(self, index):
        parent = self.getParentIndex(index)
        if self.hasParent(index) and self.heap[parent] > self.heap[index]:
            self.swap(index, parent)
            self.bubbleUp(parent)

    def poll(self):
        last_index = self.heap_size - 1
        value = self.heap[0]
        self.swap(0, last_index)
        self.heap[last_index] = None
        self.bubbleDown(0)
        self.heap_size -= 1
        return value

    def bubbleDown(self, index):
        left_index = self.getLeftChildIndex(index)
        right_index = self.getRightChildIndex(index)
        if left_index >= self.heap_size or right_index >= self.heap_size:
            return
        left_child = self.heap[left_index]
        right_child = self.heap[right_index]
        if not left_child:
            return
        current_node = self.heap[index]
        if current_node > left_child or (right_child and current_node > right_child):
            if not right_child or left_child < right_child:
                self.swap(left_index, index)
                self.bubbleDown(left_index)
            else:
                self.swap(right_index, index)
                self.bubbleDown(right_index)

    def remove(self, value):
        pass

                



if __name__ == '__main__':
    my_heap = BinaryHeap(10)

    for _ in range(10):
        val = randint(1, 10)
        my_heap.insert(val)

    print(my_heap.heap)

    for _ in range(10):
        print(my_heap.poll())