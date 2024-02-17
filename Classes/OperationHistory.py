#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : OperationHistory.py
#--------------------------------------------------------------

# Import necessary classes and libraries
from Classes.DataStructures.LinkedList import LinkedList
from datetime import datetime
import statistics

# Define the OperationHistory class
class OperationHistory:
    def __init__(self):
        # Initialize the OperationHistory object with an empty LinkedList to store operations
        self.history = LinkedList()  # Using LinkedList to store operations
        self.next_id = 1  # Initialize the next operation ID to 1

    def add_operation(self, original, result, operation, key):
        """
        Adds a new operation to the history.

        :param original: The original message.
        :param result: The result message after the operation.
        :param operation: The type of operation (ENCRYPTION or DECRYPTION).
        :param key: The cipher key used for the operation.
        """
        datestamp = datetime.now().strftime("%Y-%m-%d")  # Get the current date in the format "YYYY-MM-DD"
        operation_tuple = (self.next_id, original.upper(), result.upper(), operation.upper(), datestamp, key)
        self.history.append(operation_tuple)  # Append the operation to the history
        self.next_id += 1  # Increment the next operation ID

    def undo(self, operation_id):
        """
        Undo a specific operation by its ID.

        :param operation_id: The ID of the operation to undo.
        :return: True if the operation was undone successfully, False otherwise.
        """
        operation_id = int(operation_id)  # Convert the operation_id to an integer
        operation = self.history.find(operation_id)  # Find the operation with the given ID
        if operation:
            self.history.remove(operation_id)  # Remove the operation from the history
            return True  # Return True to indicate successful undo
        return False  # Return False if the operation was not found

    def get_history(self):
        """
        Get the entire history of operations.
        :return: A list of operation tuples representing the history.
        """
        operations = []
        current = self.history.head  # Start from the head of the linked list
        while current:
            operations.append(current.data)  # Append the operation data to the list
            current = current.next  # Move to the next node in the linked list
        return operations  # Return the list of operations
    
    def show_statistics(self):
        """
        Calculate and display statistics based on the operation history.
        :return: A dictionary containing various statistics.
        """
        operations = self.get_history()  # Get the entire history of operations

        total_operations = len(operations)  # Calculate the total number of operations
        encryption_count = sum(1 for op in operations if op[3] == 'ENCRYPTION')  # Count the number of encryption operations
        decryption_count = sum(1 for op in operations if op[3] == 'DECRYPTION')  # Count the number of decryption operations
        message_lengths = [len(op[1]) for op in operations]  # Create a list of message lengths

        # Calculate the most common cipher key
        key_frequency = {}
        for op in operations:
            key = op[5]
            if key in key_frequency:
                key_frequency[key] += 1
            else:
                key_frequency[key] = 1
        most_common_key = max(key_frequency, key=key_frequency.get, default='N/A')
        most_common_key_count = key_frequency.get(most_common_key, 0)  # Get the count of the most common key

        avg_message_length = int(round(statistics.mean(message_lengths))) if message_lengths else 0  # Calculate the average message length

        return {
            'total_operations': total_operations,
            'encryption_count': encryption_count,
            'decryption_count': decryption_count,
            'most_common_key': most_common_key,
            'most_common_key_count': most_common_key_count,
            'avg_message_length': avg_message_length
        }  # Return a dictionary containing the calculated statistics