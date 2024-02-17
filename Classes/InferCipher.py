#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : InferCipher.py
#--------------------------------------------------------------

# Import necessary classes and libraries
from Classes.LetterFrequency import LetterFrequency
from Classes.CaesarCipher import CaesarCipher

# Define InferCipher class
class InferCipher:
    """
    Class for inferring the key of a Caesar Cipher based on letter frequency analysis
    and decrypting text using the inferred key.
    """

    def __init__(self):
        """
        Constructor for the InferCipher class.
        Initializes the reference frequencies, LetterFrequency, and CaesarCipher instances.
        """
        self._reference_freq = {}  # Stores reference frequencies for letters
        self._letterfrequency = LetterFrequency()  # Instance for letter frequency analysis
        self._caesarcipher = CaesarCipher()  # Instance for Caesar Cipher operations

    def load_reference_frequencies(self, file_path):
        """
        Load reference frequencies from a file and store them.
        :param file_path: Path to the file containing reference frequencies.
        :return: Dictionary of reference frequencies.
        """
        filecontent = self._caesarcipher.read_file(file_path)
        for line in filecontent.strip().split('\n'):
            parts = line.strip().split(',')
            if len(parts) == 2:
                letter, frequency = parts[0], float(parts[1])
                self._reference_freq[letter] = frequency
        return self._reference_freq

    def _calculate_chi_squared(self, encrypted_frequency, shift):
        """
        Calculate the chi-squared statistic for a given shift on the encrypted frequencies.
        :param encrypted_frequency: Frequencies of letters in the encrypted text.
        :param shift: Shift value to be tested.
        :return: Chi-squared statistic for this shift.
        """
        chi_sq = 0
        for letter, encrypted_freq in encrypted_frequency.items():
            shifted_letter = chr((ord(letter) - shift - 65) % 26 + 65)
            expected_frequency = self._reference_freq.get(shifted_letter, 0)
            if expected_frequency > 0:
                chi_sq += ((encrypted_freq - expected_frequency) ** 2) / expected_frequency
        return chi_sq

    def infer_cipher_key(self, encrypted_text):
        """
        Infer the key of a Caesar Cipher based on letter frequency analysis.
        :param encrypted_text: The encrypted text whose key is to be inferred.
        :return: Inferred key.
        """
        self._letterfrequency.set_text(encrypted_text)
        self._letterfrequency.calculate_letter_frequencies()
        encrypted_frequency = dict(self._letterfrequency.get_letter_frequency())
        chi_sq_stats = [self._calculate_chi_squared(encrypted_frequency, shift) for shift in range(26)]
        return chi_sq_stats.index(min(chi_sq_stats))

    def decrypt_text(self, encrypted_text):
        """
        Decrypt text using the inferred Caesar Cipher key.
        :param encrypted_text: The encrypted text to be decrypted.
        :return: Tuple containing the decrypted text and the inferred key.
        """
        inferred_key = self.infer_cipher_key(encrypted_text)
        self._caesarcipher.set_key(inferred_key)
        decrypted_text = self._caesarcipher.cipher(encrypted_text, encrypt=False)
        return decrypted_text, inferred_key