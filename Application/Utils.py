#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : Utils.py
#--------------------------------------------------------------

# Import relevant libraries and modules
import os
import textwrap

# Enter Key Function
def enter():
    input("Press enter key, to continue....")
    
# Input Validation for User Inputs - Checks for any errors in inputs
def valid_input(text: str, mode: str, min_range: int = None, max_range: int = None, is_submenu: bool = False) -> list([bool, str]):
    
    # modes : Type of Validation / Input Type from users
    modes = ['integer', 'alpha', 'boolean', 'fileinput', 'fileoutput', 'keyvalue', 'cipherchoice', 'directory', 'operationid', 'shiftdirection', 'shiftvalue', 'frequencyfile']
   
    # Check if input type is one of the above
    if mode not in modes:
        raise ValueError(f"Invalid validation input type. Expected one of: {modes}")
       
    # Check input of choices for the main menu
    
    # Check if input type is an integer
    if mode == 'integer':
        error_msg = f'\nOnly options between 1 and {max_range} are available, please try again:\n' if not is_submenu else f'\nPlease select a valid option:\n'
        return (
            text.isnumeric() and
            int(text) >= min_range and int(text) <= max_range  
        ), error_msg
        
    # Check if input type is a valid cipher key
    elif mode == 'keyvalue':
        try:
            key_value = int(text)
        except ValueError:
            return False, '\nPlease only enter numbers between -25 and 25.'

        if -25 <= key_value <= 25:
            return True, None
        else:
            return False, '\nPlease only enter numbers between -25 and 25.'
        
    # Check if input type is either E or D for cipher choice
    elif mode == 'cipherchoice':
        return (
            text.upper() == 'E' or
            text.upper() == 'D' or
            text.upper() == "X"
        ), f'\nPlease enter only "E", "D" or "X" to proceed.'
        
    # Check that shift direction is valid either F, B or H
    elif mode == 'shiftdirection':
        return (
            text.upper() == 'F' or
            text.upper() == 'B' 
        ), f'\nPlease enter only "F" or "B" to proceed.'
        
    # Check that shift values are between 1 and 25
    elif mode == 'shiftvalue':
        try:
            start_shift, end_shift = map(int, text.split(','))
        except ValueError:
            return False, "\nPlease enter start and end shift values following this example format : 2, 20."

        if not (1 <= start_shift <= 25 and 1 <= end_shift <= 25):
            return False, "\nPlease only enter numbers between 1 and 25."

        if start_shift <= end_shift:
            return True, None
        else:
            return False, "\nInvalid. The end shift value must be equal to or larger than the start shift value."
    
    # Check formatting for input file
    elif mode == 'fileinput':
        invalid_chars = [':', '*', '?', '"', '<', '>', '|']
        valid_ext = ['txt']
        
        # Check for invalid characters in the file name
        for character in text:
            if character in invalid_chars:
                return False, f"Invalid character in path."
        
        # Check for the extension separators
        if text.count('.') <= 0:
            return False, f"\nNo file extension found. Please enter a .txt extension."

        # Check for the format / type of the extension (only accept text files)
        if not text.split('.')[-1].lower() in valid_ext:
            return False, f"\nInvalid extension. Extension must be in {valid_ext} format."

        # Check if the file exists
        if not os.path.isfile(text):
            return False, f"\nThe text file '{text}' does not exist. Please provide another file name."
        
        # Check if the file is empty
        if os.path.getsize(text) == 0:
            return False, f"\nThe file '{text}' is empty. Please provide a file with content."
        
    elif mode == 'directory':
        # Check if the directory exists
        if not os.path.exists(text):
            return False, f"\nThe directory '{text}' does not exist."
        
        # Check if the path is indeed a directory
        if not os.path.isdir(text):
            return False, f"\nThe path '{text}' is not a directory."

        # Check if the directory is readable 
        if not os.access(text, os.R_OK):
            return False, f"\nThe directory '{text}' is not accessible."
        
        # Check if the directory only contains .txt files
        files_in_directory = os.listdir(text)
        if not all(file.endswith('.txt') for file in files_in_directory):
            return False, f"\nInvalid. This directory '{text}' contains files other than .txt files."

        return True, None
    
    # Check formatting for output file
    elif mode == 'fileoutput':
        invalid_chars = [':', '*', '?', '"', '<', '>', '|']
        valid_ext = ['txt']

        # Check for invalid characters in the file name
        for character in text:
            if character in invalid_chars:
                return False, f"Invalid character in path."
            
        # Check for the extension separators
        if text.count('.') <= 0:
            return False, f"\nNo file extension found. Please enter a .txt extension."

        # Check for the format / type of the extension (only accept text files)
        if not text.split('.')[-1].lower() in valid_ext:
            return False, f"\nInvalid extension. Extension must be in {valid_ext} format."
        
        # Check that the output file name does not already exist
        if os.path.isfile(text):
            return False, f"\nThe file '{text}' already exists. Please provide a new file name."

        return True, None
    
    # Check if reference frequencies file is valid
    elif mode == 'frequencyfile':
        
        invalid_chars = [':', '*', '?', '"', '<', '>', '|']
        valid_ext = ['txt']
        
        # Check for invalid characters in the file name
        for character in text:
            if character in invalid_chars:
                return False, f"Invalid character in path."
        
        # Check for the extension separators
        if text.count('.') <= 0:
            return False, f"\nNo file extension found. Please enter a .txt extension."

        # Check for the format / type of the extension (only accept text files)
        if not text.split('.')[-1].lower() in valid_ext:
            return False, f"\nInvalid extension. Extension must be in {valid_ext} format."

        # Check if the file exists
        if not os.path.isfile(text):
            return False, f"\nThe text file '{text}' does not exist. Please provide another file name."
        
        # Check if the file is empty
        if os.path.getsize(text) == 0:
            return False, f"\nThe file '{text}' is empty. Please provide a file with content."
        
        # Check if format of file is correct
        with open(text, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue
                parts = line.split(',')
                if len(parts) != 2 or not parts[0].isalpha() or not parts[1].strip().replace('.', '', 1).isdigit():
                    return False, f"\nReference frequencies file '{text}' is not in the correct format."

        return True, None
    
    # Check if input type is an alphabet
    elif mode == 'alpha':
        return text.replace(" ", "").isalpha(), '\nPlease enter only alphabetical characters to proceed.'
    
    # Check if input type is bookean-type (y or n)
    elif mode == 'boolean':
        return text.lower() == 'y' or text.lower() == 'n', "\nPlease enter only either 'y' or 'n' to proceed.\n"
    
    # Check if input type is a valid operation id that exists
    elif mode == 'operationid':
        if not text.isnumeric():
            return False, "\nPlease enter numerical values only to proceed."
        
    return True, 'NaN'
      
# Question Validation for User Inputs
def question(questionText: str, mode: int, min_range = 1, max_range = 10, choices=None, num_choice=None, is_submenu=False) -> list([bool, str]):
                
    # Obtain input from the valid_input function and process under this function
    output = input(questionText)
    
    # Directly handle the 'X' input for exit
    if output.upper() == 'X':
        return 'X'
    
    # Checks based on input entered by user
    is_valid, reason = valid_input(output, mode, min_range = min_range, max_range = max_range, is_submenu=is_submenu)
    
    # If input is invalid
    while not is_valid:
        call_error(reason)
        
        # Print the selection menu again if the user enters a wrong input
        if choices is not None and num_choice is not None:
            print(f"Please select your choice: ({','.join(num_choice)})")
            for idx, choice in enumerate(choices):
                print(f'\t{idx + 1}. {choice}')
            
        output = input(questionText)
        is_valid, reason = valid_input(output, mode, min_range = min_range, max_range = max_range)
        
    # Checks if input type is a number (integer)
    if mode == 'integer':
        return int(output)
    
    # Return an output after checking through the validity of the user input
    return output

# Function to format and wrap texts in a column for a table
def format_column(content, width):
    return textwrap.fill(content, width).split('\n')

# Function to print a single row
def print_row(row, widths):
    lines = [format_column(cell, width) for cell, width in zip(row, widths)]
    max_lines = max(len(line) for line in lines)
    for i in range(max_lines):
        print("|" + "|".join(lines[j][i].ljust(widths[j]) if i < len(lines[j]) else " " * widths[j] for j in range(len(lines))) + "|")
        
# Function to display simple table
def display(shifts, max_shift_type_width, max_transformed_text_width):
    print(f"+{'-' * (max_shift_type_width + 2)}+{'-' * (max_transformed_text_width + 2)}+")

    for shift_type, transformed_text in shifts:
        print(f"| {shift_type:<{max_shift_type_width}} | {transformed_text:<{max_transformed_text_width}} |")
        print(f"+{'-' * (max_shift_type_width + 2)}+{'-' * (max_transformed_text_width + 2)}+")

# Function to return error message if input is invalid
def call_error(error_msg: str) -> None:
    print(error_msg)
    

    

