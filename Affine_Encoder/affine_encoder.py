'''
Affine encoder
Use python3
'''
a = input("Please input the first variable (integer between 1 and 26): ")
b = input("Please input the second variable (integer between 1 and 26): ")

if int(a) >= 27 or int(b) >= 27:
    print("invalid integer input")
    exit()

elif int(a) < 1 or int(b) < 1:
    print("invalid integer input")
    exit()

print("\nYou have inputted for variable A: " + a)
print("You have inputted for variable B: " + b + "\n")

string = input("Please input the string you want to encode: ")
encoded = ""

for elem in string:
    numb = ord(elem) - 97
    letter = ((numb * int(a)) + int(b)) % 26
    letter = letter + 97
    letter = chr(letter)
    encoded += letter
    ### print(encoded)

print("\nUsing the string: " + string + " and numbers " + a + " and " + b)
print("We get: " + encoded)
