# File Name: main.py
# Student Name: Cam Shinker, Luke Elmore, Ryan Jacob
# email: shinkecj@mail.uc.edu, elmorels@mail.uc.edu, jacobry@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/24/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt 2 files and take a photo according to the decrypted data.

# Brief Description of what this module does: Contains the entry point code for the assignment
# Citations: 

# Anything else that's relevant:

from function_package.shinker import *
from function_package.elmore import *

if __name__ == "__main__":
    step2 = shinker()
    hints = step2.get_team_words("Norman Dale")
    print(hints)

    step3 = elmore()
    fernet_key = "tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI="
    message = step3.decrypt_movie("Data/TeamsAndEncryptedMessagesForDistribution.json", "Norman Dale", fernet_key)
    print("Decrypted message:", message)

