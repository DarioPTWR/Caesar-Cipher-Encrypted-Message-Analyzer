#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : ActionPage.py
#--------------------------------------------------------------

# Import relevant libraries and modules
from Application.Utils import question, enter, print_row, display
from Application.Page import Pages

# Instantiate the LetterFrequency class to get letter frequency functions
from Classes.LetterFrequency import LetterFrequency
# Instantiate the InferCipher class to get infer caesar cipher key functions
from Classes.InferCipher import InferCipher
# Instantiate the TextAnalyzer class to batch process and decrypt txt files
from Classes.TextAnalyzer import AnalyzeEncryptedFile
# Instantiate the OperationHistory class
from Classes.OperationHistory import OperationHistory

class ActionPage(Pages):
    """
    Class ActionPage, inheriting from the Pages class. This class is designed to
    facilitate actions like encryption, decryption, and other operations related to
    Caesar cipher by executing a series of callback functions.
    """

    def __init__(self, caesarcipher, callbacks, **kwargs):
        """
        Constructor of the ActionPage class.

        :param caesarcipher: An instance of a CaesarCipher class. This object is used
                             to perform encryption and decryption operations.
        :param callbacks: A list of callback functions. Each function in this list
                          represents a specific action or operation that can be
                          performed in this application.
        :param kwargs: Additional keyword arguments that might be needed for initialization
                       in the superclass or for other purposes.
        """
        # Calling the constructor of the superclass (Pages) with the provided arguments.
        super().__init__(caesarcipher, **kwargs)

        # Storing the list of callback functions. These functions are intended to be
        # called later to execute various actions.
        self.callbacks = callbacks

    def __call__(self):
        # Iterating through each callback function in the list.
        for callback in self.callbacks:
            # Executing the callback function with the caesarcipher instance as an argument.
            callback(self.caesarcipher)
            
# Option 1 : Encrypting and Decrypting Messages
def encrypt_decrypt_message(caesarcipher):
    # Prompt the user to choose between encryption (E), decryption (D), or exit (X)
    choice = question('\nEnter "E" for Encrypt or "D" for Decrypt or "X" for Exit: ', mode='cipherchoice').upper()
    
    # Determine whether to encrypt or decrypt based on the user's choice
    if choice in ('E', 'D', 'X'):
        # If the choice is to encrypt, prompt the user to enter the text to be encrypted.
        if choice == 'E':
            text = question('\nPlease type text you want to encrypt:\n', mode='alpha')
        # If the choice is to decrypt, prompt the user to enter the text to be decrypted.
        elif choice == 'D':
            text = question('\nPlease type text you want to decrypt:\n', mode='alpha')
        # If the choice is to exit, return from the function without doing anything.
        else:
           return
            
        # Prompt the user to enter the key for the Caesar cipher and set it in the caesarcipher instance.
        caesarcipher.set_key(int(question('\nEnter the cipher key: ', mode='keyvalue')))

        # Use the cipher method to perform encryption or decryption
        encrypt = (choice == 'E')
        result = caesarcipher.cipher(text, encrypt=(choice == 'E'))

        # Print the original text and the result (encrypted or decrypted text).
        if encrypt:
            print(f'\nPlaintext:\t{text.upper()}\nCiphertext:\t{result.upper()}\n')
        else:
            print(f'\nCiphertext:\t{text.upper()}\nPlaintext:\t{result.upper()}\n')
            
        # Call the 'enter' function to pause the program, allowing the user to read the output.
        enter()
        
