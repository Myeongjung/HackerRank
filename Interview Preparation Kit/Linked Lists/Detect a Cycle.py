"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head == None:
        return false
    
    if head != head.next:
        if head.next == None or head.next.next == None:
            return False
        else:
            return has_cycle(head.next)
    else:
        return True