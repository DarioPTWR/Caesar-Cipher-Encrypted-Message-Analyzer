#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : TextAnalyzer.py
#--------------------------------------------------------------

# Import necessary classes and libraries
import os
from Classes.LetterFrequency import LetterFrequency
from Classes.CaesarCipher import CaesarCipher
from Classes.InferCipher import InferCipher

# Define the AnalyzeEncryptedFile class
class AnalyzeEncryptedFile:
    def __init__(self, directory):
        # Initialize the LetterFrequency class to calculate letter frequencies
        self.letterfrequency = LetterFrequency()
        self.directory = directory
        self.decrypted_files = []  # Store decrypted file information as tuples (key, original_file, decrypted_text)
        self.log_entry = []  # Store log entries for decryption operations

    def reset(self):
        # Re-initialize the InferCipher and CaesarCipher classes to prevent stateful instances
        self.infercipher = InferCipher()
        self.caesarcipher = CaesarCipher()

    def read_encrypted_files(self):
        """
        Read and return a list of all files in the specified directory.
        :return: A list of file names.
        """
        # List all the files in that folder
        return [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]

    def decrypt_files(self, files):
        """
        Decrypt a list of files using the CaesarCipher and InferCipher classes.
        Re-initialize the classes to prevent stateful instances during batch processing of files.
        :param files: A list of file names to decrypt.
        """
        for file in files:
            file_path = os.path.join(self.directory, file)

            # Re-initialize the InferCipher class to infer the encryption key
            # Prevent stateful instances for the classes
            self.reset()

            # Assume the English text reference file is one level up from the encrypted files directory
            reference_freq_path = os.path.join(self.directory, '..', 'englishtext.txt')
            self.infercipher.load_reference_frequencies(reference_freq_path)

            encrypted_text = self.caesarcipher.read_file(file_path)
            decrypted_text, key = self.infercipher.decrypt_text(encrypted_text)
            self.decrypted_files.append((key, file, decrypted_text))

    def sort_and_write_files(self):
        """
        Sort decrypted files by their encryption keys and write them to new files.
        """
        self.decrypted_files.sort(key=lambda x: x[0])

        for i, (key, original_file, decrypted_text) in enumerate(self.decrypted_files, 1):
            decrypted_file_name = f'file{i}.txt'
            print(f"Decrypting: {original_file} with key: {key} as: {decrypted_file_name}\n")
            decrypted_file_path = os.path.join(self.directory, decrypted_file_name)
            self.caesarcipher.write_file(decrypted_file_path, decrypted_text)
            self.log_entry.append(f"Decrypting: {original_file} with key: {key} as: {decrypted_file_name}")

    def write_log_file(self):
        """
        Write a log file with decryption details.
        """
        log_file_path = os.path.join(self.directory, 'log.txt')
        self.caesarcipher.write_file(log_file_path, '\n'.join(self.log_entry))

    def analyze_and_sort_encrypted_files(self):
        """
        Analyze and sort encrypted files using the defined methods.
        """
        files = self.read_encrypted_files()
        self.decrypt_files(files)
        self.sort_and_write_files()
        self.write_log_file()