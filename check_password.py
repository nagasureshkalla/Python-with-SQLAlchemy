
"""
HW 1
Problem 1
Author : Kalla Naga Suresh

"""
import re

def check_password(password):

    # Check if the password has at least eight characters
    # Check if the password contains at least two digits
    # Check if the password consists of only letters and digits
    if len(password) < 8 or sum(c.isdigit() for c in password) < 2 or not re.match("^[a-zA-Z0-9]+$", password):
        return False
    else:
        return True

if __name__ == '__main__':
    # Taking input from User
    password=input("Please Enter Password")
    # printing Valid/Invalid based on returned value of check_password method
    if check_password(password):
        print("valid Password" )
    else :
        print("invalid Password")