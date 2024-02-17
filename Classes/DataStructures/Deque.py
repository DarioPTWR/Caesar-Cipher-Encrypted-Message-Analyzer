#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : Deque.py
#--------------------------------------------------------------

# Define a class Deque for deque data structure
class Deque:
    def __init__(self):
        self.items = []

    def add_to_front(self, item):
        """Add an item to the front of the deque."""
        self.items.insert(0, item)

    def add_to_rear(self, item):
        """Add an item to the rear of the deque."""
        self.items.append(item)

    def remove_from_front(self):
        """Remove and return an item from the front of the deque."""
        if self.items:
            return self.items.pop(0)
        return None 

    def remove_from_rear(self):
        """Remove and return an item from the rear of the deque."""
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the deque."""
        return len(self.items)
    
    def clear(self):
        self.items = []  # Reset the deque to an empty list