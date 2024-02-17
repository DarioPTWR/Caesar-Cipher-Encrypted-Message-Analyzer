#--------------------------------------------------------------
# ST1507 DSAA | CA1 Assignment
#--------------------------------------------------------------
# Author    : Dario Prawara Teh Wei Rong
# StudentID : 2201858
# Class     : DAAA/FT/2B/04
# Date      : 20-Nov-2023
# Filename  : SelectionPage.py
#--------------------------------------------------------------

# Import relevant libraries and modules
from Application.Page import Pages
from Application.Utils import call_error, enter, question

class SelectionPage(Pages):
    def __init__(self, mainMenu, caesarcipher, selectionMenu, is_submenu=False, **kwargs) -> None:
        super().__init__(caesarcipher, **kwargs)
        
        self.mainMenu = mainMenu
        
        # Choice: List of possible options the user can input and select from to proceed to another part of the program
        # Action: Instructs what the program will display and execute based on the user's initial input under self.__choice
        # Num_Choice: Shows an incremental list of numbers if there is a list of options available for the user to select from
        self.__choice = list(selectionMenu.keys())
        self.__action = list(selectionMenu.values())
        self.num_choice = [str(i + 1) for i in range(len(self.__choice))]
        self.is_submenu = is_submenu  # New attribute to distinguish submenu
    
    def __call__(self):
        while self.mainMenu.active:
            if self.is_submenu:
                print(f"\nPlease select your choice: ({','.join(self.num_choice)})")
            else:
                print(f"\nPlease select your choice: ({','.join(self.num_choice)})")

            for idx, choice in enumerate(self.__choice):
                print(f'\t{idx + 1}. {choice}')

            try:
                chosen = question(f'Enter choice: ', mode='integer', min_range=1, 
                                  max_range=len(self.__choice), choices=self.__choice, 
                                  num_choice=self.num_choice)

                # Execute the selected action
                exit = self.__action[chosen - 1]()

                # Check if the action signals to exit
                # For main menu, exit would be True to exit the application
                # For submenu, break if True is returned (to return to the main menu)
                if self.is_submenu and exit:
                    break
                elif not self.is_submenu and exit:
                    return  # Exit the __call__ method, effectively exiting the application

            except Exception as e:
                call_error(e)
                enter()
