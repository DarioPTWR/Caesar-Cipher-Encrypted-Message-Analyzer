#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : GUI.py
#--------------------------------------------------------------

# Import relevant libraries and modules
from ActionPage import (
    ActionPage, 
    encrypt_decrypt_message, 
    encrypt_decrypt_file, 
    letter_frequency, 
    infer_cipher_key, 
    analyze_sort_file, 
    view_cipher_transformations, 
    view_history, 
    undo_operation,
    show_statistics
    )
from SelectionPage import SelectionPage
from Classes.CaesarCipher import CaesarCipher
from Application.Utils import enter

# Instantiate a class called menus
# This class is used to store functions relating to the selection menus of the application (starting application, selecting different choices, exiting application)
class GUI():
    def __init__(self):
        
        self.active = True
        self.caesarcipher = CaesarCipher()

        # Set up the program and connect the respective pages
        self.encrypt_decrypt_message = ActionPage(self.caesarcipher, [encrypt_decrypt_message])
        self.encrypt_decrypt_file = ActionPage(self.caesarcipher, [encrypt_decrypt_file])
        self.letter_frequency = ActionPage(self.caesarcipher, [letter_frequency])
        self.infer_cipher_key = ActionPage(self.caesarcipher, [infer_cipher_key])
        self.analyze_sort_file = ActionPage(self.caesarcipher, [analyze_sort_file])
        self.view_cipher_transformations = ActionPage(self.caesarcipher, [view_cipher_transformations])
  
        # Function for submenu for option 7 : History Recorder
        self.history_tracker = SelectionPage(self, self.caesarcipher, {
            "View Encryption/Decryption History": lambda: view_history(self.caesarcipher),
            "Show Statistics of Operations": lambda: show_statistics(self.caesarcipher),
            "Delete Past Operations": lambda: undo_operation(self.caesarcipher),
            "Return to Main Menu": lambda: True
        }, is_submenu=True)
    
        # Function for Main Selection Menu
        self.main_menu = SelectionPage(self, self.caesarcipher, {
                "Encrypt/Decrypt Message": self.encrypt_decrypt_message,
                "Encrypt/Decrypt File": self.encrypt_decrypt_file,
                "Analyze letter frequency distribution": self.letter_frequency,
                "Infer caesar cipher key from file": self.infer_cipher_key,
                "Analyze, and sort encrypted files": self.analyze_sort_file,
                "View caesar cipher shift transformations": self.view_cipher_transformations,
                "View operation history of encryption/decryption": self.history_tracker,
                "Exit": self.exit
            })
        
    # Function for Show Title of Application
    def start(self):
        print("")
        print("*" * 57)
        print("*" + f"{' ST1507 DSAA: Welcome to:':<55}" + "*")
        print("*" + f"{' ':<55}" + "*")
        print("*" + f"{'     ~ Caesar Cipher Encrypted Message Analyzer ~':<55}" + "*")
        print("*" + f"{'':-<55}" + "*")
        print("*" + f"{' ':<55}" + "*")
        print("*" + f"{'   - Done by: Dario Prawara Teh Wei Rong(2201858)':<55}" + "*")
        print("*" + f"{'   - Class DAAA/2B/04':<55}" + "*")
        print("*" * 57)
        print("\n" * 1)
        enter()
            
        while self.active:
            self.main_menu()
    
    # Function to Exit Application
    def exit(self):
        print('\nBye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer\n')
        self.active = False
        