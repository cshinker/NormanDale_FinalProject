# File Name: elmore.py
# Student Name:  Luke elmore
# email: elmorels@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/24/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt 2 files and take a photo according to the decrypted data.

# Brief Description of what this module does: Contains Luke's work on the functions
# Citations: 

# Anything else that's relevant:
import json
from cryptography.fernet import Fernet

class elmore():
    def decrypt_movie(self, file_path: str, team_name: str, fernet_key: str) -> str:
        # Load JSON data
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Get encrypted message
        encrypted_message = data.get(team_name)
        if not encrypted_message:
            raise ValueError(f"No message found for team '{team_name}'.")

        # If it's a list, join into one string
        if isinstance(encrypted_message, list):
            encrypted_message = ''.join(encrypted_message)

        # Initialize Fernet
        fernet = Fernet(fernet_key)

        # Decrypt
        decrypted_message = fernet.decrypt(encrypted_message.encode())

        return decrypted_message.decode('utf-8')
