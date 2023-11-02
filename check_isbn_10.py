
"""
HW 2
Problem 1
Author : Kalla Naga Suresh

"""

# Define a function to calculate the ISBN-10 checksum
def calculate_isbn_10(first_nine_digits):
    checksum = 0  # Initialize the checksum variable

    # Calculate the checksum using the provided formula
    for i in range(9):
        digit = int(first_nine_digits[i])  # Get the current digit as an integer
        checksum += (i + 1) * digit  # Apply the formula to calculate the checksum

    checksum %= 11  # Calculate the checksum modulo 11

    # If the checksum is 10, represent it as 'X'
    if checksum == 10:
        return first_nine_digits + 'X'
    else:
        return first_nine_digits + str(checksum)  # Convert the checksum to a string and append it

# Define the main program function
if __name__ == "__main__":
    print("Enter the first 9 digits of an ISBN-10 as a string:")
    first_nine_digits = input()  # Get the user's input as a string

    # Check if the input has exactly 9 digits and consists only of digits
    if len(first_nine_digits) != 9 or not first_nine_digits.isdigit():
        print("Invalid input. Please enter exactly 9 digits")
    else:
        isbn_10 = calculate_isbn_10(first_nine_digits)  # Calculate the ISBN-10
        print(f"The ISBN-10 number is {isbn_10}")  # Display the calculated ISBN-10
