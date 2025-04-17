# File Name: jacob.py
# Student Name: Ryan Jacob
# email: jacobry@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/24/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt 2 files and take a photo according to the decrypted data.

# Brief Description of what this module does: Contains Ryan's work on the functions
# Citations: https://chatgpt.com/

# Anything else that's relevant:

import os
import webbrowser

class jacob():
    def show_norman_dale_picture(self):
        """
        Opens the Norman Dale picture in the default web browser.
        """
        image_path = os.path.abspath(os.path.join("Data", "NormanDalePicture.jpg"))
        if not os.path.exists(image_path):
            print("Image not found:", image_path)
            return

        # Open the image in your default browser
        webbrowser.open(f'file://{image_path}')