'''
This is a ROT-x program to help
decrypt a ROT encoded message

This program will show all rotations

Directions:
Input encrypted text 
    * It is assumed that it is all lower case
    * It is assumed that there are no spaces
'''

print("\nThis is a ROT decoder that will show all rotations")

cipher = input("Please input the text you want to decode (no spaces or upper case): ")
print("\n")

i = 1
decoded = ""

while i <= 25:
    for elem in cipher:
        number = ord(elem) + i

        if number >= 123:
            temp_number = number - 123
            number = 97 + temp_number

        decoded += chr(number)

    print("ROT-" + str(i) + ": " + decoded)

    i += 1
    decoded = ""

print("\n")