# Option 2 : Encrypting and Decrypting Text Files       
def encrypt_decrypt_file(caesarcipher):
    # Ask the user whether they want to perform encryption (E), decryption (D), or exit (X)
    choice = question('\nEnter "E" for Encrypt, "D" for Decrypt, or "X" for Exit: ', mode='cipherchoice')
    choice = choice.upper()

    # Determine whether to encrypt, decrypt, or exit based on the user's choice
    if choice in ("E", "D", "X"):

        # Execute if the user chooses encryption
        if choice == "E":
            # Ask for the input file to be encrypted
            textfile = question('\nPlease enter the file you want to encrypt: ', mode='fileinput')
            # Set the encryption key
            caesarcipher.set_key(int(question('\nEnter the cipher key: ', mode='keyvalue')))
            # Read the plaintext from the input file
            plaintext = caesarcipher.read_file(textfile)
            # Encrypt the plaintext
            ciphertext = caesarcipher.cipher(plaintext, encrypt=True)

            # Ask for the output file to save the encrypted text
            outputfile = question('\nPlease enter an output file: ', mode='fileoutput')
            # Write the ciphertext to the output file
            caesarcipher.write_file(outputfile, ciphertext)

        # Execute if the user chooses decryption
        elif choice == "D":
            # Ask for the input file to be decrypted
            cipherfile = question('\nPlease enter the file you want to decrypt: ', mode='fileinput')
            # Set the decryption key (must match the key used for encryption)
            caesarcipher.set_key(int(question('\nEnter the cipher key: ', mode='keyvalue')))
            # Read the ciphertext from the input file
            ciphertext = caesarcipher.read_file(cipherfile)
            # Decrypt the ciphertext
            plaintext = caesarcipher.cipher(ciphertext, encrypt=False)

            # Ask for the output file to save the decrypted text
            outputfile = question('\nPlease enter an output file: ', mode='fileoutput')
            # Write the decrypted plaintext to the output file
            caesarcipher.write_file(outputfile, plaintext)

        # Execute if the user wishes to return to the main menu
        else:
            return

    # Add new line spacing for better readability
    print()
    enter()
        
# Option 3 : Analyze letter frequency distribution (based on text file)
def letter_frequency(caesarcipher):
    # Ask the user for the file they want to analyze or exit ('X' for Exit)
    fileanalysis = question('\nPlease enter the file you want to analyze or "X" for Exit: ', mode='fileinput')
    
    # If the user chooses to exit, return from the function
    if fileanalysis == 'X':
        return
    
    # Read text from the specified file
    text = caesarcipher.read_file(fileanalysis)
    
    # Create an instance of LetterFrequency to analyze letter frequencies in the text
    letterfrequency = LetterFrequency(text)
    
    # Calculate letter frequencies in the text
    letterfrequency.calculate_letter_frequencies()
    
    # Get the display string for the letter frequencies with asterisks and the top 5 frequencies
    print('\n')
    print(letterfrequency.display_letter_frequency())
        
    # Add new line spacing for better readability
    print()
    enter()

# Option 4 : Infer the caesar cipher key from file
def infer_cipher_key(caesarcipher):
    # Ask the user for the file they want to analyze
    fileanalysis = question('\nPlease enter the file to analyze or "X" for Exit: ', mode='fileinput')
    
    # If the user chooses to exit, return from the function
    if fileanalysis == 'X':
        return
    
    # Enter the reference frequencies file: englishtext.txt
    referencefile = question('\nPlease enter the reference frequencies file: ', mode='frequencyfile')
    # Create an instance of InferCipher()
    infercipher = InferCipher()

    # Load the reference frequencies from the provided file
    infercipher.load_reference_frequencies(referencefile)
    
    # Read the text to be analyzed
    encrypted_text = caesarcipher.read_file(fileanalysis)
    
    # Infer the cipher key using the encrypted text
    inferred_key = infercipher.infer_cipher_key(encrypted_text)
    
    # Provide the inferred cipher key to the user
    print(f"The inferred cipher key is: {inferred_key}")
    
    # Ask the user if they want to decrypt the file using the key provided
    decryptwithkey = question('Would you want to decrypt this file using this key? y/n: ', mode='boolean').lower()
    
    # Conditional check if Y / N
    if decryptwithkey == 'y':
        # Decrypt the text using the inferred key
        decrypted_text, _ = infercipher.decrypt_text(encrypted_text)
        # Ask the user for an output file path
        outputfile = question('\nPlease enter a output file: ', mode='fileoutput')
        # Write the decrypted text to the file
        caesarcipher.write_file(outputfile, decrypted_text)
        # Return key
        print()
        enter()
    else:
        print('\nReturning you back to the main menu now....\n')
        enter()
        
# Option 5 : Analyze and sort encrypted files
def analyze_sort_file(fileanalyzer):
    # Ask the user for the folder they want to analyze
    folder = question('\nPlease enter the folder name or "X" for Exit: ', mode='directory')
    
    # If user chooses to exit, return from the function
    if folder == 'X':
        return
    
    # Initialize the AnalyzeEncryptedFile class with the folder name
    fileanalyzer = AnalyzeEncryptedFile(folder)
    
    # Call the method to analyze and sort encrypted files
    fileanalyzer.analyze_and_sort_encrypted_files()
    print()
    enter()
         
