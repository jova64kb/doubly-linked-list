class Node:
    def __init__(self, data = None):
        self.prev = None
        self.next = None
        self.data = data

def insert(head, data):
    cur = head
    while cur.next != None:
        cur = cur.next
    new_node = Node(data)
    new_node.prev = cur
    cur.next = new_node

def delete(head, data):
    cur = head
    prev = None
    while cur != None:
        if cur.data == data:
            if prev != None:
                cur.next.prev = prev 
                prev.next = cur.next
                break
            else:
                print('error: you tried to delete HEAD.')
                print('use delete_head function.')
                break
        else:
            prev = cur
        cur = cur.next

def delete_head(head):
    return head.next

head = Node('node_0')
insert(head, 'node_1')
insert(head, 'node_2')
insert(head, 'node_3')

cur = head
while cur != None:
    print(f'prev: {None if cur.prev == None else cur.prev.data}')
    print(f'cur: {cur.data}')
    print(f'next: {None if cur.next == None else cur.next.data}')
    print('------')
    cur = cur.next

delete(head, 'node_1')
print('deleted: node_1')
cur = head
while cur != None:
    print(f'prev: {None if cur.prev == None else cur.prev.data}')
    print(f'cur: {cur.data}')
    print(f'next: {None if cur.next == None else cur.next.data}')
    print('------')
    cur = cur.next

