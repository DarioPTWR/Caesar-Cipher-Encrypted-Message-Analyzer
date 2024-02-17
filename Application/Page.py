#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : Page.py
#--------------------------------------------------------------

# Import relevant libraries and modules
from Classes.CaesarCipher import CaesarCipher

class Pages():
    def __init__(self, caesarcipher: CaesarCipher) -> None:
        self.caesarcipher = caesarcipher
        
    def __call__(self) -> None:
        """Each subclass/child page will be called to 'flip to' that page.
        Calling a page can perhaps be thought of as visiting said page.
        """
        NotImplementedError("Subclass must implement abstract method")
    