# Option 6 : View Cipher Transformations
def view_cipher_transformations(caesarcipher):
    text = question('\nEnter the text to visualize cipher shifts or "X" for Exit: ', mode='alpha')
    
    # Check if user entered 'X' to exit
    if text.upper() == 'X':
        return
    
    shift_values = question("\nEnter the start and end shift values, separated by a comma: ", mode='shiftvalue')
    start_shift, end_shift = map(int, shift_values.split(','))
    
    direction = question('\nEnter "F" for forward shift or "B" for backward shift: ', mode='shiftdirection').upper()

    # Cipher Transformations
    transformations = caesarcipher.visualize_transformation(text, start_shift, end_shift, direction)

    print(f"\nPerform Cipher Transformation For : {text}")
    
    if transformations:
        max_shift_type_width = max(len(trans.split(": ")[0]) for trans in transformations)
        max_transformed_text_width = max(len(trans.split(": ")[1]) for trans in transformations)

        if direction in ["F"]:
            print("\nForward Shift:")
            display([trans.split(": ") for trans in transformations if "F" in trans], max_shift_type_width, max_transformed_text_width)

        if direction in ["B"]:
            print("\nBackward Shift:")
            display([trans.split(": ") for trans in transformations if "B" in trans], max_shift_type_width, max_transformed_text_width)
    
    print()
    enter()

# Option 7 : Tracking History of Encryptions / Decryptions
history = OperationHistory()

# View Operations History Function
def view_history(caesarcipher):
    # Get the history of operations from the caesarcipher
    history = caesarcipher.get_history()
    
    # Check if there is no history
    if not history:
        print("\nNo past history found. Please perform encryption or decryption first.\n")
        enter()
        return

    # Define column widths and headers for the history table
    columns = [('ID', 6), ('Original Message', 25), ('Result Message', 25), ('Operation', 16), ('Shift Key', 10), ('Date', 16)]
    header, widths = zip(*columns)
    border = "+" + "+".join("-" * width for width in widths) + "+"

    # Print the table with history of encryption and decryption
    print()
    print(border)
    print_row(header, widths)
    print(border)

    for operation in history:
        # Unpack each element of the operation
        id, original_msg, result_msg, operation, datestamp, key = operation
        print_row([str(id), original_msg, result_msg, operation, str(key), datestamp], widths)
        print(border)
    print()   
    enter()

# Function to undo operation
def undo_operation(caesarcipher):
    # Get the history of operations from the caesarcipher
    history = caesarcipher.get_history()
    
    # Check if there is no history
    if not history:
        print("\nNo past history found. Please perform encryption or decryption first.\n")
        enter()
        return

    # Ask the user for the ID of the operation to delete
    operation_id = question("\nEnter the ID of the operation to delete: ", mode='operationid')
    
    # Undo the specified operation
    caesarcipher.undo(operation_id)
    print()
    enter()

# Function to show statistics
def show_statistics(caesarcipher):
    # Get statistics about the history of operations
    statistics = caesarcipher.history_manager.show_statistics()
    
    print("\nOperation Statistics:")
    headers = ["Metric", "Value"]
    data = [
        ("Total Cipher Operations", statistics['total_operations']),
        ("Encryption Operations", statistics['encryption_count']),
        ("Decryption Operations", statistics['decryption_count']),
        ("Most Common Cipher Key", f"{statistics['most_common_key']} (Used {statistics['most_common_key_count']} time(s))"),
        ("Average Text Length", f"{statistics['avg_message_length']} characters")
    ]

    # Determine column widths
    column_widths = [max(len(str(row[i])) for row in data) for i in range(2)]
    header_widths = [max(len(headers[i]), column_widths[i]) for i in range(2)]

    # Print header
    header = " | ".join(headers[i].ljust(header_widths[i]) for i in range(2))
    print(header)
    print("-" * len(header))

    # Print data rows
    for row in data:
        print(" | ".join(str(row[i]).ljust(header_widths[i]) for i in range(2)))
        
    print()
    enter()