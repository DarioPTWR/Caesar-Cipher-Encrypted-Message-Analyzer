#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : CaesarCipher.py
#--------------------------------------------------------------

# Import relevant modules and classes
from Classes.OperationHistory import OperationHistory
from Classes.DataStructures.Deque import Deque

# Define CaesarCipher class
class CaesarCipher:
    """
    Class for performing Caesar Cipher encryption and decryption operations,
    along with maintaining an operation history and visualizing cipher transformations.
    """

    def __init__(self):
        """
        Constructor for the CaesarCipher class.
        Initializes the operation history manager and the deque for transformations,
        and sets the initial cipher key to 0.
        """
        self.history_manager = OperationHistory()  # History manager for operations
        self._deque = Deque()  # Deque for storing transformations
        self._key = 0  # Cipher key, initially set to 0

    def set_key(self, key):
        """
        Set the cipher key for encryption or decryption.
        :param key: Integer value representing the shift in the cipher.
        """
        self._key = key

    def get_key(self):
        """
        Get the current cipher key.
        :return: Integer value of the current cipher key.
        """
        return self._key

    def cipher(self, text, encrypt=True):
        """
        Perform encryption or decryption on the given text.
        :param text: String representing the text to be encrypted or decrypted.
        :param encrypt: Boolean indicating whether to encrypt (True) or decrypt (False).
        :return: String representing the result after performing the cipher.
        """
        result = self._perform_cipher(text, encrypt)
        operation_type = "encryption" if encrypt else "decryption"
        self.history_manager.add_operation(text, result, operation_type, self._key)
        return result

    def _perform_cipher(self, text, encrypt, shift=None):
        """
        Internal method to perform the Caesar cipher shift on the given text.
        :param text: String representing the text to be transformed.
        :param encrypt: Boolean indicating encryption or decryption.
        :param shift: Optional; specific shift value. If None, uses the object's key.
        :return: String representing the transformed text.
        """
        shift = shift if shift is not None else (self._key if encrypt else -self._key)
        result = ""

        for char in text:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                result += shifted_char
            else:
                result += char

        return result

    def visualize_transformation(self, text, start_shift, end_shift, direction="F"):
        """
        Visualize the transformation of text with varying cipher shifts.
        :param text: String to be transformed.
        :param start_shift: Starting shift value.
        :param end_shift: Ending shift value.
        :param direction: Direction of shift ('F' for forward, 'B' for backward).
        :return: List of strings representing the transformations.
        """
        self._deque.clear()  # Clearing the deque before new transformations
        if direction in ["F"]:
            for shift in range(start_shift, end_shift + 1):
                transformed_text = self._perform_cipher(text, encrypt=True, shift=shift)
                self._deque.add_to_rear(f"Forward Shift {shift}: {transformed_text}")

        if direction in ["B"]:
            backward_deque = Deque()  # Use a separate deque for backward transformations
            for shift in range(start_shift, end_shift + 1):
                transformed_text = self._perform_cipher(text, encrypt=False, shift=-shift)
                backward_deque.add_to_rear(f"Backward Shift {shift}: {transformed_text}")

            # Reverse the order of backward transformations before adding to the main deque
            while not backward_deque.is_empty():
                self._deque.add_to_front(backward_deque.remove_from_rear())

        # Convert deque items to a list for returning
        transformations_list = []
        while not self._deque.is_empty():
            transformations_list.append(self._deque.remove_from_front())

        return transformations_list

    def read_file(self, file_path):
        """
        Read and return the content of a file.
        :param file_path: Path to the file to be read.
        :return: String containing the content of the file.
        """
        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, text):
        """
        Write text to a file.
        :param file_path: Path to the file where the text will be written.
        :param text: Text to be written to the file.
        """
        with open(file_path, 'w') as file:
            file.write(text)

    def undo(self, operation_id):
        """
        Undo an operation based on its ID.
        :param operation_id: ID of the operation to be undone.
        """
        if self.history_manager.undo(operation_id):
            print(f"\nOperation with ID {operation_id} was successfully deleted.")
        else:
            print(f"\nOperation with ID {operation_id} does not exist.")

    def get_history(self):
        """
        Get the history of operations performed.
        :return: List of operation records.
        """
        return self.history_manager.get_history()
