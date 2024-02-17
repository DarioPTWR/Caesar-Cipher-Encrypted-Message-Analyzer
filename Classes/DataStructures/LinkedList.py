#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : LinkedList.py
#--------------------------------------------------------------

# Import relevant modules and libraries
from .Node import Node

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def find(self, operation_id):
        current = self.head
        while current:
            if current.data[0] == operation_id:
                return current.data
            current = current.next
        return None

    def remove(self, operation_id):
        current = self.head
        prev = None
        while current:
            if current.data[0] == operation_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  
            prev = current
            current = current.next
        return False 