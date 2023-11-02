"""

HW : 4
Problem : 1
Author : Kalla Naga Suresh

"""
import re

def remove_string_from_file(file_path, word_to_remove):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Replace the specified string with an empty string
        expression = rf'{word_to_remove}|{word_to_remove.capitalize() + " "}|{word_to_remove + " "}|{word_to_remove.capitalize()}'

        # print(expression)
        modified_content= re.sub(expression,'',file_content)
        # Open the file in write mode and write the modified content
        with open(file_path, 'w') as file:
            file.write(modified_content)
        return 1
    except:
        return 0

if __name__ == "__main__":
    file_path = input("Enter a filename : ")
    string_to_remove = input("Enter the string to be Removed: ")

    done=remove_string_from_file(file_path, string_to_remove)
    if(done):
        print("Done")
    else:
        print("String Couldn't Found / Delete")