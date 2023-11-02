"""
HW 2
Problem 2
Author : Kalla Naga Suresh

"""

def is_valid_credit_card(card_number):
    # Convert the card number to a list of integers
    digits = [int(digit) for digit in str(card_number)]

    # Double every second digit from right to left and sum the digits
    total = 0
    for i in range(len(digits) - 2, -1, -2):
        double_digit = digits[i] * 2
        if double_digit >= 10:
            double_digit = (double_digit % 10) + 1
        total += double_digit

    # Add all the digits in the odd positions from right to left
    total += sum(digits[-1::-2])

    # Check if the total is divisible by 10
    if total % 10 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        card_number = int(input("Enter a credit card number as an integer: "))  # Get user input as an integer

        if is_valid_credit_card(card_number):  # Check if the credit card number is valid
            print("The credit card number is valid.")
        else:
            print("The credit card number is invalid.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # Handle invalid input

