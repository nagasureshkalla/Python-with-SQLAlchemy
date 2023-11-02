
"""
HW 1
Problem 3
Author : Kalla Naga Suresh

"""

# getNumber Method returns the Number based on the characters
def getNumber(uppercaseLetter):
    if uppercaseLetter in ['A','B','C']:
        return '2'
    elif uppercaseLetter in ['D','E','F']:
        return '3'
    elif uppercaseLetter in ['G','H','I']:
        return '4'
    elif uppercaseLetter in ['J','K','L']:
        return '5'
    elif uppercaseLetter in ['M','N','O']:
        return '6'
    elif uppercaseLetter in ['P','Q','R','S']:
        return '7'
    elif uppercaseLetter in ['T','U','V']:
        return '8'
    elif uppercaseLetter in ['W','X','Y','Z']:
        return '9'
    else:
        return uppercaseLetter


if __name__ == '__main__':

    # enter a phone number as a string
    phone_number = input("Enter a string: ")
    # phone number with letters converted to digits is stored in String num
    num=""
    for i in phone_number:
        num += getNumber(i.upper())

    print(num)
