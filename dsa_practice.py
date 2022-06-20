
# Singly linked list
# class Node():
#     def __init__(self, val=None):
#         self.next = None
#         self.val = val
#     def print(self):
#         print(self.val)

# class SinglyLinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self,next):
#         if self.head is None:
#             self.head = next
#             self.tail = next
#         else:
#             self.tail.next = next
#             self.tail = next
    
#     def print(self):
#         trav = self.head
#         while trav is not None:
#             print(trav.val)
#             trav = trav.next


# ssl = SinglyLinkedList()
# ssl.append(Node(5))
# ssl.append(Node(-1))
# ssl.print()
    

# Graph DFS

adj_list = {
    0:{1,2},
    1:{0},
    2:{0,3,4},
    3:{0,1,2,4},
    4:{2,3},
}

visited = [False]*len(adj_list)

def dfs(at):
    if visited[at]:
        print(f'Revisiting {at}')
        return
    print(at)
    visited[at] = True
    neighbors = adj_list[at]
    for n in neighbors:
        dfs(n)

start_node = 4
dfs(start_node)
