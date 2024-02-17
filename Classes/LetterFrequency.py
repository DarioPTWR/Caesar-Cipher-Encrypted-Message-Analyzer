#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : LetterFrequency.py
#--------------------------------------------------------------

# Import relevant libraries and modules
import string
import math

# Define LetterFrequency class
class LetterFrequency:
    def __init__(self, text=None):
        """
        Initializes a new instance of the LetterFrequency class.
        :param text: Optional initial text to analyze.
        """
        self._text = text
        self._letter_frequencies = None
        self._alphabet = dict.fromkeys(string.ascii_uppercase, 0)
        self._frequency_output = []

    def set_text(self, text):
        """
        Sets the text for frequency analysis.
        :param text: Text to be analyzed.
        """
        self._text = text

    def _normalize_text(self, text):
        """
        Converts the text to uppercase and removes non-alphabetic characters.
        :param text: Input text to be normalized.
        :return: Normalized text.
        """
        return ''.join(char.upper() for char in text if char.isalpha())

    def calculate_letter_frequencies(self):
        """
        Calculates the frequency of each letter in the text.
        """
        normalized_text = self._normalize_text(self._text)
        
        # Manually count the letters based on the standardized text from normalized_text function
        letter_count = {}
        for letter in normalized_text:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Update the frequencies for the letters in the input text
        for letter, count in letter_count.items():
            if letter in self._alphabet:
                self._alphabet[letter] += count
            else:
                self._alphabet[letter] = count

        self._letter_frequencies = sorted(self._alphabet.items(), key=lambda item: item[0])
        
    def get_letter_frequency(self):
        """
        Gets the calculated letter frequencies.
        :return: Sorted list of letter frequencies.
        """
        if self._letter_frequencies is None:
            raise ValueError("Letter frequencies not calculated. Call calculate_letter_frequencies first.")
        return self._letter_frequencies
    
    def display_letter_frequency(self):
        """
        Displays the frequency of each letter as a bar chart, along with the top 5 frequencies.
        :return: String representation of the letter frequency chart.
        """
        if self._letter_frequencies is None:
            raise ValueError("Letter frequencies not calculated. Call calculate_letter_frequencies first.")
        
        letter_frequencies = self.get_letter_frequency()
        total_frequency = sum(frequency for _, frequency in letter_frequencies)

        # Sort the letter frequencies in descending order
        sorted_frequencies = sorted(letter_frequencies, key=lambda x: x[1], reverse=True)

        # Determine the percentage value for letters and create a dictionary for the top 5
        top_5_frequencies = {letter: (frequency / total_frequency) * 100 for letter, frequency in sorted_frequencies[:5]}

        # Calculate the starting index for the "TOP 5 FREQ" label to be centered
        top_5_length = 5
        start_index = (26 - top_5_length) // 2

        # Display the bar frequency chart for all letters
        for i in range(26):
            letter = chr(65 + i)
            frequency = dict(letter_frequencies).get(letter, 0)
            percentage = (frequency / total_frequency) * 100
            space = "" if len(f"{percentage:.2f}") > 4 else " "
            graph = '  '.join('*' if math.ceil((frequency / total_frequency) * 26) > (25 - i) else ' ' for _, frequency in letter_frequencies)

            # Print the graph and the percentage
            line = f"{'  '}{graph} | {letter}-{space}{percentage:.2f}% "

            # Determine if we are at the starting index for the "TOP 5 FREQ" label
            if i == start_index:
                line += "\tTOP 5 FREQ"

            # Print the dashed line below the "TOP 5 FREQ" label
            if i == start_index + 1:
                line += "\t----------"

            # Determine if we are within the range to print the top 5 frequencies
            if start_index + 1 < i <= start_index + 1 + top_5_length:
                top_5_letter = list(top_5_frequencies.keys())[i - start_index - 2]
                top_5_percentage = top_5_frequencies[top_5_letter]
                top_5_space = "" if len(f"{top_5_percentage:.2f}") > 4 else " "
                line += f"\t| {top_5_letter}-{top_5_space}{top_5_percentage:.2f}%"
                
            self._frequency_output.append(line)

        # Display the respective letters (A-Z) above the horizontal line
        letters = '  '.join(chr(65 + i) for i in range(26))
        self._frequency_output.append(f'{"_" * 79}|\n{"  "}{letters}')
        
        return '\n'.join(self._frequency_output)
