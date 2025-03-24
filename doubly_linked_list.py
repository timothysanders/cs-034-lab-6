class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_after(self, current_node, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node
            
    def remove(self, current_node):
        successor_node = current_node.next
        predecessor_node = current_node.prev
        
        if successor_node is not None:
            successor_node.prev = predecessor_node
            
        if predecessor_node is not None:
            predecessor_node.next = successor_node
            
        if current_node is self.head:
            self.head = successor_node
        
        if current_node is self.tail:
            self.tail = predecessor_node
    
    def ListTraverse(self):
        current_node = self.head // Start at head

        while (current_node is not None):
            print(current_node.data, end = " ")
            current_node = current_node.next

    '''def search(self, target_node):
        pass'''
    
    
if __name__ == "__main__":
    num_list = DoublyLinkedList()
    
    node_1 = Node(14)
    node_2 = Node(2)
    node_3 = Node(20)
    node_4 = Node(31)
    node_5 = Node(16)
    node_6 = Node(55)
    
    num_list.append(node_1)
    num_list.append(node_2)
    num_list.append(node_3)
    
    num_list.prepend(node_4)
    
    num_list.insert_after(node_2, node_5)
    num_list.insert_after(node_3, node_6)
    
    print("List after adding nodes:", end = " ")
    node = num_list.head
    while node != None:
        print(node.data, end =" ")
        node = node.next
    print()
    
    num_list.remove(node_6) # Remove the tail
    num_list.remove(node_4) # Remove the head
   
    print("List after removing nodes:", end = " ")
    node = num_list.head
    while node != None:
        print(node.data, end = " ")
        node = node.next
    print()
