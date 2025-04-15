# File Name: shinker.py
# Student Name: Cam Shinker
# email: shinkecj@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 4/24/2025
# Course #/Section: IS 4010-002
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt 2 files and take a photo according to the decrypted data.

# Brief Description of what this module does: Contains Cam's work on the functions
# Citations: 

# Anything else that's relevant:


import json
import os

class shinker():
    def get_team_words(self, team_name, data_folder="Data"):
        """
        Retrieves words from 'English.txt' using indices from 'EncryptedGroupHints.json'
        associated with a given team name.

        Args:
            team_name (str): The name of the team.
            data_folder (str, optional): The name of the folder where the files are located.
                Defaults to "data".

        Returns:
            list: A list of words corresponding to the indices, or None if the team
                  is not found or an error occurs.  Returns an empty list if no words are found.
        """
        english_file_path = os.path.join(data_folder, "English.txt")
        hints_file_path = os.path.join(data_folder, "EncryptedGroupHints.json")

        try:
            # Read the list of words from 'English.txt'.
            with open(english_file_path, 'r') as english_file:
                words = [line.strip() for line in english_file]

            # Read the team hints from 'EncryptedGroupHints.json'.
            with open(hints_file_path, 'r') as hints_file:
                team_hints = json.load(hints_file)

            # Get the indices for the specified team.
            indices = team_hints.get(team_name)
            if indices is None:
                print(f"Team '{team_name}' not found in EncryptedGroupHints.json")
                return None

            # Extract the words based on the indices.
            # Check if indices is a list before proceeding.
            if isinstance(indices, list):
                try:
                    # Convert string indices to integers.
                    indices = [int(i) for i in indices]
                    result_words = [words[i] for i in indices]
                except ValueError:
                    print(f"Error: Invalid index value for team '{team_name}'.  Expected integer, found string.")
                    return None
            else:
                print(f"Error: Indices for team '{team_name}' is not a list.")
                return None
            return result_words

        except FileNotFoundError as e:
            print(f"Error: File not found - {e.filename}")
            return None
        except json.JSONDecodeError:
            print("Error: Invalid JSON in EncryptedGroupHints.json")
            return None
        except IndexError:
            print("Error: Index out of range.  Check the indices in EncryptedGroupHints.json and the number of words in English.txt")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
