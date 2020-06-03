# **** LINKED LIST *******

# creating a node

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # create the linkedlist

# class LinkedList:
#     def __init__(self):
        
#         self.head = None


# if __name__ == '__main__':
#     # assining the value of LinkedList in llist
#     llist = LinkedList()

#     # adding the node to the LinkedList

#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)

#     # connecting the linkedlist
    
#     llist.head.next = third
#     # second.next = third

#     while llist.head != None:
#         print(llist.head.data)
#         llist.head = llist.head.next

# traversing a linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     # adding a new Node before the head node

#     def __init__(self , new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#     #inserting a new node after a node
#     def __init__(self , prev_node ,new_datas):

#         if prev_node is None:
#             print("prev node not present")
#             return

#         new_node = Node(new_datas)
#         new_node.next = prev_node.next
#         prev_node.next = new_node
    
#     #inserting a node at the end
#     def __init__(self,new_data):
#        newnode = Node(new_data)

#        if (self.head == None):

#            self.head = Node
#            return
           
#            last = self.head
#            while (last.next):
#             last = la
           










         
# if __name__ == '__main__':

#     llist = LinkedList()