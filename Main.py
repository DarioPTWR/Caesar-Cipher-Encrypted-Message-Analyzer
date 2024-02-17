#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : Main.py
#--------------------------------------------------------------

# Import relevant libraries and modules
import os  # Import the os module for file and directory operations
import sys  # Import the sys module for system-related functionality

# Set the current working directory to the directory containing this script
os.chdir((os.path.abspath(os.path.dirname(__file__))))

# Append the 'Application' directory to the Python import path to make its modules accessible
sys.path.append('Application')

# Import the menus class from the 'application.GUI' module
from Application.GUI import GUI

# Create an instance of the menus class
app = GUI()

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the application by calling the 'start' method of the 'app' instance
    app.start()
        
    

